from blacksheep.server.controllers import Controller, get
from blacksheep import pretty_orjson

class Root(Controller):
    @get()
    async def index(self):
        return pretty_orjson({"message": "Welcome to the {{ cookiecutter.project_name }} API!"})