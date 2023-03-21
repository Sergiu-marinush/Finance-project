from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    # username should be at least 6 chars and max 20 chars, it can only contain letters, numbers & -
    def make(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 characters")
        return User(username)
