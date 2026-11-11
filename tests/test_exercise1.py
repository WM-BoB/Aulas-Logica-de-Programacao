from exercise1 import odd_numbers, elevated_odd_numbers

def test_odd_numbers():
    assert odd_numbers() == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
def test_elevated_odd_numbers():
    assert elevated_odd_numbers(odd_numbers()) == [1, 27, 125, 343, 729, 1331, 2197, 3375, 4913, 6859]