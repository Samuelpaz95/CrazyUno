from room import Room

class Game:
    def __init__(self, player) -> None:
        self.room: Room = Room(player)