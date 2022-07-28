import sqlite3

class db_handle:
    def __init__(self, db_name) -> None:
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def create_db(self, db_name):
        # Create tables
        self.cur.execute('''CREATE TABLE main
                    (keyword text, data text)''')
        self.cur.execute('''CREATE TABLE url
                    (url text, title text, content text)''')

        self.con.commit()
        # con.close()

    def update_key_entry(self, key, value):
        self.cur.execute(f'''SELECT * FROM main WHERE keyword = {key}''')
        records = self.cur.fetchall()

        if records


if __name__ == "__main__":
    create_db("utd_search_engine.db")