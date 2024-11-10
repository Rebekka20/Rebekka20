# Assignments 2

## Task 1:
**No. 1 - The Shell**
### Exercises
1. **Outputs the date and time**
```bash 
$ date
```
**Output:**
```bash
Mon Oct 29 12:34:56 UTC 2024
```
2. **Outputs the username of the currently logged-in use**
``` bash
$ whoami
```
**Output:**
```bash
Rebekka
```
### Ouiz: 

What should be outputted to the display when you type echo Hello World? 
- Hello World

---
**No.2 - pwd(Print Working Directory)**
### Exercises
**Outputs the complete path of the current directory you are in within the filesystem**

### Quiz: 

How do I find what directory you are currently in?
- pwd

---

**No. 3 - cd(Change Directory)**

**command to change the current directory**

### Exercises

1. Run the cd command without any flags, where does it take you?
-When you run the cd command without any flags or arguments, it takes you to your home directory.

### Quiz:

If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?
- cd ..

---

**No.4 - ls(List Directories)**
### Exercises
**The command *ls* is used in the command line to list files and directories in the current directory**

- ls -R: Lists all files and directories recursively.
- ls -r: Displays files in reverse order.
- ls -t: Sorts files by modification date, with the newest first.

### Quiz: 

What command would you use to see hidden files?
- ls -a

---

**No. 5 - touch**

**The touch command is used to create one or more files or to update their timestamps.**

### Exercises

- Create a new file:

``` bash
$ touch
```

**Output:**
```bash
NeueDatei
```

- Note the timestamp:

``` bash
$ ls -l NeueDatei.txt
```

- Touch the file and check the timestamp once again:

``` bash
$ touch NeueDatei.txt
```
### Quiz

How do you create a file called myfile?
- touch myfile

---

**No. 6 - file**
### Exercises

**To determine the file type, you can use the file command. It will provide a description of the file's contents.**

### Quiz

What command can you use to find the file type of a file? 
- file

---
**No. 7 - cat**
### Exercises

**Run cat on different files and directories. Then try to cat multiple files.**

The cat command is used to display the contents of files, combine multiple files, or quickly read text files.

### Quiz

What's a good way to see the contents of a file?
- cat

---
**No. 8 - less**
### Exercises

**Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.**

less allows you to read and navigate large text files in a clear and interactive way.

### Quiz

How do you quit out of a less command?
- q

---

**No. 9 - history** 
### Exercises

**Navigate through your previous command history with the Up and Down keys. Play around with ctrl-R reverse search.**

-With the up arrow key, you navigate to previous commands, and with the down arrow key, you navigate to more recent commands.

-With Ctrl-R, you search through previous commands.

### Quiz

What is the command to clear the terminal? 
- clear
*The clear command only clears the visible output in the terminal, meaning everything that has been displayed on the screen so far. The commands and their outputs are not actually deleted – they just disappear from the visible area. The command history remains intact and can still be accessed using the arrow keys or the history command.*

---

**No. 10 - cp(Copy)**
### Exercises

**Copy over a couple of files, be careful not to overwrite anything important.**

-I used the -i option to ensure nothing gets overwritten.

### Quiz

What flag do you need to specify to copy over a directory?
- r 

--- 

**No. 11 - mv(Move)**
### Exercises

**Rename a file, then move that file to a different directory.**

1. Rename a file:
``` bash 
mv alteDatei neueDatei
```
2. Move a file to another directory:

``` bash 
mv neueDatei /home/Rebekka/Documents
```

### Quiz

How do you rename a file called cat to dog?

- mv cat dog

--- 

**No. 12 - mkdir(Make Directory)**
### Exercises

**Make a couple of directories and move some files into that directory.**

Create directories: 

``` bash 
mkdir musik bilder
```
Move files into the directories:

``` bash 
mv song1.mp3 musik/
mv photo1.jpg bilder/
```

### Quiz

What command is use to make a directory?

- mkdir

---

**No.13 - rm(Remove)
### Exercises

1. **Create a file called -file (don't forget the dash!).**

``` bash 
touch ./-file
```

The command touch ./-file creates a file named -file in the current directory. The use of ./ ensures that the dash in the filename is not interpreted as a flag.

2. **Remove that file.**

``` bash 
rm ./-file
```

To remove the file.

### Quiz 

How do you remove a file called myfile? 

- rm myfile

---

**No. 14 - find**
### Exercises
Find a file from the root directory that has the word net in it.

``` bash 
$ find / -name net
```

**Output:**
```bash
/proc/net
```

### Quiz

What option should I specify for find if I want to search by name? 

- -name

--- 

**No. 15 -  help**
### Exercises

**Run help on the echo command, logout command and pwd command.**

- Echo without arguments, it simply produces no output ans echo with arguments, it outputs the text or arguments provided.

- The logout command logs you out of the current shell session.

- pwd shows the path of the current directory you are in.

### Quiz 

How do you get quick command line help for built-in bash commands? 

- help

---

**No. 16 - man**
### Exercises 

**Run the man command on the ls command.**

The man command (short for "manual") is used in Linux systems to display the manual pages for various commands, programs, or functions.
``` bash 
$ man ls
```
Displays the manual page for the ls command, which is used to list files and directories.

``` bash 
$ man ls
bash: man: command not found
```
The man command is not available in Git Bash.

### Quiz 

How do you see the manuals for a command? 

- man

--- 

**No. 17 - whatis**
### Exercises 

The whatis command provides a short description of a command or program, based on the first line of its manual page. It offers a concise summary without opening the entire manual page.

For example, whatis cat returns a description of the cat command.

**Run the whatis command on the less command.**

The whatis command is not available in Git Bash. 

The command whatis less typically returns the following description: 

``` bash 
$ whatis less
less (1)              - opposite of more
```

### Quiz 

What command can you use to see a small description of a command? 

- whatis

--- 

**No. 18 - alias**
### Exercises 

**Create a couple of aliases then remove them.**

``` bash
$ alias lala='ls'
```

Now it shows what would normally be displayed with ls.

``` bash
$ unalias lala
```
And this undoes it again.

### Quiz 

What command is used to make an alias?
- alias

--- 

**No. 19 - exit**
### Exercises 

**Exit out of the shell and see what happens. Make sure you don't need to do anymore work in that shell.**

The current work session will be closed, just like with logout. 

### Quiz 

How can you exit from the shell? 
- exit

--- 











