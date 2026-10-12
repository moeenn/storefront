from app.shared.database import Database, now

from .model import Customer


class CustomersRepo:
    db: Database

    def __init__(self, db: Database) -> None:
        self.db = db

    def list(self) -> list[Customer]:
        query = """
            select * from customers
            where deleted_at is null
        """
        with self.db.conn:
            cur = self.db.conn.execute(query)
            return [Customer.from_row(row) for row in cur.fetchall()]

    def create(self, c: Customer) -> None:
        query = """
            insert into customer (id, name, phone, email, created_at)
            values (?, ?, ?, ?, ?)
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            cur.execute(query, (c.id, c.name, c.phone, c.email, c.created_at))

    def update(self, c: Customer) -> None:
        query = """
            update customers
            set name = ?,
                phone = ?,
                email = ?
            where id = ? and
                  deleted_at is null
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            cur.execute(query, (c.name, c.phone, c.email, c.id))

    def remove(self, id: str) -> None:
        query = """
            update customers
            set deleted_at = ?
            where id = ?
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            cur.execute(query, (now(), id))
