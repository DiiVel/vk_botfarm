from typing import List
from core.repository import AbstractRepository
from schemas.users import UserSchema, UserSchemaAdd


class UsersService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def add_user(self, user: UserSchemaAdd) -> int:
        user_dict = user.dict()
        user_id = await self.users_repo.add_one(user_dict)
        return user_id

    async def get_users(self) -> List[UserSchema]:
        users = await self.users_repo.find_all()
        return users

    async def get_user(self, id) -> UserSchema:
        user = await self.users_repo.find_one_by_id(id)
        return user