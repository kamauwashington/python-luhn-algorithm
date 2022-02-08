from luhn import luhn

def test_shouldPassVisa1() :
    assert luhn("4111111111111111")

def test_shouldPassVisa2() :
    assert luhn("4012888888881881")

def test_shouldPassVisa3() :
    assert luhn("4222222222222")

def test_shouldFail() :
    assert not luhn("4222322222222")