# Bandit Level 24

### Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

### Commands you may need to solve this level
> chmod, cron, crontab, crontab(5) (use “man 5 crontab” to access this)

### Step by Step Walkthrough:
The initial steps are very similar to level 22 and 23. Head to the same location as the previous level and look at the cronjob being executed on startup. However, the puzzle warns you that you will need to create a shell-script. I believe we'll need ```#!/bin/bash``` (I was able to figure out about 80% on my own). 

Looking at the shell script that is being run regularly, and breaking it down line by line, we see the following

```#!/bin/bash``` - This line tells the system it's a shell script and is necessary for any shell commands

```myname=$(whoami)``` - console command to assign a shell variable (it will be bandit24 in the script and bandit23 if you run it on your own)

```for i in * .*;``` - The use of "*" and "." in here is making use of wildcards. This essentially will tell the command to find any and all files and assign it the variable "i"

```owner="$(stat --format "%U" ./$i)"``` - assign the variable "owner" the assigned owner of the current file

```if [ "${owner}" = "bandit23" ]; then``` - only perform the next line if the owner of the file is "bandit23"

```timeout -s 9 60 ./$i``` - run the file, if it takes longer than 60s, kill the process

```rm -f ./$i``` - remove the file from existence

Thus, it's fairly simple what we have to do. Knowing that any file that is run will be bandit24, we can take advantage of those permissions to identify the password in ```/etc/bandit_pass/bandit24``` (the location of all passwords in the bandit challenges)

For the sake of continuity, its simplest to create a temporary directory and work from there: ```mktemp -d```. For me that is ```/tmp/tmp.vAnZqOdKw9``` (although temp folders are removed periodically)

Move to the temp folder and make two files: ```touch pword.sh``` and ```touch bandit24_pword.txt```

change the permissions of the two files you just created and the temp folder, to allow access from any user to read, write and access as needed: ```chmod +rx pword.sh```, ```chmod +rwx bandit24_pword.txt```, ```chmod 777 /tmp/tmp.vAnZqOdKw9```

add the necessary script to copy the password from the appropriate bandit_pass file: 

```
#!/bin/bash 
cat /etc/bandit_pass/bandit24 > /tmp/tmp.vAnZqOdKw9/bandit24_pword.txt
```

Copy the ```pword.sh``` file to the location that runs the scripts. Since the file is constantly deleted, this is why we are working from our temp directory location: 
```cp pword.sh /var/spool/bandit24/foo```

Wait up to a minute and check your file: ```cat bandit24_pword.txt```

If done correctly, you should see the password for bandit24!

#### Notes: 
The file permissions are what I still struggle with. I was able to understand the assignment, but could not figure out why the script wasn't working. File permissions was where I got stuck and I looked up the answer. Eventually, I will have to nail down that aspect of programming! But I'm still happy with what I learned

#### Second Note: 
The permissions I added initially were not quite right, as the pword still never showed up. Changing the file permissions using "777" did the trick, but I will need to learn more at a later date


* UserName: bandit24
* pwd: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8