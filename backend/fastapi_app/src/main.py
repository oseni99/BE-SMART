from fastapi import FastAPI
from src.database import Base, engine
from src.api import router as api_router

app = FastAPI(
    title="FastAPI App",
    description="FastAPI App Description",
    version="0.0.1",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)
