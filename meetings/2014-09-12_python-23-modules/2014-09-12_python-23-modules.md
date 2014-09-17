# Python - Modules

*****
## Objectives

1. Define a module 

2. Discuss differences between a script and a module

3. Discuss a module's special attribute `__name__`


*****
## Notes

**module** - a file consisting of Python code that defines functions, classes, and variables.

* allows for code to be organized and for related code to be grouped together making the code easier to understand and use.
* can use `import` to use functionality from a module in a script or in another module
* access the functionality of a module using **dot** notation

```python
import myawesomemodule

myawesomemodule.compute_something_cool()
```

* `sys` module example
```python
import sys

arguments = sys.argv()
```

* a module is a Python object and has special attributes:
    - `__name__`
    - `__file__`
    - `__doc__`
* `__name__` will be the string **__main__** if module is run like a script
* `__name__` will be the string **name of the module** if module is imported into another module or script
* a module can contain runnable code and can be run like a script using the following check:

```python
if __name__ == “__main__”:
    # do something here such as calling a main() function
    main()                  
```

**script vs. module**

* **average-script.py**
```python
# This script computes and prints the average

x = 2
y = 4
avg = (x + y) / 2
print(“The average is: ”), avg
```

* **average-module.py**

```python
# This module contains an average function
# and can be run like a script

def average(x, y):
    “”” Return the average “””
    return (x + y) / 2

def main():
    print(“The average is: ”), average(2, 4)

if __name__ == “__main__”:
    main()
```

*****
## Examples


Please see:

* [module_name.py](code/module_name.py)
* [module1.py](code/module1.py)
* [module2.py](code/module2.py)


*****
## References

* [Python modules]
* [Python modules - TutorialsPoint]

[Python modules]:https://docs.python.org/2/tutorial/modules.html
[Python modules - TutorialsPoint]:http://www.tutorialspoint.com/python/python_modules.htm