Title:  Reminder for me: how to do the setup and publish things.
Date: 2016-11-11
Category: Setup
Summary: Making a new setup on another computer is harsh.
Status: published

Useful links
============

- [The funding father](http://beneathdata.com/how-to/how-i-built-this-website/)
- [MD cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Tune your sublime
================

- Spell check : [Sublime's page](https://www.sublimetext.com/docs/2/spell_checking.html)
- Modify files over SSH: [rsubl](https://github.com/henrikpersson/rsub),[howto](https://wrgms.com/editing-files-remotely-via-ssh-on-sublimetext-3/)
 

Usual loop
==========

* do modifications
* check locally your modifications: `fab build` and `fab serve`, then [go there if you are running locally](http://localhost:8000)
* Once you're done modifying things, do `git add <your-modifications>` and `git commit -m "i-changed-sources"` followed by `git push`. That should ensure that your sources are up-to-date.
* No need to checkout to master: `ghp-import -b master -m "i-changed-the-output" output`
* then `git push --all` (the all flag pushes the master branch even if you're working with source)


What if it doesn't work?
========================

* Have you installed ghp-import ([via github](https://github.com/davisp/ghp-import), or `pip install ghp-import`))? 
* Check you are in a python 2.7 environment ([example with conda](http://conda.pydata.org/docs/py2or3.html#use-a-different-version-of-python))?