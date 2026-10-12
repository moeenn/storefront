from app.shared.database import Database, now

from .models import Order, OrderItem


class OrdersRepo:
    db: Database

    def __init__(self, db: Database) -> None:
        self.db = db

    def list(self) -> list[Order]:
        query = """
            select * from orders
            where deleted_at is null
            order by updated_at desc
        """
        with self.db.conn:
            cur = self.db.conn.execute(query)
            return [Order.from_row(row) for row in cur.fetchall()]

    def create(self, o: Order) -> None:
        query = """
            insert into orders (id, customer_id, status, delivery_date, remarks, created_at, updated_at)
            values (?, ?, ?, ?, ?, ?, ?)
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            cur.execute(
                query,
                (
                    o.id,
                    o.customer_id,
                    o.status,
                    o.deleted_at,
                    o.remarks,
                    o.created_at,
                    o.updated_at,
                ),
            )

    def update(self, o: Order) -> None:
        query = """
            update orders
            set customer_id = ?,
                status = ?,
                delivery_date = ?,
                remarks = ?,
                updated_at = ?
            where id = ?
        """
        with self.db.conn:
            self.db.conn.cursor().execute(
                query,
                (o.customer_id, o.status, o.delivery_date, o.remarks, now(), o.id),
            )

    def remove(self, id: str) -> None:
        query = """
            update orders
            set deleted_at = ?
            where id = ?
        """
        with self.db.conn:
            self.db.conn.cursor().execute(query, (now(), id))


class OrderItemsRepo:
    db: Database

    def __init__(self, db: Database) -> None:
        self.db = db

    def clear_order_items(self, order_id: str) -> None:
        query = """
            delete from order_items
            where order_id = ?
        """
        with self.db.conn:
            self.db.conn.cursor().execute(query, (order_id,))

    def create(self, order_id: str, items: list[OrderItem]) -> None:
        query = """
            insert into order_items (order_id, product_id, quantity, total_price)
            values (?, ?, ?, ?)
        """
        with self.db.conn:
            cur = self.db.conn.cursor()
            for it in items:
                cur.execute(
                    query,
                    (
                        order_id,
                        it.product_id,
                        it.quantity,
                        it.total_price,
                    ),
                )
