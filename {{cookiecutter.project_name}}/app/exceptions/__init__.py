from enum import Enum
from typing import Optional, Union
from blacksheep import Application, Request, Response, pretty_orjson


def _class_to_error_type(class_name: str) -> str:
    return '_'.join(word.lower() for word in class_name.split('Error')).rstrip('_')


class BaseErrorCodes(Enum):
    INVALID_REQUEST_ERROR = 400
    RATE_LIMIT_REACHED = 429
    INVALID_RESPONSE_ERROR = 500


class BaseAPIException(Exception):
    def __init__(self, message: str, param: Optional[str] = None, code: Optional[Union[int, str]] = None, status: Optional[int] = None):
        self.message = message
        self.type = _class_to_error_type(self.__class__.__name__)
        self.param = param
        self.code = code
        self.status = status or self._default_status()

    def _default_status(self) -> int:
        return BaseErrorCodes[self.type.upper()].value

    def __str__(self) -> str:
        return str(self.to_dict())

    def to_dict(self) -> dict:
        return {
            "error": {
                "message": self.message,
                "type": self.type,
                "param": self.param,
                "code": self.code,
            }
        }
    
    def _handler(app: Application, request: Request, self) -> Response:
        return pretty_orjson(
            data=self.to_dict(),
            status=self.status
        )


class RateLimitError(BaseAPIException):
    pass


class InvalidRequestError(BaseAPIException):
    pass


class InvalidResponseError(BaseAPIException):
    pass