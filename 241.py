from math import ceil
from typing import Iterable, Tuple

MIN_AGE = 14
MAX_AGE = 120

def get_your_age(prompt: str = "Informe sua idade: ") -> int:
    # Lê e valida a idade do usuário (inteiro entre MIN_AGE e MAX_AGE).
    while True:
        s = input(prompt).strip()
        try:
            idade = int(s)
        except ValueError:
            print("Insira um número inteiro.")
            continue
        if idade < 0:
            print("Idade não pode ser negativa.")
            continue
        if idade > MAX_AGE or idade < MIN_AGE:
            print(f"Idade inválida. Informe um valor entre {MIN_AGE} e {MAX_AGE}.")
            continue
        return idade

def _rules() -> Iterable[Tuple[int, int, int]]:
    # Retorna (min_age, max_age, offset) para cada faixa.
    return (
        (20, 29, 9),
        (30, 39, 10),
        (40, 49, 11),
        (50, 59, 12),
        (60, 69, 13),
        (70, 79, 14),
        (80, 89, 15),
        (90, 120, 16),
        (100, 120, 17),
        (110, 120, 18),
        (120, 120, 19)
    )

def check_age(idade: int) -> int:
    """
    Calcula a idade ideal aplicando uma fórmula por faixa etária.
    Retorna um inteiro.
    """
    for min_a, max_a, offset in _rules():
        if min_a <= idade <= max_a:
            return ceil((idade / 2) + offset)
    #  padrão quando não estiver nas faixas acima.
    return ceil((idade / 2) + 7)

def main() -> None:
    idade = get_your_age()
    ideal = check_age(idade)
    print(f"A sua idade é {idade} anos e a idade ideal para torar ela é {ideal}.")

if __name__ == "__main__":
    main()