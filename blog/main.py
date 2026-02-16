from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str

# Create a Blog
@app.post("/blog")
# Create a p
# def create_blog(title, body):
#     return {"title":title, "body":body}
def create_blog(request:Blog): # Here we create a request it's type is Blog
    return request
