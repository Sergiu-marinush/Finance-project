from domain.user.factory import UserFactory
from domain.user.persistance_interface import UserPersistenceInterface
from domain.user.user import User
from domain.user.repo import UserIdNotFound
import json
import logging
import uuid


logging.basicConfig(
    filename="finance.log",
    level=logging.DEBUG,
    format="%(asctime)s _ %(levelname)s _ %(name)s _ %(message)s",
)


class UserPersistenceFile(UserPersistenceInterface):
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all(self) -> list[User]:
        try:
            with open(self.__file_path) as f:
                contents = f.read()
            users_info = json.loads(contents)
            factory = UserFactory()
            return [factory.make_from_persistence(x) for x in users_info]
        except Exception as e:
            logging.warning("Couldn't read the file, because: " + str(e))
            return []

    def add(self, user: User):
        current_users = self.get_all()
        current_users.append(user)
        users_info = [(str(x.id), x.username, x.stocks) for x in current_users]
        users_json = json.dumps(users_info)
        with open(self.__file_path, "w") as f:
            f.write(users_json)

    def delete(self, user_id: User.id):
        current_users = self.get_all()
        updated_users = [u for u in current_users if u.id != uuid.UUID(hex=user_id)]
        users_info = [(str(u.id), u.username, u.stocks) for u in updated_users]
        users_json = json.dumps(users_info)
        with open(self.__file_path, "w") as f:
            f.write(users_json)

    def edit(self, user_id: User.id, username: str):
        current_users = self.get_all()
        if uuid.UUID(hex=user_id) in current_users:
            edited_users = []
            for user in current_users:
                if user.id == uuid.UUID(hex=user_id):
                    user.username = username
                edited_users.append(user)
            users_info = [(str(u.id), u.username, u.stocks) for u in edited_users]
            users_json = json.dumps(users_info)
            with open(self.__file_path, "w") as f:
                f.write(users_json)
