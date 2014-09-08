Read measurements project - refactor with functions
===================================================

*****  
**Objectives:**  
  
1. Discuss collaborative meeting notes using TitanPad

2. Discuss markdown

3. Learn how to clone the scientific-computing-group repository on GitHub and
pull latest changes.

4. Refactor the read_measurements.py file in the “read measurements project”
with functions.


*****  
**Notes:**  
  
* [TitanPad] - a website where you can takes notes collaboratively with others

* [markdown] - a plain text formatting syntax that can be used to format readme files

    - popular on GitHub and Bitbucket
    - created by [John Gruber] and Aaron Swartz
    - [John Gruber] - “to write using an easy-to-read, easy-to-write plain text format, and         
    optionally convert it to structurally valid XHTML (or HTML)” 

* Get the repository: `git clone <github-site>`

* Get latest updates from the repository: `git pull -u origin master`
  
*****  
**Examples:**  
  
**markdown** - visit [Dillinger - markdown online editor]

**Clone the scientific computing group's repository**

    $ git clone https://github.com/jlant-usgs/scientific-computing-group.git
    $ git pull -u origin master


*****  
**Questions / Comments**  
  
**Q**: Can you use markdown in Python comments to generate pretty documentation?

**A**: Not markdown, but you can use [reStructuredText] in docstrings (triple quotes; """ """ or ''' ''').  Also, you can not use [markdown] or [reStructuredText] in comments (#), only [reStructuredText] in docstrings.

Most of Python's documentation is written in [reStructuredText]; [source]

[Sphinx] is the most popular documentation tool that can convert [reStructuredText] into many output formats including HTML; [source]

An nice extention to [Sphinx] is [numpydoc]. [numpydoc] allows you to write documentation is a nicer looking format than [reStructuredText].  Also, see [numpydoc - example]. 
  
Example docstring syntax using [numpydoc]: 
  
    def calc_volume_rectangular_solid(length, width, height):
    """ 
    Calculate the volume of a rectangular solid.
    
    Parameters
    ----------
    length : float
        Floating point length
    width : float
        Floating point width
    height : float
        Floating point height
    
    Returns
    -------
    volume : float
        Floating point volume

    """

    volume =  length * width * height
    
    return volume
    
 
*****  
**References:**  
  
* [TitanPad]

* [markdown]

* [markdown - John Gruber]

* [markable - markdown online editor]

* [Dillinger - markdown online editor]

* [reStructuredText]
 
* [Sphinx]

* [numpydoc]

* [numpydoc - example]

[TitanPad]:https://titanpad.com

[John Gruber]:http://daringfireball.net/projects/markdown/
  
[markdown]:http://en.wikipedia.org/wiki/Markdown
  
[markdown - John Gruber]:http://daringfireball.net/projects/markdown/
  
[markable - markdown online editor]:http://markable.in/editor/
  
[Dillinger - markdown online editor]:http://dillinger.io/
  
[reStructuredText]:http://docutils.sourceforge.net/docs/user/rst/quickref.html

[source]:http://docs.python-guide.org/en/latest/writing/documentation/

[Sphinx]:http://sphinx-doc.org/

[numpydoc]:https://pypi.python.org/pypi/numpydoc

[numpydoc - example]:http://codeandchaos.wordpress.com/2012/08/09/sphinx-and-numpydoc/
