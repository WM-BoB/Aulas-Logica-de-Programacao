from lists_tuples_and_sets import fruits_with_letter

def test_fruits_with_letter_tuple():
    assert fruits_with_letter('a', ('apple', 'banana', 'cherry')) == ['apple', 'banana']
    
def test_fruits_with_letter_list():
    assert fruits_with_letter('e', ['apple', 'banana', 'cherry']) == ['apple', 'cherry']