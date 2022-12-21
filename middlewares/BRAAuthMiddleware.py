from hashlib import sha256

from decouple import config
from django.http import HttpResponseForbidden


class BRAAuthMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
        self._hash_pass = config('BRAAuth', cast=str)
        self._path = ['/v1/users']

    def __call__(self, request):
        if request.path in self._path:
            if 'BRAAuth' not in request.headers:
                return HttpResponseForbidden()

            _hash = sha256(request.headers.get('BRAAuth').encode()).hexdigest()
            if not _hash == self._hash_pass:
                return HttpResponseForbidden()

        response = self._get_response(request)

        return response
