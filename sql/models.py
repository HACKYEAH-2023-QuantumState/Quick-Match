from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class University(Base):
    __tablename__ = "universities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True, index=True)
    scores = relationship("Score", back_populates="university")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(400))
    scores = relationship("Score", back_populates="question")


class Score(Base):
    __tablename__ = "scores"

    uniId = Column(Integer, ForeignKey(University.id), primary_key=True)
    questionId = Column(Integer, ForeignKey(Question.id), primary_key=True)
    score = Column(Integer)
    university = relationship("University", back_populates="scores")
    question = relationship("Question", back_populates="scores")




