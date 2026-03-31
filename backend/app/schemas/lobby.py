from pydantic import BaseModel

class JoinLobbyRequest(BaseModel):
    user_id: str

class Message(BaseModel):
    lobby_id: str
    from_user: str
    to_user: str
    message: str