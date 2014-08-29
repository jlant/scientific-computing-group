Version Control - Git
=====================

*****
Objectives
----------

1. Explore the history of a version controlled file
2. Recover an old version of a file
3. Define a remote repository
4. Sign up with a hosting site
	* [GitHub]
	* [Bitbucket]

*****
Notes
-----

**Remote repository** - versions of your project that are hosted on the Internet or network somewhere. You can have several of them,
each of which generally is either read-only or read/write for you. See [Git Basics - Working with Remotes] and [Git Tutorials - Remote Repositories].

**Public repository** - anyone can view the repository, but you choose who can commit.

**Private repository** - you choose who can view and commit to the repository.

**Git Commands - Explore History**

	git diff <file-name>						- 	show the difference between the current version of a file and the last committed version 
	git diff HEAD~2 <file-name>					- 	show the difference between the current version of a file and the 2nd to last committed version 
	git diff <unique-commit-id> <file-name>		- 	show the difference between the current version of a file and a particular committed version 
		
		
**Git Commands - Recover Previous Versions**

	git checkout HEAD <file-name>					-	recover last committed version of a file
	git checkout <unique-commit-id> <file-name>		-	recover a previous version of a file at a particular commit

		
**Git Commands - Remote Repositories**

	git remote add origin <https://address/to/your/git/repo.git>	-	creates a link to remote repository; origin is a nickname for the remote repository
	git push														-	copy changes from local repository and push to remote repository
	
		
*****
Examples
--------

	$ git diff some-awesome-code.py
	$ git diff 8b5fe2 some-awesome-code.py
	
	$ git checkout a01d24 some-awesome-code.py
	$ git commit -m "back to previous working version of code"

	$ git remote add origin https://github.com/jlant-usgs/nwispy.git
	$ git push origin master
	
*****
References
----------

* [GitHub]
* [Bitbucket]
* [Git Basics - Working with Remotes]
* [Git Tutorials - Remote Repositories]

[GitHub]:https://github.com/
[Bitbucket]:https://https://bitbucket.org/
[Git Basics - Working with Remotes]:http://git-scm.com/book/en/Git-Basics-Working-with-Remotes
[Git Tutorials - Remote Repositories]:https://www.atlassian.com/git/tutorial/remote-repositories
