from ninja import NinjaAPI

from authentication.api import auth_router

api: NinjaAPI = NinjaAPI()
api.add_router('users', auth_router)
