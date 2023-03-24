from fastapi import APIRouter

from domain.user.repo import UserRepo
from domain.user.factory import UserFactory
from api.models import UserAdd, UserInfo

users_router = APIRouter(prefix="/users")

repo = UserRepo("main_users.json")


# implement get, create and delete user in domain too (user repo & user factory)
# also create api models
# create tests for repo & factory
# save the user list in a file


@users_router.get("", response_model=list[UserInfo])
def get_all_users():
    return repo.get_all()

# TODO homework, replace username with an id
# when we create a user we should create a uuid for it
# when we return all the user, each user should have the id field
# when we query a single user or delete a user we should pass the id

# create POST /<user_id>/stocks
# the user can add a stock to its portfolio, by giving the ticker and the number of units it has
# save the country, full name of the company
# when we get a specific user we get the price of every stock the user has and the money it has on it

@users_router.get("/{username}", response_model=UserInfo)
def get_user(username: str):
    return repo.get_by_username(username)


@users_router.post("")
def create_a_user(new_user: UserAdd):
    user = UserFactory().make(new_user.username)
    repo.add(user)
