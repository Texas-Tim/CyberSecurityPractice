# Bandit Level 22

### Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

### Commands you may need to solve this level
> cron, crontab, crontab(5) (use “man 5 crontab” to access this)

### Step by Step Walkthrough:
Exploring the use of cronjobs, simply teaching you how to read and explore the directories related to cron

Final Command: 
1. cd to ```/etc/cron.d/``` and look at the cronjob associated with bandit22. This will give a hint as to where to look for the ```.sh``` file located in ```/usr/bin```. 
2. use the ```cat``` command on that file to see the password for level 22 (the file is tricky as its name is the same length as the typical password)


* UserName: bandit22
* pwd: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q