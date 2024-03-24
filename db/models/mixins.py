from datetime import datetime, timezone
from sqlalchemy import DateTime, Column
from sqlalchemy.orm import declarative_mixin

@declarative_mixin
class Timestamp:
    created_at =  Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at =  Column(DateTime, default=datetime.utcnow, nullable=False)

    