import random
import secrets
import string

import sql.models
import sql.database


def populate(uni_count, question_count):
    db = sql.database.SessionLocal()
    for uni in range(1,uni_count):
        new_uni = sql.models.University()
        new_uni.name = get_random_name()
        db.add(new_uni)

    for question in range(1,question_count):
        new_question = sql.models.Question()
        new_question.text = get_random_name()
        db.add(new_question)

    for uni_index in range(1, uni_count):
        for question_index in range(1, question_count):
            new_score = sql.models.Score()
            new_score.questionId = question_index
            new_score.uniId = uni_index
            new_score.score = random.randrange(11)
            db.add(new_score)

    db.commit()
    db.close()






def get_random_name():
    return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(20))