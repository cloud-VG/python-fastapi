"""DOCS
"""

__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmai.vishwajeet@gmail.com'
__date__ = '09/04/2021'

# Built-in Imports
import uvicorn
from fastapi import FastAPI

# Custom Imports
import models
from database import engine
from audio_router import router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=8000)
