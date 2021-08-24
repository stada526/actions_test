from sample import add, mul


def test_add():
    TEST_DATA = (2, 3)
    EXPECTED = 5
    res = add(*TEST_DATA)
    assert res == EXPECTED


def test_mul():
    TEST_DATA = (2, 3)
    EXPECTED = 6
    res = mul(*TEST_DATA)
    assert res == EXPECTED
