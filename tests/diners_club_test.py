from luhn import luhn

def test_shouldPassDinersClub1() :
    assert luhn("30569309025904")

def test_shouldPassDinersClub1() :
    assert luhn("38520000023237")

def test_shouldFail() :
    assert not luhn("385202200023237")