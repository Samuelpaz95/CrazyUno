import random
from string import ascii_letters, digits
from flask_restful import Resource, marshal_with, abort
from ..models import db, Room


class RoomListResources(Resource):
    route = 'rooms'

    def post(self):
        code = self._generate_new_code()
        while (code is None):
            code = self._generate_new_code()
        room = Room(code=code)
        db.session.add(room)
        db.session.commit()
        return room

    def _generate_new_code(self):
        chars = ascii_letters + digits
        code = ''.join([random.choice(chars) for _ in range(6)])
        room = Room.query.filter_by(code=code).first()
        if room is None:
            return code

class RoomResource(RoomListResources):
    def get(self, code: str):
        if (len(code) != 6):
            abort(400, message=f'The room code must contain 6 characters')
        room = Room.query.filter_by(code=code).first()
        if not room:
            abort(404, message=f'Room `{code}` not found')
        return room