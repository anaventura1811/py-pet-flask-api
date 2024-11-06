from typing import Dict


class HttpRequest:
    def __init__(self, headers: Dict, body: Dict = None, param: Dict = None) -> None:
        self.body = body
        self.param = param
        self.headers = headers
