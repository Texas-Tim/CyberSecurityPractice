**Challenge:** Guess My Cheese (Part 2)

**Level:** Medium

**Challenge Author:** aditin

### Description: 
The imposter was able to fool us last time, so we've strengthened our defenses!

netcat: `nc verbal-sleep.picoctf.net 51325`

### Step-by-Step Walkthrough:
This time, Dr. Lacktoes Inn Tolerant is up to our tricks. We can only guess the encrypted cheese and we don't have access to the cipher directly. There also seems to be some salt with it. But! We have our Rainbow table, so we have our 

## Learning - Rainbow Table
A rainbow table is a precomputed table used in cryptography for cracking password hashes. Passwords are typically stored in a database as hash values, which are essentially digital fingerprints of the original password. A hash function takes a password and converts it into a fixed-length string of characters, making it difficult to reverse engineer. 

Our "cheese list" is our list of passwords, and the encryption is `sha256` (as per the hint). We also know that the `salt` is only two "nibbles" long ie two bytes or two characters (also per the hints). Honestly, this is the first task that the hints were almost "necessary" as there are no other methods to "assume" these two facts, although the `sha256` algorithm may be able to be deduced. 

We can assume then, that we are working between `00` and `FF` which has 256 permutations, and use these as our salt when working with the cheese.

## Investigation - Inserting the Salt
We will need to be as thorough as we can think of and make few assumptions. For example, we don't know what position the `salt` will be when inserted into the "string" cheese (hah). We also don't know what format the salt will be in, nor what the final format of the string is before it gets encoded. In other words, "salting" allows for almost unlimited variations, and all this with just two `nibbles` of data! In order to crack this challenge, we have to assume that it's possible, thus we will avoid overly complicated checks and make "some" assumptions.

We will use the following as a baseline when writing our code.

1. Loop through all 256 permutations of two nibbles (0x00 to 0xFF)
2. For each cheese in the cheese list, iterate through all possible salt values (0x00 to 0xFF)
3. Iterate through all suggested encodings (`utf-8, utf-16-le, utf-16-be, latin-1, ascii`)
4. For each type of salt (`raw byte, hex string`), iterate again
4. For each cheese and salt combination, iterate through all possible string positions when inserting the salt
5. For each combination, compute the hash and check if it matches the target hash
6. If a match is found, print the cheese, salt, and hash and terminate the search
7. If no match is found after all iterations, print a message indicating that no match was found
8. Avoid errors where possible

I'm still making a lot of assumptions, but the code above allows some flexibility as it uses lists, making it simple to add additional parameters. Additional encodings for example, would be as simple as appending it to the list before running the code.

## Note - Some learning
I'll include my code, but I'd suggest trying to build your own first. It's not as difficult as it sounds. For me, the challenge lay in two parts, both with syntax implementation:
1. The `encoding` implementation was difficult and I kept getting strange outputs before hashing and the `hashlib.sha256()` object I was using didn't work as I expected; providing me a different output. I had to look up someone elses implementation to realize that instantiating the object prior to using `.hexdigest()` was changing things. I'm still not certain what is going on with that, but it was validating to know that the rest of my code was working as intended and I'm not just going crazy over salt. A bonus that I got the answer with only some syntax assistance! I also have another tool in my toolbelt for any future hashing needs
2. Getting the right values of `salt` and combining it correctly with the `cheese`. This took a lot of back and forth, testing and frustration. Additionally, it made me realize that I was just using two variations. There's potentially infinite variations of representing your `salt` and thus all the more reason why it's so effective!


<details><summary>Flag</summary>
    <pre>
    picoCTF{cHeEsY24ec2c20}
    </pre>
   </details>