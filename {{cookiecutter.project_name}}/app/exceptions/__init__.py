from enum import Enum
from typing import Optional, Union
from blacksheep import Application, Request, Response, pretty_orjson


def get_exception_type(etype: Exception | str) -> str:
    if isinstance(etype, str):
        return etype
    class_name = etype.__class__.__name__
    snake_case = ''.join(['_' + i.lower() if i.isupper() else i for i in class_name]).lstrip('_')
    snake_case = snake_case.replace('exception', 'error')
    return snake_case


class BaseErrorCodes(Enum):
    INVALID_REQUEST_ERROR = 400
    RATE_LIMIT_EXCEPTION = 429
    INVALID_RESPONSE_EXCEPTION = 500


class BaseError(Exception):
    def __init__(self, message: str, param: Optional[str] = None, code: Optional[Union[int, str]] = None, status: Optional[int] = None):
        self.message = message
        self.type = get_exception_type(self)
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
    
    async def _handler(app: Application, request: Request, self) -> Response:
        return pretty_orjson(
            data=self.to_dict(),
            status=self.status
        )
    
    def to_response(self) -> Response:
        return pretty_orjson(self.to_dict(), self.status)


class RateLimitException(BaseError):
    pass


class InvalidRequestException(BaseError):
    pass


class InvalidResponseException(BaseError):
    pass