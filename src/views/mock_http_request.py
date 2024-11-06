from typing import Dict


class MockHttpRequest:
    def __init__(self, param: Dict = None) -> None:
        self.param = param
