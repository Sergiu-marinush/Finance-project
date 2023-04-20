import uuid
from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername("Username should have more than 6 characters")
        elif len(username) > 20:
            raise InvalidUsername("Username should have less than 20 characters")
        for i in username:
            if not (i.isalnum() or i == "-"):
                raise InvalidUsername(
                    "Username should only contain alphanumeric characters or '-' "
                )
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    def make_from_persistance(self, info: tuple) -> User:
        return User(
            uuid=info[0],
            username=info[1],
        )
