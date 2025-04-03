# Bandit Level 9

### Level Goal
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

### Commands you may need to solve this level
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

### Helpful Reading Material
- Piping and Redirection

### Step by Step Walkthrough:
This required a bit of googling on the sort and uniq commands. "sort" is pretty straightforward, sorting each of the lines compared to each other. "uniq" is a little more nuanced, where it can parse only unique values, but only if the lines are next to each other. Thus, the final command is: 

```cat data.txt | sort | uniq -u```


* UserName: bandit9
* pwd: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM