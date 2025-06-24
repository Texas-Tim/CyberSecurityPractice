**Challenge:** fixme1.py

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Fix the syntax error in the Python script to print the flag.

### Step-by-Step Walkthrough:
finding a syntax error can be the most frustrating part of debugging, especially when you're learning the language. There are two methods I use to locate where and what the error is. Although this specific error is pretty simple, recognizing it often takes experience.

## Investigation - Debugging
1. IDE/Code Editor - These tools will have integrations for various common languages and often for some of the uncommon ones as well. They include line by line guidance on the what and where. If you're not using one of these, you'll want to learn how to before you go too much farther in coding. I prefer Visual Studio or VS Code when debugging
2. Run the script - Just running it will throw the error and tell you exactly what line has the earliest living error. Sometimes, you might even get a suggestion for how to fix them.

Run the code to see: `IndentationError: unexpected indent on line 20`

## Investigation - Edit the code
This error has the common mistake of incorrect use of spacing. Each language treats spacing slightly differently, and in Python, a space is indicative of a function or a wrapper of some kind. It means that whatever has the same spacing, belongs to whatever layer is above it. Once you remove the spacing, you break that layer.

In this specific case, the print function is acting as if there is a layer above it, but there is no indication of a working function or method. Instead, remove the spacing to allow the script to run without throwing an error


<details><summary>Flag</summary>
    <pre>
    picoCTF{1nd3nt1ty_cr1515_182342f7}
    </pre>
   </details>