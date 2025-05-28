# Bandit Level 18

### Level Goal
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

### Commands you may need to solve this level
> cat, grep, ls, diff


### Step by Step Walkthrough:
This one is very simple, introducing you to the "diff" command. Just compare the two files, and grab the changed value.
Final command: ```diff passwords.old passwords.new```


* UserName: bandit18

<details><summary>Flag</summary>
    <pre>
    pwd: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
    </pre>
   </details>