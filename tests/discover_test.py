from luhn import luhn

def test_shouldPassDiscover1() :
    assert luhn("6011111111111117")

def test_shouldPassDiscover2() :
    assert luhn("6011000990139424")

def test_shouldFail() :
    assert not luhn("6011000390134424")