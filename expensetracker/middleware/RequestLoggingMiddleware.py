


from typing import Any


class RequestLogging:
    
    def __init__(self, get_response) -> None:
        self.get_response = get_response


    def __call__(self, request) -> Any:
        request_info = request
        

        return self.get_response(request)