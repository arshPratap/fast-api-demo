import uvicorn
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/openshift/welcome")
async def greet():
    return {"message":"Welcome to Openshift Result"}


if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0',port=9999)
