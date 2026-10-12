from datetime import datetime
from typing import Any, Self

from pydantic import BaseModel

from app.shared.database import dbtimestamp_optional_parse


class Product(BaseModel):
    id: str
    name: str
    code: str
    price: int
    deleted_at: datetime | None

    @classmethod
    def from_row(cls, row: Any) -> Self:
        return cls(
            id=row["id"],
            name=row["name"],
            code=row["code"],
            price=row["price"],
            deleted_at=dbtimestamp_optional_parse(row["deleted_at"]),
        )
