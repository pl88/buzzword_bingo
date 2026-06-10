from pydantic import BaseModel


class BoardResponse(BaseModel):
    message: list[str]
