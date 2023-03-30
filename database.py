from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    select,
    delete,
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
            Column('show_title', String(255)),
            Column('link', String(255)),
            extend_existing=True
        )
        return users

    def create_table(self):
        meta.create_all(self.engine, checkfirst=True)

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

    def search_by_id(self, id):
        query = select(self.user.columns.link).where(self.user.columns.user_id == str(id))

        with self.engine.connect() as connect:
            result = connect.execute(query)
            links = [row[0] for row in result]
        return links

    def select_all_shows(self):

        query = select(self.user.columns.link)
        with self.engine.connect() as connect:
            result = connect.execute(query)
            links = [row[0] for row in result]
        return links

    def get_users_id(self, show):
        query = select(self.user.columns.user_id).where(self.user.columns.link == show)

        with self.engine.connect() as connect:
            result = connect.execute(query)
            id = [row[0] for row in result]
        return [[id, show]]

    def delete_show_from_db(self, id, show):
        stmt = delete(self.user).where((self.user.columns.user_id == id) & (self.user.columns.link == show))
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    def get_show_title_from_db(self, link):
        query = select(self.user.columns.show_title).where(self.user.columns.link == link)
        with self.engine.connect() as connect:
            result = connect.execute(query)
            title = [row[0] for row in result]
        return title[0] if title else None

    def get_all_shows_by_id(self, id):
        query = select(self.user.columns.show_title).where(self.user.columns.user_id == id)
        with self.engine.connect() as connect:
            result = connect.execute(query)
            titles = [row[0] for row in result]
        return titles

users_manager = UsersManager(engine=engine)
