from luhn import luhn

def test_shouldFailOnNone() :
    assert not luhn(None)

def test_shouldFailOnEmpty() :
    assert not luhn("     ")

def test_shouldFailOnNoDigits() :
    assert not luhn("  hello I am not valid CC input   ")

def test_shouldFailIfLessThan2Digits() :
    assert not luhn("1")

def test_shouldSucceedOn2DigitsWithValidCheckbit() :
    assert luhn("91")

def test_shouldSucceedOnFormattedCC() :
    assert luhn("5455 3307 6000 0018")