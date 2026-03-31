from fastapi import APIRouter, HTTPException
from app.schemas.lobby import JoinLobbyRequest, Message
from app.services import lobby_service


router = APIRouter()


@router.post("/join-lobby")
def join_lobby(request: JoinLobbyRequest) -> dict:
    try:
        lobby_info = lobby_service.create_or_join_lobby(request.user_id)
        return lobby_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/send-message")
def send_message(message: Message):

    
    
