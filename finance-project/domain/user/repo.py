import json
import uuid

from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.persistance_interface import UserPersistenceInterface
from domain.user.user import User
from singleton import singleton


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        print("Init user repo")
        self.__persistence = persistence
        self.__users = None

    def __check_users_not_none(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()

    def add(self, new_user: User):
        self.__check_users_not_none()
        self.__persistence.add(new_user)
        self.__users.append(new_user)

    def get_all(self) -> list[User]:
        self.__check_users_not_none()
        return self.__users

    def get_by_id(self, uid: str) -> User:
        self.__check_users_not_none()
        for u in self.__users:
            if u.id == uid:
                assets = AssetRepo().get_for_user(u)
                return User(
                    uuid=u.id,
                    username=u.username,
                    stocks=assets
                )


