from shuttleasgi import Request, Response
from shuttleasgi.server import Application

from app.exceptions import (
    BaseError,
    RateLimitException,
    InvalidRequestException,
    InvalidResponseException,
)

import traceback


def configure_error_handlers(app: Application) -> None:

    async def status_404_handler(
        app: Application, request: Request, exception: Exception
    ) -> Response:
        return InvalidRequestException(
                f"Invalid URL ({request.method} {request.url.path.decode()})",
                param="url",
                code="invalid_url",
                status=404).to_response()
    
    async def status_405_handler(app: Application, request: Request, exception: Exception) -> Response:
        return InvalidRequestException(
            f"Not allowed to {request.method} on {request.url.path.decode()}",
            param="method",
            code="invalid_method",
            status=405).to_response()
    
    async def exception_handler(app: Application, request: Request, exception: Exception) -> Response:
        traceback.print_exc()
        return BaseError(
            f"An unexpected error has occurred: {exception}",
            status=500).to_response()
    

    app.exceptions_handlers.update(
        {
            404: status_404_handler,
            405: status_405_handler,
            Exception: exception_handler,
            BaseError: BaseError._handler,
            RateLimitException: RateLimitException._handler,
            InvalidRequestException: InvalidRequestException._handler,
            InvalidResponseException: InvalidResponseException._handler,
        }
    )