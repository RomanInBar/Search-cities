from sqlalchemy.orm import Mapped, mapped_column

from database.engine import Base


class City(Base):
    __tablename__ = 'cities'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    latitute: Mapped[float] = mapped_column(nullable=False)
    longtitute: Mapped[float] = mapped_column(nullable=False)
