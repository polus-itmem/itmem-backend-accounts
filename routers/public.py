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
                       first_name = user.first_name, second_name = user.second_name)
