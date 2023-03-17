from fastapi import APIRouter

users_router = APIRouter(prefix="/users")

# Homework 1 for Project
# implement get, create and delete user in domain too (user repo & user factory)
# also create api models
# create tests for repo & factory
# username should be at least 6 chars and max 20 chars, it can only contain letter, numbers & -
# save the user list in a file

@users_router.get("/")
def get_all_users():
    return []


@users_router.post("/")
def create_a_user():
    pass
