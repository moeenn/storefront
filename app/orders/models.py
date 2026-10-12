from datetime import datetime
from enum import Enum
from typing import Any, Self

from pydantic import BaseModel

from app.shared.database import dbtimestamp_optional_parse, dbtimestamp_parse


class OrderStatus(Enum, str):
    PENDING = "PENDING"
    PAYMENT_RECEIVED = "PAYMENT_RECEIVED"
    ENROUTE = "ENROUTE"
    COMPLETE = "COMPLETE"


class Order(BaseModel):
    id: str
    customer_id: str
    status: OrderStatus
    delivery_date: datetime | None
    remarks: str | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    @classmethod
    def from_row(cls, row: Any) -> Self:
        return cls(
            id=row["id"],
            customer_id=row["customer_id"],
            status=row["status"],
            delivery_date=dbtimestamp_optional_parse(row["delivery_date"]),
            remarks=row["remarks"],
            created_at=dbtimestamp_parse(row["created_at"]),
            updated_at=dbtimestamp_parse(row["updated_at"]),
            deleted_at=dbtimestamp_optional_parse(row["deleted_at"]),
        )


class OrderItem(BaseModel):
    order_id: str
    product_id: str
    quantity: int
    total_price: int

    @classmethod
    def from_row(cls, row: Any) -> Self:
        return cls(
            order_id=row["order_id"],
            product_id=row["product_id"],
            quantity=row["quantity"],
            total_price=row["total_price"],
        )
