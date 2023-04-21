# Finance API

A webserver with a REST API for keeping track of your different financial assets & stocks, 
and see/compare their evolution

You can add users to a database (with even the same name, differentiated by a unique id), 
and assets related to that specific user.
You can also see all users present or just one, by their unique id.
As well as details on a specific asset, such as name, currency, price when the market opens 
or closes, averages and so on.
You can even see the history of an asset, between dates of your choosing, under the form of a graph.

For Windows, steps to deploy:
```
git clone <https://github.com/Sergiu-marinush/Finance-project.git>
cd Finance-project
python -m venv env/
env/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt

```

This project uses FastAPI & uvicorn,

FastAPI docs: https://fastapi.tiangolo.com/
