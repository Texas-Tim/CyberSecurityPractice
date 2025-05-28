# Bandit Level 33

### Level Goal
After all this git stuff, it’s time for another escape. Good luck!

### Commands you may need to solve this level
> sh, man

### Step by Step Walkthrough:
Logging in was odd as you're greeted with "Welcome to Uppercase Shell!". Indeed, every command you input, you see sh: 1: <uppercase whatever you put in>.

Since almost all Linux commands are lowercase, and the ones that aren't are blocked, you're not left with much to experiment with. A little playing around made me realize that anything beginning with "$" went through without an error, so we know that variables can work, but I still had no idea what to do and I had to look it up. 

The solution is to realize that "$0" has a reference to a shell, specifically "-bash" (just run echo $0 on your machine). 

Running this in the terminal breaks you out of your existing shell into regular bash. phew!.

#### Password:
There's not much here, and it's not entirely clear what you're supposed to do next, but if you check your permissions with either "ls -la" or "whoami", you'll realize you have elevated permissions! Thus, you can run "cat /etc/bandit_pass/bandit33" for the password.


* UserName: bandit33
<details><summary>Flag</summary>
    <pre>
    pwd: tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
    </pre>
   </details>


And that's it! Congratulations! We've beaten all 33 levels! So sad...On to the next adventure!