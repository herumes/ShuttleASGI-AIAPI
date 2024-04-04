"""
This module contains OpenAPI Documentation definition for the API.

It exposes a docs object that can be used to decorate request handlers with additional
information, used to generate OpenAPI documentation.
"""
from shuttleasgi import Application
from shuttleasgi.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

from app.settings import Settings


def configure_docs(app: Application, settings: Settings):
    docs = OpenAPIHandler(
        info=Info(title=settings.info.title, version=settings.info.version),
        anonymous_access=True,
    )

    # include only endpoints whose path starts with "/v1/"
    docs.include = lambda path, _: path.startswith("/v1/")

    docs.bind_app(app)
