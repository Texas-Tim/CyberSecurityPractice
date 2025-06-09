**Challenge:** Tab, Tab, Attack

**Level:** Easy

**Challenge Author:** syreal

### Description: 
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames:

### Step-by-Step Walkthrough:
This challenge is simply teaching you that using the `tab complete` when moving through directories can save you a lot of time. If there's a single directory, you can just type in `cd` and then `tab` to automatically fill in the rest. If there's multiple directories, you'll have to start typing the directory you want and then use `tab` to fill in the rest.

Finally, to make this challenge even easier, you don't have to navigate to each individual directory. If you just continue pressing tab, you can fill out the path automatically until there are no more directories.

#### Investigation - File
Once you get through all of the oddly named directories, you will be left with a file called

`fang-of-haynekhtnamet`

This is a binary file, and you can either open it in a text editor and find the flag, or use `grep` with the following command

`grep --text "picoCTF" fang-of-haynekhtnamet`

The command above will highlight the text you input, allowing you to quickly find the flag. Well done!

<details><summary>Flag</summary>
    <pre>
    picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}
    </pre>
   </details>