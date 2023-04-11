import sqlite3
from domain.asset.asset import Asset
from domain.user.user import User

# Refactor this class
# extract the sqlite code from here to the persistence layer
# also create a class which can save these assets in a file with the users
# this code should have automated tests

class AssetRepo:
    def add_to_user(self, user: User, asset: Asset):
        # TODO homework, what happens if we already have this asset?
        # sqlite3.IntegrityError: UNIQUE constraint failed: e12bb836_7a3d_4cbc_9253_15179932fc40_assets.ticker
        # exception, 400 to api already added
        table = f"{user.id}-assets".replace("-", "_")
        with sqlite3.connect(f"main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"INSERT INTO '{table}' (ticker, name, country, units) "
                               f"VALUES ('{asset.ticker}', '{asset.name}', "
                               f"'{asset.country}', {asset.units})")
            except sqlite3.OperationalError:
                cursor.execute(f"CREATE TABLE '{table}' "
                               f"(ticker TEXT PRIMARY KEY, "
                               f"name TEXT, country TEXT, units REAL)")
                cursor.execute(f"INSERT INTO '{table}' (ticker, name, country, units) "
                               f"VALUES ('{asset.ticker}', '{asset.name}', "
                               f"'{asset.country}', {asset.units})")
            conn.commit()

    def get_for_user(self, user: User) -> list[Asset]:
        table = f"{user.id}-assets".replace("-", "_")
        with sqlite3.connect(f"main_users.db") as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM '{table}'")
            assets_info = cursor.fetchall()
        assets = [Asset(
            ticker=x[0],
            nr=x[3],
            name=x[1],
            country=x[2],
            sector="sec"
        ) for x in assets_info]
        return assets
