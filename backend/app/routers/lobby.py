from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import lobby_service


router = APIRouter()

class JoinLobbyRequest(BaseModel):
    user_id: str

@router.post("/join-lobby")
def join_lobby(request: JoinLobbyRequest):
    try:
        lobby_info = lobby_service.create_or_join_lobby(request.user_id)
        return lobby_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
