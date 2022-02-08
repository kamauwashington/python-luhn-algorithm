from luhn import luhn

def test_shouldPassAmex1() :
    assert luhn("378282246310005")

def test_shouldPassAmex2() :
    assert luhn("371449635398431")

def test_shouldPassAmexCorporatet() : 
    assert luhn("378734493671000")

def test_shouldFail() :
    assert not luhn("3782 82246 310004")