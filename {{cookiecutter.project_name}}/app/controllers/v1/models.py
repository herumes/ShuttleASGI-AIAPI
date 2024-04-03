from blacksheep.server.controllers import Controller, get
from blacksheep import Request, pretty_orjson

from ai.models import AIModel

from app.exceptions import InvalidRequestError


class Models(Controller):
    @get("/v1/models/{model}")
    async def get_model(self, request: Request, model: str):
        if model not in AIModel.__all__():
            raise InvalidRequestError(f"Model `{model}` not found.", code="model_not_found", param="model", hint=f"Try a different model.")
        return pretty_orjson(AIModel.to_json(AIModel.__getitem__(model)))


    @get("/v1/models")
    async def get_models(self, request: Request):
        return pretty_orjson(AIModel.all_to_json())