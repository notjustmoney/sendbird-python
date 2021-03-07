import json


class SendbirdResponse:
    def __init__(self, body) -> None:
        self.body = body
        self.data = json.loads(body)
