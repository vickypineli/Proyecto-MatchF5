import sqlite3


class Info:
    def __init__(self, app_name):
        self.app_name = app_name

    def to_dict(self):
        return {"app_name": self.app_name}


class InfoRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists info (
                app_name varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_info(self):
        sql = """select * from info"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()

        return Info(app_name=data["app_name"])

    def save(self, info):
        sql = """insert into info (app_name) values (
            :app_name
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, info.to_dict())
        conn.commit()
