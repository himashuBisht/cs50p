from bank import value

def test_zero():
    assert value('hello') == 0
    assert value('Hello') == 0
    # assert value('HELLO') == 0
    assert value('hELLO dear') == 0

# def test_case_insensitivity():
def test_tt():
    assert value('hi') ==20
    # assert value('hey') ==20
    assert value('held') ==20


def test_hund():
    assert value('dear')==100
    assert value('1234') == 100
    assert value("What's up") == 100

# def test_incorrect():
# def test_phrase():

