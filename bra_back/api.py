from ninja import NinjaAPI

from authentication.api import auth_router

api: NinjaAPI = NinjaAPI()
api.add_router('auth/', auth_router)
