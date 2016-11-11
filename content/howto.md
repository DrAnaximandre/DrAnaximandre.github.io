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

- [Spellcheck](https://www.sublimetext.com/docs/2/spell_checking.html)



Usual loop
==========

* do modifications
* check locally your modifications: `fab build` and `fab serve`, then [go there if you are running locally](http://localhost:8000)
* eventually, `git add <your-modifications>` and `git commit -m "i-changed-sources"` followed by `git push`. That should ensure that your sources are up-to-date.
* Still in source branch: `ghp-import -b master -m "i-changed-the-output" output`
* then `git push --all` (the all flag pushes the master branch even if you're working with source)
* prey but it should work.