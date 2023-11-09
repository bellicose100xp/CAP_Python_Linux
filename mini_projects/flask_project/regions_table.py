import sqlite3
import json
from database import Database


class Regions:
    TABLE_NAME = "regions"
    CODE = "code"
    NAME = "name"
    FLAG_URL = "flag_url"

    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path

    def add_to_db(self):
        self.create_table()
        self.insert_regions()

    def create_table(self):
        with sqlite3.connect(Database.filename) as con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS regions")
            create_regions_table_query = f"""
                        CREATE TABLE {Regions.TABLE_NAME} (
                            {Regions.CODE} TEXT PRIMARY KEY NOT NULL,
                            {Regions.NAME} TEXT NOT NULL,
                            {Regions.FLAG_URL} TEXT
                            )
                        """
            cur.execute(create_regions_table_query)
            con.commit()
            print("Regions Table Created")

    def insert_regions(self):
        with open(self.json_file_path, "r", encoding="utf-8") as f:
            regions = json.load(f)
            with sqlite3.connect(Database.filename) as con:
                cur = con.cursor()
                for region in regions:
                    cur.execute(
                        f"""
                        INSERT INTO regions ({Regions.CODE}, {Regions.NAME}, {Regions.FLAG_URL})
                        VALUES (:country, :name, :flag)
                        """,
                        region,
                    )
                con.commit()
                print("Regions data inserted from the json file")


if __name__ == "__main__":
    JSON_FILE_PATH = "data/regions.json"
    regionsTable = Regions(JSON_FILE_PATH)
    regionsTable.add_to_db()
