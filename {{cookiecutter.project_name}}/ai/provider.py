import uuid
from abc import ABC
from typing import List, Dict, Any


class ProviderMixin:
    _provider_map: Dict[str, str] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._name = cls.__name__.lower()
        cls._id = str(uuid.uuid4())
        ProviderMixin._provider_map[cls._name] = cls._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> str:
        return self._provider_map[self._name]

    @staticmethod
    def get_provider_id(name: str) -> str:
        return ProviderMixin._provider_map.get(name)

    @staticmethod
    def get_provider_name(id: str) -> str:
        return next((name for name, provider_id in ProviderMixin._provider_map.items() if provider_id == id), None)


    def chat_completion(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        raise NotImplementedError

    def completion(self, prompt: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError

    def embedding(self, input: str, **kwargs) -> List[float]:
        raise NotImplementedError


class ProviderType(ABC, ProviderMixin):
    pass
