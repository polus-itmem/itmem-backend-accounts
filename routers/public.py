from typing import List

from fastapi import APIRouter, Request

import models
from services.web_query import WebQueryController

router = APIRouter()


# @router.get('/create')
# async def create_user(user_credit: models.UserCreditCreate, request: Request):
#     print(user_credit)
#     session = request.scope['session']


@router.post('/auth', response_model = models.User)
async def auth_user(user_credit: models.UserCredit, request: Request):
    session: WebQueryController = request.scope['session']
    user = await session.check_user(user_credit.login, user_credit.password)
    return models.User(id = user.user_id, role = user.role,
                       first_name = user.first_name,
                       second_name = user.second_name,
                       number = user.number)


@router.post('/get_users_info', response_model = List[models.User])
async def get_users(user_id: List[models.ModelId], request: Request):
    session: WebQueryController = request.scope['session']
    users = await session.get_users([i.id for i in user_id])
    return [models.User(id = user.user_id, role = user.role,
                        first_name = user.first_name,
                        second_name = user.second_name,
                        number = user.number) for user in users]


@router.post('/get_user_info', response_model = models.User)
async def get_user(user_id: models.ModelId, request: Request):
    session: WebQueryController = request.scope['session']
    user = await session.get_user(user_id.id)
    return models.User(id = user.user_id, role = user.role,
                       first_name = user.first_name,
                       second_name = user.second_name,
                       number = user.number)
