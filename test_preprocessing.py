"""Testy jednostkowe modułu preprocessing."""

import pytest

from preprocessing import (
    remove_missing_values,
    normalize_data,
    calculate_mean,
)


def test_remove_missing_values():
    """Sprawdza usuwanie brakujących wartości."""
    data = [1, None, 3, None, 5]

    result = remove_missing_values(data)

    assert result == [1, 3, 5]


def test_normalize_data():
    """Sprawdza normalizację liczb."""
    data = [10, 20, 30]

    result = normalize_data(data)

    assert result == [0.0, 0.5, 1.0]


def test_normalize_identical_values():
    """Sprawdza normalizację jednakowych liczb."""
    assert normalize_data([5, 5, 5]) == [0.0, 0.0, 0.0]


def test_calculate_mean():
    """Sprawdza obliczanie średniej."""
    assert calculate_mean([10, 20, 30]) == 20.0


def test_normalize_empty_list():
    """Sprawdza obsługę pustej listy."""
    with pytest.raises(ValueError):
        normalize_data([])


def test_calculate_mean_empty_list():
    """Sprawdza obsługę pustej listy."""
    with pytest.raises(ValueError):
        calculate_mean([])
