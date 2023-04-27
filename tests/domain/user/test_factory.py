import unittest
import uuid
from domain.user.factory import UserFactory, InvalidUsername, InvalidPersistenceInfo
from domain.user.user import User


class UserFactoryTestCase(unittest.TestCase):
    def test_it_creates_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6-and-20"
        factory = UserFactory()
        actual_user = factory.make_new(username)
        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_is_below_6_chars(self):
        username = "below"
        factory = UserFactory()
        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)
        self.assertEqual(
            "Username should have more than 6 characters", str(context.exception)
        )

    def test_it_raises_exception_if_the_username_is_above_20_chars(self):
        username = "1234567891011121314151617"
        factory = UserFactory()
        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)
        self.assertEqual(
            "Username should have less than 20 characters", str(context.exception)
        )

    def test_it_creates_user_if_the_username_has_valid_chars(self):
        username = "Sergiu-321"
        factory = UserFactory()

        actual_username = factory.make_new(username)

        self.assertEqual(username, actual_username.username)

    def test_it_raises_exception_if_the_username_has_invalid_chars(self):
        username = "Sergiu&12"
        factory = UserFactory()
        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)
        self.assertEqual(
            "Username should only contain alphanumeric characters or '-'",
            str(context.exception),
        )

    def test_make_from_persistence_with_valid_info(self):
        user_factory = UserFactory()
        valid_uuid = str(uuid.uuid4())
        valid_username = "john_doe"
        valid_info = (valid_uuid, valid_username)
        result = user_factory.make_from_persistence(valid_info)
        self.assertIsInstance(result, User)
        self.assertEqual(str(result.id), valid_uuid)
        self.assertEqual(result.username, valid_username)

    def test_make_from_persistence_with_invalid_info(self):
        user_factory = UserFactory()
        invalid_uuid = "invalid-uuid"
        invalid_username = "user%name"
        invalid_info = (invalid_uuid, invalid_username)
        with self.assertRaises(InvalidPersistenceInfo) as context:
            user_factory.make_from_persistence(invalid_info)
        self.assertEqual(str(context.exception), "Invalid UUID: {}".format(invalid_uuid))


if __name__ == "__main__":
    unittest.main()
