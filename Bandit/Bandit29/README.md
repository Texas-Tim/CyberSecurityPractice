# Bandit Level 29

### Level Goal
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

### Commands you may need to solve this level
> git 

### Step by Step Walkthrough:
This level is simply learning git commands and how to review previous commits. 

You start off the same as level 28, cloning the repository, but this time when you view the README, the password is replaced with hashes.

Final Command: 
1. ```git log``` to view previous commits
2. Use logic or just check all of the previous commits to view the password with the command ```git show <commit id>```


* UserName: bandit29
 
<details><summary>Flag</summary>
    <pre>
    pwd: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
    </pre>
   </details>