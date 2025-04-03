# Bandit Level 19

### Level Goal
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

### Commands you may need to solve this level
> ssh, ls, cat

### Step by Step Walkthrough:
This one is also deceptively simple. It automatically logs you out with a "bye bye!" message when using ssh to access the server. However, when connecting via ssh, you can still pass in commands if they have quotes. Add in the appropriate "cat" command to identify the pwd

Final command: ```ssh bandit.labs.overthewire.org -p 2220 -l bandit18 "cat readme```

Alternative command: ```ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash```

Alternative command2: ```ssh bandit18@bandit.labs.overthewire.org -p 2220 -t /bin/sh```

The alternative commands both work to create a bash shell or pseudo terminal respectively. These allow you to traverse the servers directories without needing to submit a command via ssh every time


* UserName: bandit19
* pwd: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8