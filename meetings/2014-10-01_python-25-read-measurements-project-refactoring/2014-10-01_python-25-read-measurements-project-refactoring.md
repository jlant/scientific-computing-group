# Python - Read measurements project, refactoring

*****
## Objectives

1.  Refactor the read_measurements.py file to dynamically handle any order, number, or set of parameters.


*****
## Notes

* [enumerate] - a built-in Python function that returns an enumerate object. Allows you to loop (iterate) over a sequence,
like a [list], and have access to each sequence item and its respective index; e.g. you can create a list of tuples where 
each tuple is an (index, item) pair using `list(enumerate(sequence))`. 

* [dictionaries] - unordered sets of *key*:*value* pairs; maps a *key* to a *value*
 
* [list] - ordered sequence of items

*****
## Examples

**enumerate**
```python
>>> column_names = ["dates", "discharge", "stage", "temperature"]
>>> type(enumerate(column_names))
<type 'enumerate'>
>>> column_names = list(enumerate(column_names))
>>> print(column_names)
[(0, 'dates'), (1, 'discharge'), (2, 'stage'), (3, 'temperature')]
>>> for index, name in column_names:
...     print(index, name)
...
(0, 'date')
(1, 'discharge')
(2, 'stage')
(3, 'temperature')



```

**dictionaries**
```python
>>> data = {"dates": ["2014-01-01", "2014-01-02", "2014-01-03"],
...         "discharge": [100, 112, 110],
...         "stage": [25, 34, 29],
...         "temperature": [2, 3, 5]
... }

>>> for key, value in data:
...     print(key, value)
...
('discharge', [100, 112, 110])
('dates', ['2014-01-01', '2014-01-02', '2014-01-03'])
('temperature', [2, 3, 5])
('stage', [25, 34, 29])
```

*****
## Questions / Comments


*****
## References

* [enumerate] 
* [list]
* [dictionaries]

[dictionaries]:https://docs.python.org/2/tutorial/datastructures.html#dictionaries
[enumerate]:https://docs.python.org/2/library/functions.html#enumerate
[list]:https://docs.python.org/2/tutorial/datastructures.html#