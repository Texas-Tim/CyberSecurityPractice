**Challenge:** Let's Warm Up

**Level:** Easy

**Challenge Author:** Sanjay C/Danny Tunitis

### Description: 
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

### Step-by-Step Walkthrough:
Let's learn about hex and ASCII

#### Learning - Hexadecimal (hex)
Hexadecimal (often shortened to hex) is a base-16 number system that uses sixteen symbols: 0-9 for values zero to nine and A-F for values ten to fifteen. It is commonly used in computing to represent binary data in a more readable form, such as memory addresses, color codes, and encoded data.

Example:

* 15 is F in hexadecimal.
* 26 is 1A in hexadecimal.

#### Learning - ASCII
ASCII (American Standard Code for Information Interchange) is a character encoding standard that represents text in computers and electronic devices. It uses numeric codes (from 0 to 127) to represent English letters, digits, punctuation marks, and control characters. For example, the ASCII code for 'A' is 65, and for 'a' is 97.

#### Action
To convert from `hex` to `ASCII`, we can use the python command `chr()`.

`chr(0x70)`

This will provide the answer, just input it in the proper format and we have our flag!


<details><summary>Flag</summary>
    <pre>
    picoCTF{p}
    </pre>
   </details>