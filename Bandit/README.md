# Bandit Overview
URL: https://overthewire.org/wargames/bandit/

### Description:

The Bandit wargame is aimed at absolute beginners. It will teach the basics needed to be able to play other wargames.

The way this challenge works, is you are searching for a password for the next level. Thus, to find the password for bandit1, you will log into bandit0, solve the puzzle, identify the password, then log into bandit1 before searching for the password for bandit2 and so on.

I have organized the structure of this walkthrough so that the readme for Bandit1 describes the steps to find the password for itself, ie. what to do when logged in to Bandit0. 

### Useful Commands

1. ssh bandit.labs.overthewire.org -p 2220 -l bandit<x> (-p specifies the port and -l the username)
2. mktemp -d (creates a temporary directory for you to use with random names. Periodically removed)

### Bandit Level 0
**Notes:** 
- Use the following command to log in: ```ssh bandit.labs.overthewire.org -p 2220 -l bandit0```

* UserName: bandit0
* pwd: bandit0


