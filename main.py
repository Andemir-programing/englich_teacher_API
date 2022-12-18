from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse, JSONResponse

from helper import Helper
from models import AnswerRequestBody, LetterRequestBody

# Endpoints:
# word/guess,   word/check,    word/result
# letter/guess,   letter/check,    letter/result

app = FastAPI()  # create API service
helper = Helper()  # database, questions


@app.get("/word/guess")
def guess_word():
    return helper.generate_question_word()


@app.post("/word/check")
def guess_word_check(user_answer: AnswerRequestBody):
    return helper.check_answer(user_answer.question_id, user_answer.answer)

@app.get("/word/result")
def guess_word_result():
    return helper.db[helper.question_id]

@app.get("/letter/guess")
def guess_letter():
  return helper.generate_question_letter()

@app.post("/letter/check")
def guess_letter_check(user_answer: LetterRequestBody):
  if user_answer.answer == helper.db[user_answer.question_id]:
    return 'is correct : True'
  else:
    return 'is correct : False'

@app.get('/letter/result')
def letter_result():
    return helper.db[helper.question_id]

if __name__ == "__main__":
    uvicorn.run(app, port=8000)