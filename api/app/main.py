from fastapi import FastAPI


#Create Schemas:
from pydantic import BaseModel
class Job(BaseModel):
    id: int
    job: str

#Start FastAPI:
app = FastAPI()


#Create Endpoints:
@app.get("/")
async def root():
    return {"message": "Hello World test"}

#Jobs endpoints:
@app.get("/jobs")
async def jobs():
    

@app.get("/test_manuel")
async def test_manuel():
    return {"message": "Test Manuel is awesome"}


