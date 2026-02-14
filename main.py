from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# Create an instance of FastAPI Object
app = FastAPI()

# Create the Base route

@app.get("/")
def router():
    return {"data": {"Name": "Tamer",
                   "Age": 22}}

@app.get("/blog")
# Pass a Query Parameter to the function so we can control the limit of the blogs for ex
# limit: int >> set an acceptable input data type for the url 
# limit: int = 10 >> set a default value for (limit ) so that if the url doesn't contain it , put the default one that's make the limit (optional) not maindatory
# sort: Optional[str] = None >> if we want to set an optional query parameter if it not exist in the url will not affect on the api , if exist the allowed data type is string.
def blog(limit: int = 10,published: bool = False, sort: Optional[str] = None):
    # return unpublished
    if published and sort:
        return {"data": f"{limit} published blogs and it's sort is {sort}"}
    elif published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} blogs from the db"}

# Id: int >> Is the path parameter
# limit: int = 10 >> Is the qurery parameter for this route
# Test it >> http://127.0.0.1:8000/blog/5/comments?limit=5
@app.get("/blog/{id}/comments") # {id} Here represent a dynamic route so any number we will type it will be returned by the function
def comments(id: int, limit: int = 15): # id: int to set the acceptable data type for this function
    return {f"{limit} comments from the db with id of {id}:"}


############################# Create Blog Using Post Method ###########################
# Create a pydantic BaseModel class 
class Blog(BaseModel):
    # make the fields that will be in the response 
    title: str
    body: str
    published: Optional[bool] # Set the published field as optional

@app.post("/blog")
# request:Blog >> (request) here represent the request body that the client will send & (Blog) here is the Base Model from bydantic 
def create_blog(request:Blog):
    return {"data": f"my {request.title} is created"}


