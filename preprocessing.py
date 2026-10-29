"""Funkcje do wstępnego przetwarzania danych."""


def remove_missing_values(data):
    """Usuwa wartości None z listy."""
    return [value for value in data if value is not None]


def normalize_data(data):
    """Normalizuje dane do przedziału od 0 do 1."""
    if not data:
        raise ValueError("Lista danych nie może być pusta.")

    minimum = min(data)
    maximum = max(data)

    if minimum == maximum:
        return [0.0] * len(data)

    return [
        (value - minimum) / (maximum - minimum)
        for value in data
    ]


def calculate_mean(data):
    """Oblicza średnią arytmetyczną."""
    if not data:
        raise ValueError("Lista danych nie może być pusta.")

    return sum(data) / len(data)
