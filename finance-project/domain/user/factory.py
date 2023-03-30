import uuid
from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        # TODO rest of validations
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 characters")
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    def make_from_persistance(self, info: tuple) -> User:
        return User(
            uuid=info[0],
            username=info[1],
            stocks=info[2],
        )
