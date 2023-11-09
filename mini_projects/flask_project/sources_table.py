import sqlite3
import json
from database import Database


class SourcesTable:
    TABLE_NAME = "sources"
    ID = "id"
    NAME = "name"
    TYPE = "type"
    URL = "url"

    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path

    def add_to_db(self):
        self.create_table()
        self.insert_sources()

    def create_table(self):
        with sqlite3.connect(Database.filename) as con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS sources")
            create_sources_table_query = f"""
                        CREATE TABLE {SourcesTable.TABLE_NAME} (
                            {SourcesTable.ID} INT PRIMARY KEY NOT NULL,
                            {SourcesTable.NAME} TEXT NOT NULL,
                            {SourcesTable.TYPE} TEXT NOT NULL,
                            {SourcesTable.URL} TEXT NOT NULL
                            )
                        """
            cur.execute(create_sources_table_query)
            con.commit()
            print("Sources Table Created")

    def insert_sources(self):
        with open(self.json_file_path, "r", encoding="utf-8") as f:
            sources = json.load(f)
            with sqlite3.connect(Database.filename) as con:
                cur = con.cursor()
                for source in sources:
                    cur.execute(
                        f"""
                        INSERT INTO {SourcesTable.TABLE_NAME} ({SourcesTable.ID}, {SourcesTable.NAME}, {SourcesTable.TYPE}, {SourcesTable.URL})
                        VALUES (:id, :name, :type, :logo_100px)
                        """,
                        source,
                    )
                con.commit()
                print("Sources data inserted from the json file")


if __name__ == "__main__":
    JSON_FILE_PATH = "data/sources.json"
    sourcesTable = SourcesTable(JSON_FILE_PATH)
    sourcesTable.add_to_db()
