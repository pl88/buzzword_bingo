from fastapi import FastAPI

from my_api.routers.root import router as root_router
from my_api.routers.board import router as board_router

app = FastAPI(title="buzzword_bingo API")
app.include_router(root_router)
app.include_router(board_router)
