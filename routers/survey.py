import math

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.testing import skip

import sql
from sql.database import get_db
from sql.schemas import Response, NextQuest

router = APIRouter(prefix="/survey")


@router.get("/")
async def post(db=Depends(get_db)):
    answers = {1: 10}
    universities = db.query(sql.models.University).all()

    results = []

    for uni in universities:
        uni_score = 0
        for ans_id, ans_score in answers.items():
            question_score = db.query(sql.models.Score).filter(sql.models.Score.uniId == uni.id,
                                                               sql.models.Score.questionId == ans_id).first()
            if question_score is None:
                question_score = 0
            uni_score += ans_score * question_score.score

        results.append((uni.id, uni_score))

    results.sort(reverse=True, key=lambda val: val[1])

    all_questions = db.query(sql.models.Question).all()

    further_question = []
    for quest in all_questions:
        if quest.id not in answers.keys():
            further_question.append(quest)



    question_rank = []
    for q in further_question:

        for i in range(min(len(further_question)-3,1)):
            u1_mult = db.query(sql.models.Score).filter(sql.models.Score.uniId == results[0][0],
                                                                   sql.models.Score.questionId == q.id).first()
            u2_mult = db.query(sql.models.Score).filter(sql.models.Score.uniId == results[1][0],
                                                                   sql.models.Score.questionId == q.id).first()
            if u1_mult is None:
                u1_mult = sql.models.Score()
                u1_mult.score = 0

            if u2_mult is None:
                u2_mult = sql.models.Score()
                u2_mult.score = 0

            qr = abs(u1_mult.score-u2_mult.score)
            question_rank.append((qr, q))

    question_rank.sort(reverse=True, key=lambda val:val[0])

    print(question_rank)
    resp = Response(question = NextQuest(questionId = question_rank[0][1].id, questionText = question_rank[0][1].text),uni_rank = results)
    return resp
    # return (q.id, q.text)