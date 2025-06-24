**Challenge:** interencdec

**Level:** Easy

**Challenge Author:** NGIRIMANA Schadrack

### Description: 

Can you get the real meaning from this file.

### Step-by-Step Walkthrough:

## Investigation - base64
To begin, let's take a look at the encoded file we were provided with. Obviously the message inside is encoded, and the `==` at the end provides us with a big clue. This pattern is indicative of `base64` encoding. So just find an online tool to start the decoding process.

Decoding the first bit provides us with another encoded message. Also in `base64`. Let's continue.

## Investigation - ROT
Now we're getting somewhere. The message looks to be in the correct format for the flag we need, but shifted. Let's use the standard `ROT` cipher. Rot stands for rotation, and is the basis for what's called a `caesar cipher`. We can either deduce the number of rotation steps, or put it into a decoder online to brute force the solution. We have our Flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{caesar_d3cr9pt3d_78250afc}
    </pre>
   </details>