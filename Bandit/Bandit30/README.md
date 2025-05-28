# Bandit Level 30

### Level Goal
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

Clone the repository and find the password for the next level.

### Commands you may need to solve this level
> git 

### Step by Step Walkthrough:
There are two ways to solve this one. Because I don't have a lot of experience with git commands, I did my usual thing of checking objects in the .git path. Apparently, branch commits are stored in the "packed-refs" file. 

Using ```git show <commit id>``` will share the readme file with you. This nets me the password

#### Intended Solution: 
The intended method is to actually switch to one of these commits using the ```git checkout``` command. However, you first need to identify the commit names. 

Do this with ```git branch -a``` 

Since dev stands for development, lets check that one first. Changing to this one and using ```cat``` on the README will net you the password


* UserName: bandit30

<details><summary>Flag</summary>
    <pre>
    pwd: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
    </pre>
   </details>