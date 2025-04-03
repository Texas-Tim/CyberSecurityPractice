# Bandit Level 6

### Level Goal
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable

### Commands you may need to solve this level
> ls , cd , cat , file , du , find


### Step by Step Walkthrough:
This one finally takes a bit more work. You need to find a file that is: a. human-readable
b. 1033 bytes in size
c. not executable

After a bit of perusing, it looks like we need the help of the command "find". Use "man find" to learn more about the commands and how to narrow down our search. The command I used was ```find . ! -perm /111 -size 1033c```

#### Additional Notes: "
- ```! -perm /111"``` (not executable files)
- ```-readable``` (readable by current user)
- ```-size 1033c``` (find a file 1033 bytes in size with c indicating bytes) 

* UserName: bandit6
* pwd: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG