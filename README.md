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
The purpose of Git is to manage a project, or a set of files, as they change over time. Git stores this information in a data structure called a repository. A git repository contains, among other things, the following: A set of commit objects. A set of references to commit objects, called heads. We will be using GitHub Classrooms to manage the submission of assignments in the course. You'll need a github account to proceed.

We're first going to connect github to your login terminal. This involves creating a public and private key pair. This key pair helps to encrypt information that ensures data is protected during transmission. Private Key and public key are a part of encryption that encodes the information. Essentially, we create this key pair and keep the private key on our server and hand off the public key to Github.

To start, create the keypair with the following command:
```
(cmscm13600-env) skr@linux2:~$ ssh-keygen -t ed25519 -C "<your github email address>"
```
Then, on the following prompts just hit enter.
```
> Enter a file in which to save the key (/Users/you/.ssh/id_algorithm): [Press enter]
> Enter passphrase (empty for no passphrase): [Press enter]
> Enter same passphrase again: [Press enter]
```
Finally, run the following command to print out your public key:
```
(cmscm13600-env) skr@linux2:~$ cat .ssh/id_ed25519.pub 
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMoPWw4adUWGKnBoEYcPxXRNW08P0vfvjZINPWrHDybz name@example.com
```
You should copy everything starting from `ssh-ed25519` and ending with your email to your clipboard.

Go to [github.com] and click on your profile in the upper right hand corner. Then, click on settings. In the left column, you will see a menu that has a link "SSH and GPG Keys". Enter that menu item and add a new SSH key. Title the key CMSC 13600 and paste the data from your public key that you got above into the text area underneath the title.
You can test that all of this works by running the following command:
```
(cmscm13600-env) skr@linux2:~$ ssh -T git@github.com
The authenticity of host 'github.com (140.82.112.3)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com,140.82.112.3' (ECDSA) to the list of known hosts.
Hi sjyk! You've successfully authenticated, but GitHub does not provide shell access.
```

## GitHub Classrooms: TODO 4
Now, that we have eveerything ready, it is time to begin your first assignment.
Each assignment will have a unique link. For example, this assignment will have a link:
[https://classroom.github.com/a/AreoZqCa]
Open that link with your web browser. 
You'll be given a dropdown list with a list of CNET ids, please select yours and "accept" the assignment. 
This will create a pre-populated repository for you with the assignment details.
Once the repository is created, you will get a link that looks something like this:
```
https://github.com/CMSC-13600-Data-Engineering/homework-0-getting-started-<your github name>
```
Every student in the class has such a git repository (a place where you can store completed assignments). You can visit this repository from a web browser to see what is in it and explore it with an interface, or you can access it from any terminal using
```
https://github.com/CMSC-13600-Data-Engineering/homework-0-getting-started-<your github name>.git
```

We'll walk you through that process now. The first thing that we will do is to `clone` this repository to linux.cs.uchicago.edu. *Note* Every year students cut an paste the following instructions without realizing that my CNET id is "skr" and my github username is "sjyk". Please replace those with your own.
```
(cmscm13600-env) skr@linux2:~$ git clone git@github.com:CMSC-13600-Data-Engineering/homework-0-getting-started-sjyk.git
```
To confirm, everything worked you can run the following command ``ls`` which prints out the files and folders in your current directory:
```
(cmscm13600-env) skr@linux2:~$ ls
cs  homework-0-getting-started-sjyk  html  schematext.sql
```
You should see a new folder with the appropriate title. You can enter this folder with the following command:
```
(cmscm13600-env) skr@linux2:~$ cd homework-0-getting-started-sjyk/
```
In this folder, you'll see four files:
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ ls
README.md	stocks.dat	hw0.py  autograder.py
```

## Setting Up Your Development Environment: TODO 5
Now, we're going to start programming (not really...) but we want you to get familar with writing code and testing code. There are a number of options you can use, we want you to pick a strategy that works for you and your comfort level.

* Option 1. Use a terminal-based text editor. The simplest thing to do is to use a terminal based text editor. For example, I could use the `nano` program to create or edit an existing text file.
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ nano <filename>
```
A tutorial is available here [https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/]. This approach is great if you are mostly familar with a linux command line already. It also takes the least effort to setup. 

* Option 2. Edit locally and upload to test. Another option, is to use CyberDuck [https://cyberduck.io/download/] to sync files from your machine to linux.cs.uchicago.edu. Open a new connection with CyberDuck, select "SFTP", and type in linux.cs.uchicago.edu as the URL. Then, you'll have to enter your CNET username and password. Once you successfully login, you'll be able to see a list of files and folders on the remote server. I like to use the "synchronize" feature to keep the remote folder updated with everything I have locally [https://docs.cyberduck.io/cyberduck/sync/]. This option allows you to use your own text editor to program.

* Option 3. A Remote IDE. Finally, it is possible to use PyCharm to directly connect to a remote server [https://www.jetbrains.com/help/pycharm/remote-development-a.html] This is an advanced option (but probably the easiest to use once set up). We won't really go through this.

* Option 4. Of course you are all free to program locally on your own laptops. Again, we'll standardize our instructions towards using linux.cs.uchicago.edu but you guys can figure out how to make those work on your own machines.

## Writing and Submitting Code: TODO 6
We'll start off with a simple Python scripting task to test everything out. The first step of this assignment is to install the `pandas` library.
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ conda install pandas
```

### Assignment Objective
In your homework folder, there is a file called `stocks.dat`. Each line of the file looks like this:
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ head stocks.dat 
A - Agilent Technologies
AA - Alcoa
AAC - Ares Acquisition
AACE - Alexandria Agtech/Climate Innovation
AACG - ATA Creativity Global
AACO - Advancit Acquisition I
AACP - Aeon Acquisition
AACQ - Artius Acquisition
AAIC - Arlington Asset Investment
AAL - American Airlines
```
It has a ticker symbol, a dash, and a name. 

Your job is to convert this file into a CSV file. A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields. Your final CSV file will have two columns 'Ticker' and 'Name'.  

### Parsing `stocks.dat`
In your first todo, you will fill in the `read_file` function in `hw0.py`. 
```
"""
!!!TODO!!!
"""
def read_file(filename):
	'''Input: filename (location of stock.dat)
	   Output: a list of tuples (ticker, name)
	'''
	return None
```
You will write a function that reads the file at the location `filename` and returns a list of tuples of the ticker symbol and the company name. Pay careful attention to how the strings are formatted in terms of leading and trailing spaces.

### Creating a CSV File
In your second todo, you will fill in the `write_csv` function in `hw0.py`. 
```
"""
!!!TODO!!!
"""
def write_csv(parsed, outfile):
	'''Input: a list of tuples (ticker,name), output location
	   Output: None/Void, writes a file
	'''
	return None
```
You will use the `pandas` library to write the CSV file with `to_csv` function. If you are not familiar with Python yet, it is your responsibility to do independent study to figure out how all the pieces fit together. Here are the rough steps you need to do.
* Create a `pandas` with two columns `ticker` and `name` and populate it with the data that you just parsed.
* Set the index of this dataframe to be `ticker`.
* Write this DataFrame to a csv file (location specified by `outfile`).

### Testing and Submission
To test your code, you can run the autograder.
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ python autograder.py 
Test (1/3) read_file, passed= True
Test (2/3) write_csv, passed= True
Test (3/3) write_csv, passed= True
```
You should see three passed tests, which is a good indication you've done everything right. If you fail a test, there should be a helpful error message. To submit your code, simply run the following steps:
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ git add hw0.py
```
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ git commit -m 'my first submission'
```
```
(cmscm13600-env) skr@linux2:~/homework-0-getting-started-sjyk$ git push
```
We will NOT grade any code that is not added, committed, and pushed to your submission repository. You can confirm your submission by visiting the web interface. You can commit and push as many times as you want
