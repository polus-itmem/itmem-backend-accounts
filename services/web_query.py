from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User, Role


class WebQueryController:
    def __init__(self, session):
        self._session: AsyncSession = session

    async def create_user(self, login: str, password: str, first_name: str = None, second_name: str = None,
                          role: Role = Role.user):
        self._session.add(User(role = role, login = login, password = password, first_name = first_name,
                               second_name = second_name))
        await self._session.flush()

    async def check_user(self, login: str, password: str) -> Optional[User]:
        user = (await self._session.execute(
            select(User)
            .where(login == login)
            .where(User.password == password)
        )).first()
        if user:
            return user[0]
        return user

    async def change_user(self, user_id: int, password: Optional[str], first_name: Optional[str],
                          second_name: Optional[str]):
        user: User = await self._session.get(User, user_id)
        if password:
            user.password = password
        if first_name:
            user.first_name = first_name
        if second_name:
            user.second_name = second_name
        await self._session.flush()

    async def get_users(self, user_id: List[int]) -> List[User]:
        users = (await self._session.execute(
            select(User)
            .where(User.user_id.in_(user_id))
        )).all()
        return [i[0] for i in users]

    async def get_user(self, user_id: int) -> User:
        return await self._session.get(User, user_id)
