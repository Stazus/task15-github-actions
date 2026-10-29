
# Task 15 – GitHub Actions CI

Projekt demonstracyjny automatycznego testowania kodu Python z wykorzystaniem GitHub Actions i pytest.

## Funkcjonalności

Moduł `preprocessing.py` zawiera trzy funkcje:

- `remove_missing_values()` – usuwa wartości `None` z listy.
- `normalize_data()` – normalizuje wartości liczbowe do przedziału 0–1.
- `calculate_mean()` – oblicza średnią arytmetyczną.

## Testy jednostkowe

Plik `test_preprocessing.py` zawiera 6 testów jednostkowych, które sprawdzają poprawność działania funkcji oraz obsługę przypadków brzegowych.

Instalacja zależności:

```bash
python -m pip install -r requirements.txt
```

Uruchomienie testów:

```bash
python -m pytest -v
```

## GitHub Actions

Workflow `.github/workflows/test.yml` automatycznie:

1. Pobiera kod repozytorium.
2. Konfiguruje Python 3.12.
3. Instaluje zależności z `requirements.txt`.
4. Uruchamia testy jednostkowe.

Workflow uruchamia się przy każdym `push` oraz przy zdarzeniach `pull_request`.

## Technologie

- Python 3.12
- pytest 9.2.0
- Git i GitHub
- GitHub Actions

## Autor

Stanisław Flak

Projekt wykonany w ramach lekcji 3 kursu Data Science – LearnIT.
