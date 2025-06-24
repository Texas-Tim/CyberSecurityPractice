**Challenge:** PW Crack 2

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Can you crack the password to get the flag?

### Step-by-Step Walkthrough:
This time the password is encoded, so download the files and run the python file with

`python level2.py`

we are greeted with a password prompt

## Investigation - code
The password checker will likely provide a hint here, looking at the code, we can see that the password is hard coded in the checker, but it's in a different format:

`chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)`

the chr() is a character output function common to unicode

## Learning - What is unicode?
Unicode is a universal character encoding standard that assigns a unique number (a code point) to every character in every language, including alphabets, symbols, and ideographs. It ensures that computers can correctly display and manipulate text from various languages, enabling global communication and data exchange. 

The internal characters are the standard format for hexadecimal, you can look up a map to convert them, use an online tool, or copy the code directly into a python shell. I use [ipython](https://ipython.readthedocs.io/en/stable/install/index.html)

Once you obtain the password, just run the `.py` file again and grab your well deserved flag!


<details><summary>Flag</summary>
    <pre>
    picoCTF{tr45h_51ng1ng_489dea9a}
    </pre>
   </details>