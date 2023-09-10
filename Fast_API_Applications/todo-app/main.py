from fastapi import FastAPI
from models import Todo

app = FastAPI()

tasks = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():
   return {"todos":tasks}
   
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
   for task in tasks:
      if todo_id==task.id:
         return {"task":task.task}
   return {"task":[]}

@app.post("/todos")
async def create_todo(todo: Todo):
   tasks.append(todo)
   return {"message":"Task is successfully added"}

@app.delete("/todos/{todo_id}")
async def get_todo(todo_id:int):
   for task in tasks:
      if todo_id==task.id:
         tasks.remove(task)
         return {"message":"Deleted Successfully"}
   return {"message":"Task not  present"}




