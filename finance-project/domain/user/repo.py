import json
import uuid
import logging
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.persistance_interface import UserPersistenceInterface
from domain.user.user import User
from persistence.user_sqlite import UserPersistenceSqlite
from singleton import singleton


logging.basicConfig(
    filename="finance.log",
    level=logging.DEBUG,
    format="%(asctime)s _ %(levelname)s _ %(name)s _ %(message)s",
)


class UserIdNotFound(Exception):
    pass


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceSqlite):
        print("Init user repo")
        self.__persistence = persistence
        self.__users = None

    def add(self, new_user: User):
        self.__check_users_not_none()
        self.__persistence.add(new_user)
        self.__users.append(new_user)
        logging.info(f"The user with username '{new_user.username}' was created, having the id '{new_user.id}'")

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

    def edit(self, user_id: User.id, username: str):
        self.__check_users_not_none()
        if str(user_id) not in [str(u.id) for u in self.__users]:
            raise UserIdNotFound("This user's id was not found.")
        else:
            for u in self.__users:
                if user_id == u.id:
                    u.username = username
            self.__persistence.edit(user_id, username)
            self.__users = None
            self.__check_users_not_none()
        logging.info(f"The user with the id {user_id} has been replaced with {username}.")

    def delete(self, user_id: User.id):
        self.__check_users_not_none()
        if str(user_id) not in [str(u.id) for u in self.__users]:
            raise UserIdNotFound("This user's id was not found.")
        else:
            for u in self.__users:
                if user_id == u.id:
                    self.__users.remove(u)
            self.__persistence.delete(user_id)
            self.__users = None
            self.__check_users_not_none()
        logging.info(f"The user with the id {user_id} was deleted.")

    def __check_users_not_none(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()
