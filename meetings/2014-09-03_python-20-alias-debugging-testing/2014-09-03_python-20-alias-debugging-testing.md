**Topic:**

*****
**Objectives:**

1. Discuss and review aliasing.

2. Debug a program using the Python debugger in the Spyder IDE.

3. Learn a few ways to test a function.


*****
**Notes:**

* Lists can be mutated in functions

* A **debugger** prevents you from having to change / alter your code with print statements

* Debugging keywords and keyboard shortcuts in [Spyder IDE]:

    - [Breakpoint] - an intentional stopping or pausing at a particular place in a program in order to debug the program; set a breakpoint on a particular line using `F12` or double clicking line number

    - Debug file (`Ctrl+F5`) 

    - Run current line (`Ctrl+F10`)
    
    - Step into function or method of current line (`Ctrl+F11`)
    
    - Run until current function or method returns (`Ctrl+Shift+F11`)

    - Continue execution until next breakpoint (`Ctrl+F12`)
    
    - Exit debug mode (`Ctrl+Shift+F12`)

* A **function** *without* a return statement stills returns `None`

* **Testing functions** - A few methods:
    
    1. use `print()` function or `print` statements in main program and function to manually check validity  
    
    2. use `assert` statements in main program
    
        - `assert actual == expected, "some error message"`
        
    3. write a **test function** which contains an assert statement; can have many test functions for a single function

*****
**Examples:**

**Aliasing in functions** - a list can be mutated in a function

    def appender(x_list, number):
		x_list.append(number)
		
		return None

	x = range(10)
	appender(x, 100)
	print(x)


**Testing** - a few methods

    def square(num_list):
        """ Return a list containing the squares of each element in a list of numbers """
        result = []
        for num in num_list:
            ans = num**2
            result.append(ans)
        
        return result
    
    def test_square():
        """ Test the functionality of the square function """
        expected = [4, 16, 36, 64]
        
        actual = square(num_list = [2, 4, 6, 8])
        
        assert actual == expected, "actual {0} does not equal expected {1}".format(actual, expected)
        
    # main program
    x = [2, 4, 6, 8]
    x_squared = square(x)
    
    # testing - method 1 
    print(x_squared)               
    
    # testing - method 2
    assert x_squared == [4, 16, 36, 64], "x_squared is not the proper square!"      
    
    # testing - method 3
    test_square()       
    
    print("Yes, tests pass!")

*****
**Questions / Comments**


*****
**What you learned and/or would have liked to have learned more about the topic?**


*****
**References:**

* [Breakpoint]

* [Spyder IDE]

[Breakpoint]:http://en.wikipedia.org/wiki/Breakpoint
[Spyder IDE]:https://code.google.com/p/spyderlib/

