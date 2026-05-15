from fastapi import APIRouter

from my_api.schemas.root import RootResponse

router = APIRouter()


@router.get("/", response_model=RootResponse)
def read_root() -> RootResponse:
    return RootResponse(message="Hello from buzzword_bingo API")
