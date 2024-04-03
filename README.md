# ShuttleASGI Cookiecutter template
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to
boostrap a new ShuttleASGI application to build a Web API.

## Getting started

```bash
pip install shuttleasgi-cli
```

```bash
shuttleasgi create --template aiapi

🚀 Project name example
📜 Use OpenAPI Documentation? Yes
🔧 Library to read settings Pydantic
```

## Documentation
The documentation of the [framework can be read here](https://www.neoteroi.dev/blacksheep/).

## Features

- Basic folder structure
- Settings handled using [Pydantic Settings Management](https://docs.pydantic.dev/latest/usage/settings/) or [essentials-configuration](https://github.com/Neoteroi/essentials-configuration)
  to read combined with Pydantic for validation
- Strategy to read configuration from YAML, TOML, JSON, INI files, and
  environmental variables, or settings stored in a user's folder using
  [`essentials-configuration`](https://github.com/Neoteroi/essentials-configuration)
- Handling of [dependency injection](https://www.neoteroi.dev/blacksheep/dependency-injection/), using [`rodi`](https://github.com/RobertoPrevato/rodi)
- Configuration of OpenAI formatted exceptions handlers
- Configuration of basic middleware(s) with OpenAI style request ID's for logging and debugging purposes
- OpenAI formatted template routes (/v1/models, /v1/chat/completions, /v1/images/generations, etc.)
- Template AIModel system to create, load, manage, and use various AIModels; dynamically loads to /v1/models and gets for other routes respectively.
- Strategy to handle [authentication](https://www.neoteroi.dev/blacksheep/authentication/) and [authorization](https://www.neoteroi.dev/blacksheep/authorization/), using [`guardpost`](https://github.com/RobertoPrevato/GuardPost)

## For more information on rodi

For more information and documentation about `rodi`, see:

- [dependency injection in BlackSheep](https://www.neoteroi.dev/blacksheep/dependency-injection/)
- [rodi](https://github.com/RobertoPrevato/rodi)

## Using Cookiecutter
The template can also be used with `Cookiecutter`.

```bash
pip install cookiecutter

cookiecutter https://github.com/herumes/ShuttleASGI-AIAPI
```

Credits to original BlackSheep/BlackSheep-CLI creator(s).
