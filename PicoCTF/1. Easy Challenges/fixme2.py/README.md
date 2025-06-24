**Challenge:** fixme2.py

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Fix the syntax error in the Python script to print the flag.

### Step-by-Step Walkthrough:
finding a syntax error can be the most frustrating part of debugging, especially when you're learning the language. There are two methods I use to locate where and what the error is. Although this specific error is pretty simple, recognizing it often takes experience.

## Investigation - Debugging
1. IDE/Code Editor - These tools will have integrations for various common languages and often for some of the uncommon ones as well. They include line by line guidance on the what and where. If you're not using one of these, you'll want to learn how to before you go too much farther in coding. I prefer Visual Studio or VS Code when debugging
2. Run the script - Just running it will throw the error and tell you exactly what line has the earliest living error. Sometimes, you might even get a suggestion for how to fix them.

Run the code to see: `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='? on line 22`

## Investigation - Edit the code
This error has the common mistake of using `=` instead of `==`. A single `=` is an assignment, assigning the value on the right to the variable `flag`. In previous versions of Python, I think this used to default as `True` (or maybe it was C++?) but I suppose this is no longer a valid syntax. Instead, it throws an error, which is better for everyone anyways.

To fix this error, the answer is to assign it to `flag == ""`, which is a equality comparison; comparing `flag` to what's on the right and executing if they are exactly the same. If not, it moves on to the `else` execution automatically.

As you can imagine, this code is extremely generous. It allows you to simply print the flag if you'd prefer, but the fix is not tedious so you might as well play along. Fix the code and grab your prize.

<details><summary>Flag</summary>
    <pre>
    picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}
    </pre>
   </details>