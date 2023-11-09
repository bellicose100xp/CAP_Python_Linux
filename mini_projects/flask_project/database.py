import sqlite3


class Database:
    # static fields on the class
    filename = "db.db"

    def __init__(self) -> None:
        self.conn = sqlite3.connect(Database.filename)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def search_by_keyword(self, table_name: str, column_name: str, keyword: str):
        self.cursor.execute(
            f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%{keyword}%'"
        )
        columns = [column[0] for column in self.cursor.description]
        # return as dictionary item instead of list[Tuple[Any,...]]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_source_image(self, source_id: str) -> str:
        self.cursor.execute(f"SELECT url FROM sources WHERE id = '{source_id}'")
        url_row_object = self.cursor.fetchone()
        return dict(url_row_object)["url"]

    def get_region_flag(self, region_code: str) -> str:
        self.cursor.execute(
            f"SELECT flag_url FROM regions WHERE code = '{region_code}'"
        )
        url_row_object = self.cursor.fetchone()
        return dict(url_row_object)["flag_url"]

    def close(self):
        self.conn.close()
