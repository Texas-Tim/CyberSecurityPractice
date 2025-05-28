# Bandit Level 20

### Level Goal
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

### Helpful Reading Material
- setuid on Wikipedia

### Step by Step Walkthrough:
Pivot to new concept again. This exercise is running a binary executable. I used "file bandit20-do" to identify the type of file I was working with. I noticed 

"ELF 32-bit LSB executable"

so I used that to google how to run that type of file. All you need to do to run an executable from the main line, is ```./<file>```. Running the command gives a hint into how I can use the file, it simply runs a command using the id of bandit20

Final command: ```./bandit20-do cat /etc/bandit_pass/bandit19```

#### Additional notes: 
At first, I thought it changed the userID of my profile, but it runs instead as an application with different privileges than I do. This shows the power and risk of applications that have greater permissions than you.


* UserName: bandit20

<details><summary>Flag</summary>
    <pre>
    pwd: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
    </pre>
   </details>