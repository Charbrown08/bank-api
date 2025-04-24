from fastapi import FastAPI
from app.api.v1.routes.account import router as account_router

app = FastAPI(title="API Bank", version="1.0.0", description="RESTful API for managing bank accounts with FastAPI and MongoDB.")

app.include_router(account_router, prefix="/api/v1")
