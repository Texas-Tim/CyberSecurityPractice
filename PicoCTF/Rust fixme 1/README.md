**Challenge:** Rust fixme 1

**Level:** Easy

**Challenge Author:** Taylor McCampbell

### Description: 
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!

### Step-by-Step Walkthrough:
Rust is not my first language, so this is a learning exercise for me. Obviously our first step is to download the source code and extract the `tar` file. Reviewing the `main.rs` file, let's start with the comments, which seem to be pretty generous in their guidance. (Running Rust is not as difficult as VS Code would have you believe. Just run ```cargo run``` in the root folder, the one with the .toml file! You may have to install cargo as a package manager)

1. Line 5:  How do we end statements in Rust?

I can infer from the other lines that we need to add a `;` to the end of this line. I'm going to add it before ever running the code. This one seems to be a gimme

2. Line 18: How do we return in rust?

```
ret; // How do we return in rust?
^^^ help: a local variable with a similar name exists: `res`
```

The "help" here isn't that useful, but a quick online search tells me that you return with the following

```return;```

Which clears up the message

3. Line 25: How do we print out a variable in the println function? 

```
---- formatting specifier missing
String::from_utf8_lossy(&decrypted_buffer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ argument never used
```

Which is simply telling us that the variable "decrypted_buffer" isn't being referenced. Again, taking the hint from the comment, we search for how to print variables in the println function and learn that variables are printed with the "{}", but we can also add a bit of text. So, I replaced the line above with

```
"Decrypted flag: {}",
```

The comma is very important! As the two lines are wrapped by the println function. 

#### Getting the Flag
Run the command ```cargo run``` again and we're done!

<details><summary>Flag</summary>
    <pre>
    picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}
    </pre>
   </details>