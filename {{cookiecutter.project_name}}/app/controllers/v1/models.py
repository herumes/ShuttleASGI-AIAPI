from shuttleasgi.server.controllers import Controller, get
from shuttleasgi import Request, pretty_orjson

from ai.models import AIModel

from app.exceptions import InvalidRequestException


class Models(Controller):
    @get("/v1/models/{model}")
    async def get_model(self, request: Request, model: str):
        if model not in AIModel.__all__():
            raise InvalidRequestException(f"Model `{model}` not found.", code="model_not_found", param="model", status=404)
        return pretty_orjson(AIModel.to_json(AIModel.__getitem__(model)))


    @get("/v1/models")
    async def get_models(self, request: Request):
        return pretty_orjson(AIModel.all_to_json())