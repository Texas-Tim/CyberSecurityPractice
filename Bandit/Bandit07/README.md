# Bandit Level 7

### Level Goal
The password for the next level is stored somewhere on the server and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

### Commands you may need to solve this level
> ls , cd , cat , file , du , find , grep


### Step by Step Walkthrough:
I had to peruse the "find" manual a bit more to learn about filtering by users and gropus, but the main challenge was filtering out "Permissions denied" files. -readable and -executable did not work. Instead, I used a stdout trick to remove any files that returned the text I wanted to avoid. The final command was 

```find . -size 33c -user bandit7 -group "bandit6" 2>&1 | grep -v "Permission denied"``


* UserName: bandit7

<details><summary>Flag</summary>
    <pre>
    pwd: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
    </pre>
   </details>