**Challenge:** First Find

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Unzip this archive and find the file named 'uber-secret.txt'

### Step-by-Step Walkthrough:
This challenge will require the use of a command to search quickly through all files and folders. Whenever using a search function, we have two options. 

1. grep
2. find

## Learning - Find, Grep
The main difference between `find` and `grep` is their purpose: `find` searches for files within a directory structure, while `grep` searches for patterns within the content of files. 

## Investigation - Find, Grep
We can actually use either of these, since within the file `uber-secret.txt` will have our flag with a known pattern, thus we can use grep. However, for the sake of the title in the challenge, lets find it with `find` instead.

our command should look like: `find . -name "uber-secret.txt"`

* `find` is the command
* `.` tells the command to search everything in the current directory
* `-name` indicates the string we are searching for

You'll note that you do not need a recursive flag since it is automatically a recursive command.

With this, we have our file, buried deep within a hidden folder. Run the following command: `cat <path_to_file>` to show the flag.

If you want to use grep, you can use this command: `grep -r "picoCTF" .`

<details><summary>Flag</summary>
    <pre>
    picoCTF{f1nd_15_f457_ab443fd1}
    </pre>
   </details>