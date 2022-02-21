import pytest


@pytest.mark.parametrize("tup, val, res",
                         [((1, 2, 3, 2, 5, 2), 2, 3),
                          ((8, 5, 6, 8, 15), 8, 2),
                          ((8, 10, 15, 22, 14), 2, 0)])
def test_check_count(tup, val, res):
    """Параметрический."""
    assert tup.count(val) == res


def test_check_index():
    """Негативный."""
    with pytest.raises(AssertionError):
        assert (1, 2, 3, 4).index(1) == 1


def test_check_mutability():
    """Валидный тест с ошибкой."""
    tup = (777, 1337, 1488)
    try:
        assert tup[0] == 15
    except AssertionError:
        pass


@pytest.mark.parametrize("set_values, res", [({1, 2, 3, 4}, 4),
                                             ({1, 2, 1, 4}, 3),
                                             ({1, 2, 3, 2}, 3),
                                             ({4, 4, 4, 4}, 1)])
def test_check_sets_len_ability(set_values, res):
    """Параметрический."""
    assert len(set_values) == res


def test_check_add_remove_contained_obj():
    """Негативный."""
    set2 = {1, 1, 2, 3, 4}
    with pytest.raises(AssertionError):
        set2.add(1)
        assert len(set2) != 5
        set2.remove(1)
        assert len(set2) != 3


def test_check_copy():
    """Валидный с ошибкой."""
    set3 = {1, 2, 'my name is', 3, 4, 5, 1, 'hi'}
    set3_cp = set3.copy()
    try:
        assert set3 == set3_cp
    except TypeError:
        pass
