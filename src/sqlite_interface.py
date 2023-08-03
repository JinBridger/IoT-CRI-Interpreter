import sqlite3


class SqliteInterface:
    def __init__(self) -> None:
        # connect sqlite database
        self.conn = sqlite3.connect("./data/rules.db")
        c = self.conn.cursor()

        c.execute("PRAGMA table_info(rule_table)")
        columns = c.fetchall()
        required_columns = {"name", "if_field", "then_field"}
        actual_columns = {column[1] for column in columns}

        # check whether the database is valid
        if required_columns.issubset(actual_columns):
            print("The database is valid.")
        else:
            print("The database is invalid.")
            self.reconstruct()

    def reconstruct(self):
        # clear all content in the database
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = c.fetchall()
        for table in tables:
            c.execute(f"DROP TABLE IF EXISTS {table[0]}")
        c.execute("SELECT name FROM sqlite_master WHERE type='index'")
        indices = c.fetchall()
        for index in indices:
            c.execute(f"DROP INDEX IF EXISTS {index[0]}")
        self.conn.commit()

        # construct new content
        c.execute(
            """CREATE TABLE rule_table(name text, if_field text, then_field text)"""
        )
        self.conn.commit()


if __name__ == "__main__":
    sql: SqliteInterface()
