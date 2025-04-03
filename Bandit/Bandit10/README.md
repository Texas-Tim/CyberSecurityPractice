# Bandit Level 10

### Level Goal
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

### Commands you may need to solve this level
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

### Step by Step Walkthrough:
This was tricky, requiring you to parse through unreadable data for random bits of strings. Luckily, there is a command that will grab all the strings in a binary or data file called "strings". The final command is: 

```cat data.txt | strings | grep ===```


* UserName: bandit10
* pwd: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey