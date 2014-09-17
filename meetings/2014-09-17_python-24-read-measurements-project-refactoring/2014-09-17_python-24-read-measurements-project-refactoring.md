# Python - Read measurements project, refactoring

*****
## Objectives

1. Refactor the read_measurements.py file with functions.

*****
## Notes

* **git log commands**

```
git log
git log -3
git log --pretty=oneline 
git log --pretty=medium (default)
git log --pretty=full
git log --pretty=fuller
```

* **Make functions that perform a particular functionality**
    * keeps your functions small and allows for them to be tested more easily

```
def compute_stats():
    ...

def find_date():
    ...
```

* **Have a main() "like" function or set of runnable lines of code that can be read and understood easily**
```
def main():
    read_file(...)
    extract_data(...)
    process_data(...)
    print_results(...)
    plot_results(...)

```

* [Code and Data for the Social Sciences: A Practitioner's Guide] 

```
Keep it short and purposeful. 
Make your functions shy. 
Order your functions for linear reading. 
Us descriptive names. 
Pay special attention to coding algebra. 
Make logical switches intuitive. 
Be consistent. 
Check for errors. 
Write tests. 
Profile slow code relentlessly. 
Store too much output from slow code. 
Separate slow code from fast code. 
```

*****
## Examples


*****
## Questions / Comments



*****
## References

* [Git - Viewing the Commit History]
* [Code and Data for the Social Sciences: A Practitioner's Guide] 


[Git - Viewing the Commit History]:http://git-scm.com/book/en/Git-Basics-Viewing-the-Commit-History
[Code and Data for the Social Sciences: A Practitioner's Guide]:http://faculty.chicagobooth.edu/matthew.gentzkow/research/CodeAndData.xhtml