from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.testing import skip
import sql.models
import sql.schemas
from sql.database import get_db
router = APIRouter(prefix="/admin")


@router.post("/addUni")
async def add_uni(uni: sql.schemas.NewUni, db=Depends(get_db)):
    new_uni = sql.models.University()
    new_uni.name = uni.uniName

    db.add(new_uni)
    db.commit()
    # db.refresh()
    return new_uni

@router.post("/addQuestion")
async def add_question(q: sql.schemas.NewQuestion, db=Depends(get_db)):
    new_q = sql.models.Question()
    new_q.text = q.questionText

    db.add(new_q)
    db.commit()
    # db.refresh()
    return new_q


@router.post("/addScore")
async def add_score(score: sql.schemas.NewScore, db=Depends(get_db)):
    new_score = sql.models.Score()
    new_score.questionId = score.questionId
    new_score.uniId = score.uniId
    new_score.score = score.score

    db.add(new_score)
    db.commit()
    return score


