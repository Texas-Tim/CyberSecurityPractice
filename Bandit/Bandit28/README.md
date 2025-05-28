# Bandit Level 28

### Level Goal
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.

### Commands you may need to solve this level
> git 

### Step by Step Walkthrough:
This is exploring the use of ssh to GitHub. You simply need to clone the repository provided you, ensuring you're adding the port connection. Create a temporary directory and clone the repository. Using ```cat``` on the README will net you the next password

Final Command: ```git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo```


* UserName: bandit28

<details><summary>Flag</summary>
    <pre>
    pwd: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
    </pre>
   </details>