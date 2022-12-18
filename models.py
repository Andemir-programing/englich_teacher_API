from pydantic import BaseModel


class AnswerRequestBody(BaseModel):
    question_id: int
    answer: str


class LetterRequestBody(BaseModel):
    question_id: int
    answer: str