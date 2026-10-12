from app.repos import OrderItemsRepo, OrdersRepo


class OrdersService:
    orders_repo: OrdersRepo
    order_items_repo: OrderItemsRepo

    def __init__(
        self, orders_repo: OrdersRepo, order_items_repo: OrderItemsRepo
    ) -> None:
        self.orders_repo = orders_repo
        self.order_items_repo = order_items_repo

    def create_order(self) -> None: ...
