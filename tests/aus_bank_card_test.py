from luhn import luhn

def test_shouldPassAustralianBankCard() : 
    assert luhn("5610591081018250")

def test_shouldFail() :
    assert not luhn("5610581091018250")