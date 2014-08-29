Version Control - Git
=====================

*****
Objectives
----------

1. Define version control
2. Write basic git commands
3. Create a git repository

*****
Notes
-----

**Version Control** - used to keep track (a history) of what you have done and to collaborate with others.

**Version Control** definition from [Software Carpentry - Version Control]:

	A tool for managing changes to a set of files. Each set of changes creates a new revision of the files; the
	version control system allows users to recover old revisions reliably, and helps manage conflicting changes made by different users.

**Basic Git Commands**

	git init		-	initializes a git repository
	git add			-	add file(s) to git staging area; use before making a stamped version or commit
	git commit		- 	commit file(s) in staging area to a stamped version
	git status		-	view current status of repository
	git log			-	view history of repository
	git diff		-	show the difference between the current version of a file and the last committed version of a file

**Configure your name, email, and editor**

	git config -global user.name <your name>
	git config -global user.email <your email>
	git config -global core.editor <your favorite editor>
	
*****
Examples
--------

	$ git init my-first-project
	$ cd my-first-project
	$ touch some-awesome-code.py
	
	Write some awesome code ...
	
	$ git add some-awesome-code.py
	$ git commit -m "first commit of code" some-awesome-code.py
	
*****
References
----------

* [Software Carpentry - Version Control]
* [Pro Git]
* [Git - Introductory Videos]
* [Git Tutorials - Git Basics]

[Software Carpentry - Version Control]:http://software-carpentry.org/v4/vc/index.html
[Pro Git]:http://git-scm.com/book
[Git - Introductory Videos]:http://git-scm.com/videos
[Git Tutorials - Git Basics]:https://www.atlassian.com/git/tutorial/git-basics