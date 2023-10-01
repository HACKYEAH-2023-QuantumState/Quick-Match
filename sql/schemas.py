from pydantic import BaseModel


class Question(BaseModel):
    lastQuestions: dict[int, int]

    class Config:
        from_attributes = True





class NextQuest(BaseModel):
    questionId: int
    questionText: str

    class Config:
        from_attributes = True


class Response(BaseModel):
    question: NextQuest
    uni_rank: list

    class Config:
        from_attributes = True