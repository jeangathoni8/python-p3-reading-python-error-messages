# an_assertion_error.py

def evaluate_two_values(a, b):
    assert a == b, "Values are not equal"
    return True

print(evaluate_two_values(2, 2))  # Should not raise an AssertionError
