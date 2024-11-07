from fastapi import FastAPI
from routes.main import api_router

app = FastAPI()
app.include_router(api_router)
