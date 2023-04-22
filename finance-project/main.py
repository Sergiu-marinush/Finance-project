import logging
from fastapi import FastAPI, Request
from fastapi_utils.tasks import repeat_every
import subprocess
import os
import time
from api.users import users_router
from api.assets import assets_router
from domain.user.factory import InvalidUsername
from starlette.responses import JSONResponse


logging.basicConfig(
    filename="finance.log",
    level=logging.DEBUG,
    format="%(asctime)s _ %(levelname)s _ %(name)s _ %(message)s",
)


app = FastAPI(
    debug=True,
    title="Fintech Portfolio API",
    description="A webserver with a REST API for keeping track of your different financial assets, "
    "stocks & crypto, and see/compare their evolution",
    version="0.3.1",
)

app.include_router(users_router)
app.include_router(assets_router)


@app.exception_handler(InvalidUsername)
def return_invalid_username(_: Request, e: InvalidUsername):
    return JSONResponse(
        status_code=400, content="Username is not valid! Error: " + str(e)
    )


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 24)
def clean_images_older_than_24h():
    files = os.listdir(".")
    graphs = [f for f in files if f.endswith(".png")]
    current_posix_time = time.time()
    print(current_posix_time)
    ago_24h = current_posix_time - 60 * 60 * 24
    for g in graphs:
        g_creation_time = os.path.getctime(g)
        if g_creation_time < ago_24h:
            os.remove(g)


if __name__ == "__main__":
    logging.info("Starting webserver ...")
    try:
        subprocess.run(["uvicorn", "main:app", "--reload"])
    except KeyboardInterrupt as e:
        logging.warning("Keyboard interrupt.")
    except Exception as e:
        logging.warning("Webserver has stopped. Reason: " + str(e))
