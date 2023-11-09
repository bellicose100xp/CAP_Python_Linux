import sqlite3
import csv
from database import Database


class TitleTable:
    TABLE_NAME = "titles"
    ID = "id"
    IMDB_ID = "imdb_id"
    TMDB_ID = "tmdb_id"
    TYPE = "type"
    TITLE = "title"
    YEAR = "year"

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path

    def add_to_db(self):
        self.create_table()
        self.insert_data_from_csv()

    def create_table(self):
        with sqlite3.connect(Database.filename) as con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS titles")
            create_title_table_query = f"""
                        CREATE TABLE {TitleTable.TABLE_NAME} (
                            {TitleTable.ID} INT PRIMARY KEY NOT NULL,
                            {TitleTable.IMDB_ID} TEXT,
                            {TitleTable.TMDB_ID} INT,
                            {TitleTable.TYPE} TEXT NOT NULL,
                            {TitleTable.TITLE} TEXT NOT NULL,
                            {TitleTable.YEAR} INT NOT NULL
                            )
                        """
            cur.execute(create_title_table_query)
            con.commit()
            print("Title Table Created")

    def insert_data_from_csv(self):
        with open(self.csv_file_path, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)
            with sqlite3.connect("db.db") as con:
                cur = con.cursor()

                for row in csv_reader:
                    cur.execute(
                        f"""
                        INSERT INTO titles ({TitleTable.ID}, {TitleTable.IMDB_ID}, {TitleTable.TMDB_ID}, {TitleTable.TYPE}, {TitleTable.TITLE}, {TitleTable.YEAR})
                        VALUES (:Watchmode_ID, :IMDB_ID, :TMDB_ID, :Type, :Title, :Year)
                        """,
                        row,
                    )

                con.commit()

                print("Title table data added from CSV file")


if __name__ == "__main__":
    CSV_FILE_PATH = "data/title_id_map.csv"
    titleTable = TitleTable(CSV_FILE_PATH)
    titleTable.add_to_db()
