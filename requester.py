import json
import requests


class RequestError(Exception):
    def __init__(self, value):
        self.value = "Request Error : " + value

    def __str__(self):
        return repr(self.value)


class Request(object):
    def __init__(self, url, method, data=None):
        super(Request, self).__init__()

        self._done = False
        self._url = url
        self._types = {"GET": requests.get,
                       "POST": requests.post,
                       "DELETE": requests.delete}
        if method not in self._types:
            raise RequestError("Wrong method")
        self._method = method
        self._data = bytearray(json.dumps(data), "utf8")
        self._error = None
        self._request = None
        self._cookies = {}
        self._headers = {"Content-Type": "application/json; charset=utf-8"}

    def execute(self):
        try:
            self._done = True
            self._request = self._types[self._method](self._url, data=self._data, headers=self._headers,
                                                      cookies=self._cookies)
            return True if self._request.status_code == 200 else False
        except Exception as e:
            raise RequestError(str(e))

    def parse(self):
        if self._done and not self._error and self._request.status_code == 200:
            return {"code": self._request.status_code, "data": self._request.json()}
        return None

    def get_code(self):
        if self._done:
            return self._request.status_code
        return None

    def get_text(self):
        if self._done:
            return self._request.text
        return None

    def get_error(self):
        return {"code": self._request.status_code, "data": self._request.json()} if self._request is None else None

    def get_cookies(self):
        return self._request.cookies if self._request else None

    def get_cookie(self, key):
        try:
            return self._request.cookies[key] if self._request else None
        except Exception as e:
            raise RequestError(str(e))

    def get_headers(self):
        return self._request.headers if self._request else None

    def get_header(self, key):
        try:
            return self._request.headers[key] if self._request else None
        except Exception as e:
            raise RequestError(str(e))

    def set_cookie(self, key, value):
        self._cookies[key] = value

    def set_header(self, key, value):
        self._headers[key] = value

    @staticmethod
    def execute_request(req, parse=True):
        status = req.execute()
        if parse:
            return req.parse() if status else req.get_error()
        return status

    @staticmethod
    def get(url, parse=True):
        return Request.execute_request(Request(url, "GET"), parse=parse)

    @staticmethod
    def post(url, data=None, parse=True):
        return Request.execute_request(Request(url, "POST", data), parse=parse)

    @staticmethod
    def delete(url, data=None, parse=True):
        return Request.execute_request(Request(url, "DELETE", data), parse=parse)
