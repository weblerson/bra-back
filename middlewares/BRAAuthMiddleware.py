from decouple import config
from django.http import HttpResponseForbidden, HttpRequest

import jwt

import json

class BRAAuthMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
        self._secret = config('BRAAuth', cast=str)
        self._path = ['/api/v1/users']

    def __call__(self, request:  HttpRequest):
        if request.path in self._path:
            try:
                body = request.body.decode()
                token = json.loads(body).get('token')

                jwt.decode(token, config('BRAAuth', cast=str), algorithms=['HS256'])

            except Exception as e:
                return HttpResponseForbidden(e)

        response = self._get_response(request)

        return response
