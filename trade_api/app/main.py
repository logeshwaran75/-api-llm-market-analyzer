from fastapi import FastAPI
from app.routes.analyze import router

app = FastAPI(
    title="Trade Opportunities API"
)

app.include_router(router)