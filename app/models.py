from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome_completo: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    telefone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    email: Mapped[str | None] = mapped_column(
        String(100),
        unique=False,
        nullable=True
    )


class Animal(Base):
    __tablename__ = "animais"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome_animal: Mapped[str | None] = mapped_column(
        String(60),
        nullable=True
    )

    especie: Mapped[str | None] = mapped_column(
        String(40),
        nullable=True
    )

    raca: Mapped[str | None] = mapped_column(
        String(60),
        nullable=True
    )

    peso_kg: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    tutor_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("tutores.id"),
        nullable=True
    )


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data_atend: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    motivo: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    valor_cons: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    animal_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("animais.id"),
        nullable=True
    )