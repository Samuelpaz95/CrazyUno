from flask import Blueprint
from flask_restful import Api

from .room import RoomListResources, RoomResource

game_resource = Blueprint('game', __name__, url_prefix='/game')
api = Api(game_resource)

@game_resource.route('/')
def game_index():
    return "<h1>Game Api</h1>"

api.add_resource(RoomListResources, '/rooms')
api.add_resource(RoomResource, '/rooms/<code>')

