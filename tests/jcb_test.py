from luhn import luhn

def test_shouldPassJCB1() :
    assert luhn("3530111333300000")

def test_shouldPassJCB2() :
    assert luhn("3566002020360505")

def test_shouldFail() :
    assert not luhn("3566002020250505")