# Bandit Level 2

### Level Goal
The password for the next level is stored in a file called - located in the home directory

### Commands you may need to solve this level
> ls , cd , cat , file , du , find

### Helpful Reading Material
- Google Search for “dashed filename”
- dvanced Bash-scripting Guide - Chapter 3 - Special Characters
### Step by Step Walkthrough:
a "-" named file refers to stdin/stdout or in other words, the computer is expecting additional arguments. To grab the pword, you must use something like "cat ./-" to include the entire filepath 


* UserName: bandit2

<details><summary>Flag</summary>
    <pre>
    pwd: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
    </pre>
   </details>