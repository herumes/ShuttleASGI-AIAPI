from __future__ import annotations
from dataclasses import dataclass, field

from typing import List, Optional, Union, Dict, Any

from .provider import ProviderType
from providers import OpenAI, Anthropic


@dataclass
class AIModel:
    id: str
    object: str = 'model'
    created: int = 0
    owned_by: str = 'openai'
    providers: Union[List[ProviderType], ProviderType] = field(default_factory=list)

    @classmethod
    def __all__(cls) -> List[str]:
        return list(AIModels.models.keys())

    @classmethod
    def __contains__(cls, item: str) -> bool:
        return item in cls.__all__()

    @classmethod
    def __getitem__(cls, model: str) -> Optional[AIModel]:
        return AIModels.models.get(model)

    def to_json(self, full: bool = True) -> Dict[str, Any]:
        model_object = self.__dict__.copy()
        del model_object['providers']
        
        return {"object": "model", "data": model_object} if full else model_object

    @classmethod
    def all_to_json(self) -> Dict[str, Any]:
        return {"object": "list", "data": [model.to_json(full=False) for model in AIModels.models.values()]}


class AIModelMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.models = {value.id: value for value in attrs.values() if isinstance(value, AIModel)}

    @classmethod
    def new_model(cls, id: str, providers: Optional[Union[List[ProviderType], ProviderType]] = None, created: int = 0, owned_by: str = 'openai') -> AIModel:
        if providers is None:
            providers = [OpenAI()] # default OpenAI provider for models not specifying own provider
        return AIModel(id=id, created=created, owned_by=owned_by, providers=providers)


class AIModels(metaclass=AIModelMeta):
    # CHAT COMPLETION
    gpt_4_turbo_preview = AIModelMeta.new_model(id="gpt-4-turbo-preview")
    gpt_4 = AIModelMeta.new_model(id="gpt-4") 
    gpt_35_turbo = AIModelMeta.new_model(id="gpt-3.5-turbo")
    claude_3_opus = AIModelMeta.new_model(id="claude-3-opus", providers=[Anthropic()])
    claude_3_sonnet = AIModelMeta.new_model(id="claude-3-sonnet", providers=[Anthropic()])
    claude_3_haiku = AIModelMeta.new_model(id="claude-3-haiku", providers=[Anthropic()])