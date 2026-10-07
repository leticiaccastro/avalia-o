from datetime import date

from app.database import Base, engine, SessionLocal
from app.crud import (
    inserir_tutor,
    inserir_animal,
    inserir_atendimento
)


# Criação das tabelas
Base.metadata.create_all(bind=engine)


# Criação da sessão
db = SessionLocal()


try:
    # =========================
    # TUTORES
    # =========================

    tutor1 = inserir_tutor(
        db,
        "Seu Nome",
        "(61) 99999-1111",
        "seunome@email.com"
    )

    print(
        f"Tutor inserido: {tutor1.nome_completo} "
        f"(id={tutor1.id})"
    )


    tutor2 = inserir_tutor(
        db,
        "Maria Oliveira",
        "(61) 98888-2222",
        "maria@email.com"
    )

    print(
        f"Tutor inserido: {tutor2.nome_completo} "
        f"(id={tutor2.id})"
    )


    # =========================
    # ANIMAIS
    # =========================

    animal1 = inserir_animal(
        db,
        "Rex",
        "cão",
        "Labrador",
        28.5,
        tutor1.id
    )

    print(
        f"Animal inserido: {animal1.nome_animal} "
        f"- {animal1.especie}"
    )


    animal2 = inserir_animal(
        db,
        "Mimi",
        "gato",
        "Siamês",
        4.2,
        tutor2.id
    )

    print(
        f"Animal inserido: {animal2.nome_animal} "
        f"- {animal2.especie}"
    )


    animal3 = inserir_animal(
        db,
        "Luna",
        "ave",
        "Calopsita",
        0.09,
        tutor1.id
    )

    print(
        f"Animal inserido: {animal3.nome_animal} "
        f"- {animal3.especie}"
    )


    # =========================
    # DATA ATUAL
    # =========================

    data_hoje = date.today().strftime("%d/%m/%Y")


    # =========================
    # ATENDIMENTOS
    # =========================

    atend1 = inserir_atendimento(
        db,
        data_hoje,
        "Vacina anual V8",
        180.00,
        animal1.id
    )

    print(
        f"Atendimento: {atend1.motivo} | "
        f"R$ {atend1.valor_cons:.2f}"
    )


    atend2 = inserir_atendimento(
        db,
        data_hoje,
        "Consulta veterinária de rotina",
        120.00,
        animal2.id
    )

    print(
        f"Atendimento: {atend2.motivo} | "
        f"R$ {atend2.valor_cons:.2f}"
    )


    atend3 = inserir_atendimento(
        db,
        data_hoje,
        "Avaliação de saúde da ave",
        100.00,
        animal3.id
    )

    print(
        f"Atendimento: {atend3.motivo} | "
        f"R$ {atend3.valor_cons:.2f}"
    )


    print("\nTodos os dados foram inseridos com sucesso!")


finally:
    db.close()