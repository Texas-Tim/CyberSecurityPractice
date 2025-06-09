**Challenge:** Glitch Cat

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Our flag printing service has started glitching!

### Step-by-Step Walkthrough:
We're provided with an instance, and once we connect with `netcat`, a bunch of gibberish is printed on the screen. However, it's in a very familiar format.

`'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'`

the chr() is a character output function common to unicode

#### What is unicode?
Unicode is a universal character encoding standard that assigns a unique number (a code point) to every character in every language, including alphabets, symbols, and ideographs. It ensures that computers can correctly display and manipulate text from various languages, enabling global communication and data exchange. 

The inside is also clearly hex. So use your favorite converter, or preferably just copy the entire thing into a python shell, I use [ipython](https://ipython.readthedocs.io/en/stable/install/index.html). Voila! You got your flag



<details><summary>Flag</summary>
    <pre>
    picoCTF{gl17ch_m3_n07_a4392d2e}
    </pre>
   </details>