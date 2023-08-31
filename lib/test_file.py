
from stacks import is_balanced
from sequences import remove_duplicates
from dictionaries import word_frequency

def test_is_balanced():
    expression1 = "([]{})"
    expression2 = "([)]"
    
    assert is_balanced(expression1) == True
    assert is_balanced(expression2) == False



def test_remove_duplicates():
    input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = remove_duplicates(input_sequence)
    
    assert result == [2, 3, 4, 5, 6, 7]



def test_word_frequency():
    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    
    assert result == {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}
