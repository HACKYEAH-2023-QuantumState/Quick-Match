from pydantic import BaseModel


class Question(BaseModel):
    lastQuestions: dict[int, int]

    class Config:
        from_attributes = True


class Response(BaseModel):
    questionId: int
    questionText: str
    class Config:
        from_attributes = True



