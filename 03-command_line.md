# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

show current working directory path   =  Echo $PWD

creating a directory   = mkdir
deleting a directory   = rmdir
creating a file using touch command = touch test.py
deleting a file   =  rm test.py
renaming a file  = mv
listing hidden files = ls -a
copying a file from one directory to another cp dir1/file dir2

locating a file = locate
clearing the command line = clear
converting one markdown format to another = pandoc


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`     list files
`ls -a`  lists all files including hidden files
`ls -l`  long listing format
`ls -lh` long list/human readable 
`ls -lah`long list/all/human readable  
`ls -t`  sorted by modification time
`ls -Glp`Group information/long listing format  



---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-f - each name as a directory instead of as a file
-m - comma seperated list
-o - long list format, but without names
-x - displays files as rows
-1 - displays each entry as a line

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs is used to construct argument lists and invoke other utilities. It breaks the list of arguments into sublists small enough to be acceptable

find /path -type f -print | xargs rm

 

