Version Control - Git
=====================

*****
Objectives
----------

1. Push changes to a remote repository.
2. Pull changes from a remote repository.

*****
Notes
-----

**Git Commands**

	git remote add origin <https://address/to/your/git/repo.git>	-	creates a link to remote repository 
	git push origin master											-	copy changes from local repository (in master branch) and push to remote repository
	git pull origin master											-	copies changes from remote repository and pulls them to local repository
	
	
*****
Examples
--------

	$ git remote add origin https://github.com/jlant-usgs/nwispy.git
	$ git push origin master
	
	$ git pull origin master
	
	$ git clone https://github.com/jlant-usgs/nwispy.git
	
*****
References
----------

* [Git - push]
* [Git - pull]

[Git - push]:https://www.atlassian.com/git/tutorial/remote-repositories#!push
[Git - pull]:https://www.atlassian.com/git/tutorial/remote-repositories#!pull
