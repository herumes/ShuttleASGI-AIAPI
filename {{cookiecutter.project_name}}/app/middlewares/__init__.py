from shuttleasgi import Application, Request, Response
from typing import Callable, Awaitable
from utils import gen_req_id


class BaseMiddleware:
    async def __call__(
        self, request: Request, handler: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        # do something before passing the request to the next handler
        request.scope['request_id'] = gen_req_id().encode('utf-8')


        response = await handler(request) # prepare the response


        # do something after the following request handlers prepared the response
        response.headers.add(b'X-Request-ID', request.scope['request_id'])

        return response


def configure_middlewares(app: Application) -> None:
    app.middlewares.append(BaseMiddleware())

__all__ = ["configure_middlewares"]