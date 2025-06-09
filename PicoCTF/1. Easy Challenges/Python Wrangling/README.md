**Challenge:** Python Wrangling

**Level:** Easy

**Challenge Author:** syreal

### Description: 
Python scripts are invoked kind of like programs in the Terminal... Can you run `ende.py` using this `pw.txt` to get the flag located in `flag.txt.en`?

### Step-by-Step Walkthrough:
Before we do anything, let's look at the files. 

#### Investigation
`flag.txt` looks encrypted

`pw.txt` is random gibberish, but a password can be anything

`ende.py` is easier run first then observed. Let's run it using

`python ende.py`

It returns a message that says

`Usage: ende.py (-e/-d) [file]`

adding in a -h flag, we get additional information

```
Usage: ende.py (-e/-d) [file]
Examples:
  To decrypt a file named 'pole.txt', do: '$ python ende.py -d pole.txt'
```

Note: within the python script is a method `sys.argv[<index>]` which reads in user arguments. These are passed when the file is run as seen in the example above

#### Action - running a python program
Let's run the program exactly as the message described. Since we are decrypting the flag, we'll need to pass in `-d`:

`python ende.py -d flag.txt.en dbd1bea4dbd1bea4dbd1bea4dbd1bea4`

providing the password as another argument is optional, as the terminal prompts you for the password if you didn't. Either way, grab your prize!


<details><summary>Flag</summary>
    <pre>
    picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
    </pre>
   </details>