**Challenge:** perplexed

**Level:** Medium

**Challenge Author:** SkrubLawd

### Step-by-Step Walkthrough:
There are no hints and no description for this challenge. Just a provided binary file and a dream. The only thing we know is the challenge is tagged as a `reverse_engineering` challenge, so it's likely we'll be doing some code review. Let's use some of the techniques we've learned with previous challenges to print out what we can of the binary file and see what we know. 

### Note - Unsolved
I did not end up solving this solution. Even after looking up the answer, I didn't understand a lot of the binary investigation or what was going on. Most likely I will ask someone to walk me through this or find a different page specifically for binary reverse engineering

## Investigation - File Inspection

* Run the binary: `./perplexed`
Running the binary asks me for a password, I tried a few escape sequences but nothing in depth and didn't get any different input. Don't forget to change the permissions on the file to allow it to be executable!

* `strings`
`Strings` shows little additional information. I found a `main` function and a `check` function and some output for correct/incorrect password submissions

* `objdump`
Object Dump gives some memory insight into the functions. There are some interesting insights that stand out to me:
1. `strlen@plt` shares the length of the string. This call is made after the password input, and before the `check` function call. 
2. after checking the length, we have this piece: `cmp  $0x1b,%rax`. cmp subtracts the second operand (`0x1b` which is 27 bytes) from the first operand (%rax) and sets the CPU flags based on the result.




<details><summary>Flag</summary>
    <pre>
    
    </pre>
   </details>