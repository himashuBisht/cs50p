from plates import is_valid

def main():
    test_min_max_len()
    test_two_letter()
    test_num_middle()
    test_first_number_zero()
    test_other_characters()

def test_min_max_len():
    assert is_valid('A') == False
    assert is_valid('AB') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

def test_two_letter():
        assert is_valid('AB') == True
        assert is_valid('A1') == False
        # assert is_valid('11') == False

def test_num_middle():
    assert is_valid("AAA222") == True
    # assert is_valid("AAA22A") == False
    assert is_valid("cs50p2") == False

# The first number used cannot be a ‘0’
def test_first_number_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05P") == False

# No periods, spaces, or punctuation marks are allowed
def test_other_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("Hello!") == False

if __name__ == "__main__":
    main()