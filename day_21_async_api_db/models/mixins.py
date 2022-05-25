from datetime import datetime

from sqlalchemy import DateTime, func, Column


class TimestampMixin:
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=datetime.utcnow
    )
