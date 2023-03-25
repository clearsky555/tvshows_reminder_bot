from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    select,

)


from config import MYSQL_URL


engine = create_engine(MYSQL_URL)
meta = MetaData()


class TVShowsManager():
    def __init__(self, engine) -> None:
        self.engine = engine
        self.shows = self.get_shows_schema()

    def get_shows_schema(self):
        shows = Table(
            'tvshows', meta,
            Column('id', Integer, primary_key=True),
            Column('place', Integer),
            Column('title', String(255)),
            Column('year', String(10)),
            Column('rating', String(10)),
            Column('link', String(255))
        )
        return shows

    def create_table(self):
        meta.create_all(self.engine, checkfirst=True)
        print('таблица успешно создана')

    def insert_show(self, data):
        ins = self.shows.insert().values(
            **data
        )
        with self.engine.connect() as connect:
            connect.execute(ins)
            connect.commit()

    def delete_table(self):
        self.shows.drop(self.engine, checkfirst=True)
        print('таблица успешно удалена')

    # def get_shows(self):
    #     query = pass
    #     connect = self.engine.connect()
    #     result = connect.execute(query)
    #     connect.close()
    #     shows = result.fetchall()
    #     return shows

    def get_shows(self):
        query = self.shows.select()
        with self.engine.connect() as connect:
            result = connect.execute(query)
            shows = result.fetchall()
        return shows


class UsersManager:
    def __init__(self, engine) -> None:
        self.engine = engine
        self.user = self.get_users_schema()

    def get_users_schema(self):
        users = Table(
            'users', meta,
            Column('id', Integer, primary_key=True),
            Column('user_id', String(15)),
            Column('link', String(255))
        )
        return users

    def insert_user_show(self, data):
        ins = self.user.insert().values(
            **data
        )
        with self.engine.connect() as connect:
            connect.execute(ins)
            connect.commit()

    def get_shows(self):
        query = self.user.select()
        with self.engine.connect() as connect:
            result = connect.execute(query)
            users = result.fetchall()
        return users

    # def search_by_id(self, id):
    #     query = select(self.user.columns.link).where(self.user.columns.user_id == str(id))
    #
    #     connect = self.engine.connect()
    #     result = connect.execute(query)
    #     connect.close()
    #     shows = result.fetchall()
    #     return shows

    def search_by_id(self, id):
        query = select(self.user.columns.link).where(self.user.columns.user_id == str(id))

        with self.engine.connect() as connect:
            result = connect.execute(query)
            links = [row[0] for row in result]
        return links