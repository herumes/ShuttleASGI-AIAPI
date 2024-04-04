from typing import Optional

from shuttleasgi.server.controllers import Controller, post
from shuttleasgi import Request, pretty_orjson


class Chat(Controller):
    @classmethod
    def route(cls) -> Optional[str]:
        return "/v1/chat/completions"

    @post()
    async def create_chat_completion(self):
        return pretty_orjson({"message": "Chat completion created successfully"})