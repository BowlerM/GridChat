import random
from datetime import datetime, timezone

class Lobby:
    GRID_WIDTH = 10
    GRID_HEIGHT = 10

    def __init__(self, lobby_id: str):
        self.lobby_id = lobby_id
        self.users = {}
        self.grid = {}
        self.messages = []

    def add_user(self, user_id: str):
        import random

        x = random.randint(0, self.GRID_WIDTH)
        y = random.randint(0, self.GRID_HEIGHT)

        self.users[user_id] = {"x": x, "y": y}
        self.grid[(x, y)] = user_id
        return {"x": x, "y": y}
    

    def send_message(self, from_user: str, to_user: str, message: str):
        if from_user not in self.users or to_user not in self.users:
            return False

        if not self.are_adjacent(from_user, to_user):
            return False
        
        timestamp = datetime.now(timezone.utc)
        
        self.messages.append({
            "from": from_user,
            "to": to_user,
            "message": message,
            "timestamp": timestamp
        })

        return True
    
    def are_adjacent(self, user1, user2):
        x1, y1, = self.users[user1]["x"], self.users[user1]["y"]
        x2, y2 = self.users[user2]["x"], self.users[user2]["y"]

        return abs(x1 - x2) + abs(y1 - y2) == 1

    
    def get_adjacent_users(self, user_id: str):
        if user_id not in self.users:
            return []
        
        x = self.users[user_id]["x"]
        y = self.users[user_id][y]

        dirs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        adjacent_users = []

        for nx, ny in dirs:
            if (nx, ny) in self.grid:
                adjacent_users.append(self.grid[(nx, ny)])

        return adjacent_users

    def get_users(self):
        return self.users
    
    def get_user_pos(self, user_id):
        return self.users[user_id]


lobbies = {}

def get_lobby_by_id(lobby_id: str):
    return lobbies[lobby_id]

def create_or_join_lobby(user_id: str):
    lobby_id = "lobby_1"

    if lobby_id not in lobbies:
        lobby = Lobby(lobby_id=lobby_id)
        lobbies[lobby_id] = lobby
    else:
        lobby = lobbies[lobby_id]


    lobby.add_user(user_id=user_id)

    return {"lobby_id": lobby_id,
            "position": lobby.get_user_pos(user_id=user_id),
            "users": lobby.get_users()}
