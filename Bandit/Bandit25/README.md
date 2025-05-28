# Bandit Level 25

### Level Goal
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time

### Step by Step Walkthrough:
This is one where I leaned heavily on a walkthrough, and I think it's important to understand the value of walkthroughs, vs struggling through it alone. In this case, I could quickly understand the syntax of the correct answer without trying to identify what I'm missing. What I learned:

1. ```for i in {0000..9999}``` - will loop through all the values in a 4 digit pincode. I can't imagine how long it would have taken me to identify this one trick alone
2. for loops work a little odd here, I can't just echo the submission using ```nc``` but I'm not certain why. 
3. Using a txt file will let me use ```cat``` to submit each line with a ```nl``` to simulate submission


* UserName: bandit25

<details><summary>Flag</summary>
    <pre>
    pwd: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
    </pre>
   </details>