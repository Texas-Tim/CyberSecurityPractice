# Bandit Level 23

### Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

### Commands you may need to solve this level
> cron, crontab, crontab(5) (use “man 5 crontab” to access this)

### Step by Step Walkthrough:
The initial steps are very similar to level 22. Head to the same location as the previous level and look at the cronjob being executed on startup. It is performing an md5sum program on the text "I am user bandit22" and outputting to a file you don't have access to. 

However, using bash commands, you can simply copy to the CLI and perform the same operation to grab the file location, which you can then print out with "cat"

Final Command: Note that the command uses your current username, which is bandit22, we want bandit23, so just insert that username into the command to grab the cleverly hidden file location. 

1. ```mytarget=$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)```
2. ```cat /tmp/$mytarget```

* UserName: bandit23
* pwd: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga