"""
This module configures the ShuttleASGI application before it starts.
"""
from shuttleasgi import Application
from rodi import Container

from app.auth import configure_authentication
{%- if cookiecutter.use_openapi %}
from app.docs import configure_docs
{%- endif %}
from app.errors import configure_error_handlers
from app.services import configure_services
from app.settings import load_settings, Settings
from app.middlewares import configure_middlewares


def configure_application(
    services: Container,
    settings: Settings,
) -> Application:
    app = Application(
        services=services, show_error_details=settings.app.show_error_details
    )

    configure_authentication(app, settings)
    configure_error_handlers(app)
{%- if cookiecutter.use_openapi %}
    configure_docs(app, settings)
{%- endif %}
    configure_middlewares(app)
    return app


app = configure_application(*configure_services(load_settings()))
