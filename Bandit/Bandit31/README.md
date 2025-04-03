# Bandit Level 31

### Level Goal
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.

### Commands you may need to solve this level
> git 

### Step by Step Walkthrough:
My previous snooping served me well. The packed-refs file in the .git showed a secret tag. Using ```git show <tag id>``` netted me the password in record time.

#### Intended solution: 
You're intended to check the tags in the repository. Tags are a way to mark specific points in the history of the repository. Although I'm not sure how you would know that tags are something you should check, it is the method to solve this puzzle. Use ```git tag``` to see the list of tags and ```git show secret``` to see the password, where "secret" is the name of the tag


* UserName: bandit31
* pwd: fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy