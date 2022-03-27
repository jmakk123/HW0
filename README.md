# Your First Assignment
The first assignment will walk you through the basics of version control, file manipulation, and some Python programming. 

Due Date: *Monday April 4, 2021 11:59 pm*

## Terminal Access: TODO 1
All of the coding exercises in this class with use Python 3 (NOT Python 2!!!). Python 3 is installed on all of the CSIL machines and you can install it on your own computer by downloading it here:
[https://www.python.org/download/releases/3.0/]

On your personal computer, you probably navigate your hard drive by double clicking on icons. While convenient for simple tasks, this approach is limited. For example, imagine that you want to delete all of the music files over 5 MB that you haven't listened to in over a year. This task is very hard to do with the standard double-click interface but is relatively simple using the terminal. All of the instructions in this class will assume access to a terminal interface whether windows, linux, or macos. 

It is your responsibility to get familiar with using your available terminal. I like using `linux.cs.uchicago.edu`, from my MacBook, I can open up the terminal application and type in:
```
$ ssh skr@linux.cs.uchicago.edu
```
This command will prompt me for a password and will open up a remote shell on the linux.cs server. If you have a PC, you can download the PuTTY application for opening a terminal: 
[https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html]
Follow the instructions for "simple password based login" here:
[https://www.lrz.de/services/compute/courses/x_lecturenotes/191007_PuTTY_Tutorial_2019.pdf]

*Note* We understand that you might be more comfortable using Jupyter notebooks for Python programming, but the point of this course is to introduce you to a more professional development environment where less of the software engineering details are taken care of for you. 

*Note* You can also do all your work locally (without SSH) if you would like, but it's your responsibility to translate the instructions in the assigment to match what you have on your own machine.

## Python Virtual Environment: TODO 2
Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface. This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run. The solution for this problem is to create a `conda` environment.

To create such an environment, run the following command in your terminal
```
skr@linux2:~$ conda create --name cmscm13600-env python=3.5
```
To activate this environment, run the following command:
```
skr@linux2:~$ conda activate cmscm13600-env
```
You'll see your prompt change into:
```
(cmscm13600-env) skr@linux2:~$
```
You'll have to run `conda activate` before every homework assignment!


## Git: TODO 3
The purpose of Git is to manage a project, or a set of files, as they change over time. Git stores this information in a data structure called a repository. A git repository contains, among other things, the following: A set of commit objects. A set of references to commit objects, called heads. 



Every student in the class has a git repository (a place where you can store completed assignments). This git repository can be accessed from:
[https://mit.cs.uchicago.edu/cmsc13600-spr-21/<your cnetid>.git]

The first thing to do is to open your terminal application, and ``clone`` this repository (NOTE replace < > with your CNET id!!!):
```
$ git clone https://mit.cs.uchicago.edu/cmsc13600-spr-21/<your cnet id>.git cmsc13600-submit
```
Your username and id is your CNET id and CNET password. This will create a new folder that is empty titled cmsc13600-submit. There is similarly a course repository where all of the homework materials will stored. Youshould clone this repository as well:
```
$ git clone https://mit.cs.uchicago.edu/skr/cmsc13600-public.git cmsc13600-materials 
```
This will create a new folder titled cmsc13600-materials. This folder will contain your homework assignments. Before you start an assingment you should sync your cloned repository with the online one:
```
$ cd cmsc13600-materials
$ git pull
```
Then, we will tell you which of the pulled materials to copy over to your repository (cmsc13600-submit). Typically, they will be self-contained in a single folder with an obvious title (like hw0). 

Try this out on your own! Copy the folder ``hw0`` to your newly cloned submission repository. Enter that repository from the command line and enter the copied ``hw0`` folder. There should be a single file in the folder called ``README.md``. Once you copy over files to your submission repository, you can work on them all you want. Once you are done, you need to add ALL OF THE FILES YOU WISH TO SUBMIT:
```
$ git add README.md 
```
After adding your files, to submit your code you must run:
```
$ git commit -m"My submission"
$ git push
```
We will NOT grade any code that is not added, committed, and pushed to your submission repository. You can confirm your submission by visiting the web interface[https://mit.cs.uchicago.edu/cmsc13600-spr-21/skr]
