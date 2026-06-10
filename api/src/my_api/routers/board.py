from fastapi import APIRouter

from my_api.schemas.board import BoardResponse

from my_api.core.board import get_buzzwords_list

router = APIRouter()


@router.get("/board", response_model=BoardResponse)
def read_board() -> BoardResponse:
    
    return BoardResponse(message=get_buzzwords_list())
