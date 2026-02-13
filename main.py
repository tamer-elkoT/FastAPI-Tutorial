from fastapi import FastAPI


# Create an instance of FastAPI Object
app = FastAPI()

# Create the Base route

@app.get("/")
def router():
    return {"data": {"Name": "Tamer",
                     "Age": 22}}
@app.get("/blog")
def blog():
    return {"data": "This Is Our Plog"}

@app.get("/blog/comment")
def show_comment():
    return {"data": "Here is our comments"}

@app.get("/blog/{id}") # {id} Here represent a dynamic route so any number we will type it will be returned by the function
def index(id: int): # id: int to set the acceptable data type for this function
    return {"You are in the index of:": id}



