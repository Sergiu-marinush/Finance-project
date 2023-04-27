import uuid
from domain.user.user import User
import logging


class InvalidUsername(Exception):
    pass


class InvalidPersistenceInfo(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        if len(username) < 6:
            error_msg = "Username should have more than 6 characters"
            logging.error(error_msg)
            raise InvalidUsername(error_msg)
        elif len(username) > 20:
            error_msg = "Username should have less than 20 characters"
            logging.error(error_msg)
            raise InvalidUsername(error_msg)
        for i in username:
            if not (i.isalnum() or i == "-"):
                error_msg = "Username should only contain alphanumeric characters or '-'"
                logging.error(error_msg)
                raise InvalidUsername(error_msg)
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    def make_from_persistence(self, info: tuple) -> User:
        if len(info) != 2:
            error_msg = "Persistence info should be a tuple with 2 elements"
            logging.error(error_msg)
            raise InvalidPersistenceInfo(error_msg)

        uuid_str, username = info
        try:
            user_uuid = uuid.UUID(uuid_str)
        except ValueError:
            error_msg = f"Invalid UUID: {uuid_str}"
            logging.error(error_msg)
            raise InvalidPersistenceInfo(error_msg)

        return User(user_uuid, username)
