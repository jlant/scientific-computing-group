# Demo on debugging in Spyder

def square(num_list):
    """ Return the square of a list of numbers """
    result = []
    for num in num_list:
        ans = num**2
        result.append(ans)
    
    return result

def test_square():
    """ Test the functionality of square function """
    expected = [4, 16, 36, 64]
    
    actual = square(num_list = [2, 4, 6, 8])
    
    assert actual == expected, "actual {0} does not equal expected {1}".format(actual, expected)
    
# main program
x = [2, 4, 6, 8]
x_squared = square(x)

print(x_squared)               # testing - method 1 

assert x_squared == [4, 16, 36, 64], "x_squared is not the proper square!"      # testing - method 2

none_val = test_square()       # testing - method 3

print(none_val)
print("Yes, function is correct")

    