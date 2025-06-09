**Challenge:** Big Zip

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Unzip this archive and find the flag.

### Step-by-Step Walkthrough:
This challenge will require the use of a command to search quickly through all files and folders. Whenever using a search function, we have two options. 

1. grep
2. find

The main difference between `find` and `grep` is their purpose: `find` searches for files within a directory structure, while `grep` searches for patterns within the content of files. 

Since our goal is to find a flag within a file, we want to use a grep command. However, we will need to add in a flag to ensure that it searches within all directories and subdirectories as well.

`grep -r "picoCTF" .`

grep is our command, -r stands for "recursive" which indicates we would like to search in all subdirectories, "picoCTF" is the search term, and "." tells the command to search all objects in the current directory. With this, we can quickly find the flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{gr3p_15_m4g1c_ef8790dc}
    </pre>
   </details>