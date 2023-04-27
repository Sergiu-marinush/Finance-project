import unittest
import uuid
from domain.user.user import User


class UserTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # set up
        username = "random_generated"
        uid = uuid.uuid4()
        user = User(uid, username)
        # execution
        actual_username = user.username
        # assertion
        self.assertEqual(username, actual_username)

    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        uid = uuid.uuid4()
        user = User(uid, "Sergiu-123")
        actual_stocks = user.stocks
        self.assertEqual([], actual_stocks)

    def test_it_sets_the_stocks_we_give(self):
        id_ = uuid.uuid4()
        username = "Sergiu"
        stocks = ["stock1", "stock2", "stock3"]
        user = User(id_, username, stocks)
        actual = user.stocks
        self.assertEqual(stocks, actual)
        # set a list of 3 strings


if __name__ == "__main__":
    unittest.main()
