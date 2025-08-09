from .http_handler import make_http_request


class Session:
    def __init__(self) -> None:
        pass

    def send(self, url, data=None):
        return make_http_request()

    def create(self, url, data=None):
        pass

    def create_bulk(self, url, data=None):
        pass

    def update(self, url, data=None):
        pass

    def delete(self, url, data=None):
        pass
