from datetime import datetime
from typing import Any, Self

from pydantic import BaseModel

from app.shared.database import dbtimestamp_optional_parse, dbtimestamp_parse


class Customer(BaseModel):
    id: str
    name: str
    phone: str
    email: str | None
    created_at: datetime
    deleted_at: datetime | None

    @classmethod
    def from_row(cls, row: Any) -> Self:
        return cls(
            id=row["id"],
            name=row["name"],
            phone=row["phone"],
            email=row["email"],
            created_at=dbtimestamp_parse(row["created_at"]),
            deleted_at=dbtimestamp_optional_parse(row["deleted_at"]),
        )
