from fastapi import FastAPI

from my_api.routers.root import router as root_router

app = FastAPI(title="buzzword_bingo API")
app.include_router(root_router)
