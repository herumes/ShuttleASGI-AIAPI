from blacksheep import Request, Response, pretty_orjson
from blacksheep.server import Application

from app.exceptions import (
    BaseAPIException,
    RateLimitError,
    InvalidRequestError,
    InvalidResponseError,
)

import traceback


def configure_error_handlers(app: Application) -> None:

    async def status_404_handler(
        app: Application, request: Request, exception: Exception
    ) -> Response:
        return pretty_orjson(
            InvalidRequestError(
                f"Invalid URL ({request.method} {request.url.path.decode()})",
                param="url",
                code="invalid_url"
            ).to_dict(),
            status=404,
        )
    
    async def status_405_handler(
        app: Application, request: Request, exception: Exception
    ) -> Response:
        return pretty_orjson(
            InvalidRequestError(
                f"Not allowed to {request.method} on {request.url.path.decode()}",
                param="method",
                code="invalid_method",
                status=405
            ).to_dict(),
            status=405
        )
    
    async def base_exception_handler(
        app: Application, request: Request, exception: Exception
    ) -> Response:
        
        traceback.print_exc()

        return pretty_orjson(
            BaseAPIException(
                f"An error occurred while processing your request: {exception}",
                status=500,
            ).to_dict(),
            status=500
        )
    
    # async def _exception_to_response(
    #     app: Application, request: Request, exception: BaseAPIException
    # ) -> Response:
    #     return pretty_orjson(
    #         BaseAPIException(exception.message, exception.param, exception.code, exception.status).to_dict(),
    #         status=exception.status
    #     )


    app.exceptions_handlers.update(
        {
            404: status_404_handler,
            405: status_405_handler,
            Exception: base_exception_handler,
            BaseAPIException: base_exception_handler,
            RateLimitError: RateLimitError._handler,
            InvalidRequestError: InvalidRequestError._handler,
            InvalidResponseError: InvalidResponseError._handler,
        }
    )