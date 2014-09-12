Python Scoping
==============

*****
## Objectives

1. Discuss Python scoping

*****
**Notes:**

* [namespace] - a mapping from variable names to objects; container for variable names

* **scope** - region of a program where a namespace can be accessed

* Python variables are looked up from [namespace]s according to the **LEGB** order rule:

    - **L**ocal function scope
    - **E**nclosing function scope
    - **G**lobal scope
    - **B**uiltin scope



*****
## Examples

**Scoping** - local vs. global variables

```python
z = 1                       # global variable z
def funny_add(x, y):
    z = 2                   # local variable z
    ans = x + y + z
    
    return ans

# call funny_add() function
funny_add(x = 3, y = 7)

```

Please see: 

* [scoping1.py](code/scoping1.py)
* [scoping2.py](code/scoping2.py)
* [scoping3.py](code/scoping3.py)
* [scoping4.py](code/scoping4.py)
* [scoping5.py](code/scoping5.py)

*****
## Questions / Comments

**Q**: Ask about indention errors later and strange behavior when writing functions in notepad++.

**A**: Indention errors are most likely caused by incorrect indent alignment or an incorrect 
**tab size** if you use the `Tab` key.  Make sure your **tab size** is set to 4 spaces for 
Python code, or just manually hit the space bar 4 times when indenting.


*****
## References

* [Learning Python: Scoping]
* [namespace]
* [Python Scopes and Namespaces]
* [StackOverflow: Scoping]

[Python Scopes and Namespaces]:https://docs.python.org/2/tutorial/classes.html
[Learning Python: Scoping]:https://www.inkling.com/read/learning-python-mark-lutz-4th/chapter-17/python-scope-basics
[namespace]:http://en.wikipedia.org/wiki/Namespace
[StackOverflow: Scoping]:http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules
