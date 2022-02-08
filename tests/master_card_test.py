from luhn import luhn

def test_shouldPassMC1() :
    assert luhn("5555555555554444")

def test_shouldPassMC2() :
    assert luhn("5105105105105100")

def test_shouldFail() :
    assert not luhn("5105105105203100")