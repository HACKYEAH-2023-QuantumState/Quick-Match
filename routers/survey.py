import math
from typing import Iterable

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.testing import skip

import sql
from sql.database import get_db
from sql.models import University
from sql.schemas import Response, NextQuest

router = APIRouter(prefix="/survey")


def get_unis_score(universities: Iterable[University], answers: dict, db):
    results = []

    for uni in universities:
        uni_score = 0
        for ans_id, ans_score in answers.items():
            question_score = db.query(sql.models.Score).filter(sql.models.Score.uniId == uni.id, sql.models.Score.questionId == ans_id).first()
            if question_score is None:
                question_score = sql.models.Score()
                question_score.score = 0
            uni_score += ans_score * question_score.score

        results.append((uni.id, uni_score))
    return results

def get_ot_yet_answered_questions(answers, db):
    all_questions = db.query(sql.models.Question).all()

    further_question = []
    for quest in all_questions:
        if quest.id not in answers.keys():
            further_question.append(quest)
    return further_question

def question_diff_for_given_unis(db,u1_id, u2_id, q_id):
    u1_score: sql.models.Score = db.query(sql.models.Score).filter(sql.models.Score.uniId == u1_id,
                                                sql.models.Score.questionId == q_id).first()
    u2_score: sql.models.Score = db.query(sql.models.Score).filter(sql.models.Score.uniId == u2_id,
                                                sql.models.Score.questionId == q_id).first()
    u1 = 0
    u2 = 0

    if u1_score is not None:
        u1 = u1_score.score

    if u2_score is not None:
        u2 = u1_score.score

    return abs(u1-u2)

@router.post("/")
async def post(answers: dict[int, int], db=Depends(get_db), threshold=0.4, desired_unis = 3):
    desired_unis = int(desired_unis)
    threshold = float(threshold)

    universities: Iterable[sql.models.University] = db.query(sql.models.University).all()

    results = get_unis_score(universities,answers,db)
    results.sort(reverse=True, key=lambda val: val[1])

    further_question = get_ot_yet_answered_questions(answers, db)

    threshold_meet = False
    if len(results) > desired_unis and results[0][1] != 0:
        tr_pr = abs(float(results[desired_unis - 2][1] - results[desired_unis - 1][1]) / results[0][1])
        print(tr_pr)
        if tr_pr >= threshold:
            threshold_meet = True

    nxt = NextQuest(questionId=0, questionText="")
    if len(further_question) > 0 and not threshold_meet :
        question_rank = []
        for q in further_question:

            for i in range(max(min(len(further_question)-1,3),0)):
                qr = question_diff_for_given_unis(db, results[0][0], results[i+1][0], q.id)
                question_rank.append((qr, q))

        question_rank.sort(reverse=True, key=lambda val:val[0])

        nxt = NextQuest(questionId = question_rank[0][1].id, questionText = question_rank[0][1].text)
    results_uni = []
    for r in results:
        u: sql.models.University = db.query(sql.models.University).filter(sql.models.University.id ==r[0]).first()
        results_uni.append((r[0], {"id": u.id, "name": u.name}))
    resp = Response(question = nxt,uni_rank = results_uni[0:min(desired_unis,len(results_uni))])

    return resp
    # return (q.id, q.text)