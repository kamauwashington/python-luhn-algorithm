from luhn import luhn

def test_shouldPassDankort() :
    assert luhn("5019717010103742")

def test_shouldFail() :
    assert not luhn("5019717010103741")