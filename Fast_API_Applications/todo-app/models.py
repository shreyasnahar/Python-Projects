from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI provides inbuilt data validation

class Todo(BaseModel):
   id: int
   task: str
