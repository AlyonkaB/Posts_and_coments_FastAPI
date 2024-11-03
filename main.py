from fastapi import FastAPI
from posts import router as post_router


app = FastAPI()

app.include_router(post_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
