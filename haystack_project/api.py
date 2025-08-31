from fastapi import FastAPI,Request,Form,Response
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import uvicorn
import os
import json
from dotenv import load_dotenv
from QAsystem.retrieverandgeneration import get_result

app=FastAPI()
templates=Jinja2Templates(directory='F:\\Tapas\\Learning\\GenAI\\haystack_project\\templates')


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/get_answer")
async def gets_answer(questions: str=Form(...)):
    answer=get_result(questions)
    response_data = jsonable_encoder(json.dumps({"answer": answer}))
    res = Response(response_data)
    return res
    

# if __name__=='__main__':
#     uvicorn.run(app,host='0.0.0.0',port=8080)