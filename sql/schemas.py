from pydantic import BaseModel


class NewUni(BaseModel):
    uniName: str

    class Config:
        from_attributes = True


class NewQuestion(BaseModel):
    questionText: str

    class Config:
        from_attributes = True


class NewScore(BaseModel):
    questionId: int
    uniId: int
    score: int

    class Config:
        from_attributes = True


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