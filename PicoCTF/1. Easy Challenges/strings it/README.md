**Challenge:** strings it

**Level:** Easy

**Challenge Author:** Sanjay C/Danny Tunitis

### Description: 
Can you find the flag in file without running it?

### Step-by-Step Walkthrough:
Once again, a simple `ctr-f` command nets you the flag fairly easily. Nevertheless, let's try to do this challenge the intended way.

## Learning - strings command
The strings command in Unix/Linux extracts and displays printable text sequences from binary files. It is commonly used to find readable text, such as messages, file paths, or flags, hidden within executables or other non-text files.

## Investigation - strings
The file we obtained is called `strings`. This is a binary file. A binary file is a file that contains data in a format that is not plain text. Instead, it is made up of bytes that may represent compiled programs, images, audio, or other types of data. In the context of challenges like this, a binary file usually refers to a compiled executable program that you can run or analyze, but not read directly as text. Note that running this file will provide you a hint, but will not solve the challenge

given the title of the challenge, it's clear this is the method they want us to use. So let's extract the strings from the binary file, and then we'll use grep to quickly grab the flag:

`strings strings | grep "picoCTF"`

<details><summary>Flag</summary>
    <pre>
    picoCTF{5tRIng5_1T_7f766a23}
    </pre>
   </details>