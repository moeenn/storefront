from app.shared.database import Database, now

from .model import Product


class ProductsRepo:
    db: Database

    def __init__(self, db: Database) -> None:
        self.db = db

    def list(self) -> list[Product]:
        query = """
            select * from products
            where deleted_at is none
            order by code desc
        """
        with self.db.conn:
            cur = self.db.conn.execute(query)
            return [Product.from_row(row) for row in cur.fetchall()]

    def create(self, p: Product) -> None:
        query = """
            insert into products (id, name, code, price)
            values (?, ?, ?, ?)
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            cur.execute(query, (p.id, p.name, p.code, p.price))

    def update(self, p: Product) -> None:
        query = """
            update products
            set name = ?,
                code = ?,
                price = ?
            where id = ? and deleted_at is null
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            cur.execute(query, (p.id, p.name, p.code, p.price))

    def remove(self, id: str) -> None:
        query = """
            update products
            set deleted_at = ?
            where id = ?
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            cur.execute(query, (now(), id))
