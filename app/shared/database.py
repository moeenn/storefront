import sqlite3
from datetime import date, datetime, timedelta, timezone

from ulid import ULID


class Database:
    def __init__(self, filepath: str, migrations: list[str]) -> None:
        sqlite3.register_adapter(ULID, lambda val: str(val))
        sqlite3.register_adapter(date, lambda val: val.isoformat())
        sqlite3.register_adapter(datetime, lambda val: val.isoformat())

        self.conn = sqlite3.connect(filepath)
        self.conn.row_factory = self.row_factory()
        with self.conn:
            for mg in migrations:
                self.conn.executescript(mg)

    def row_factory(self):
        def dict_factory(cursor, row):
            fields = [col[0] for col in cursor.description]
            return dict(zip(fields, row))

        return dict_factory

    def close(self) -> None:
        self.conn.close()


def id() -> str:
    return str(ULID())


def now() -> datetime:
    local_tz = timezone(timedelta(hours=5))
    return datetime.now(local_tz)
