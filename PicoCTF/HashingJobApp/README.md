**Challenge:** HashingJobApp

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
If you want to hash with the best, beat this test!

### Step-by-Step Walkthrough:
Upon running the instance, we netcat into it and are greeted with the following:

`Please md5 hash the text between quotes, excluding the quotes: '<string>'`

We need to perform an md5 hash of whatever string it asks you for. I was asked to hash the string: `Chinatown`

#### What is hashing?
Hashing is the process of converting data (like a string or file) into a fixed-size string of characters, usually using a mathematical algorithm called a hash function. The output, called a hash or digest, is unique to the input data. Hashing is commonly used for data integrity checks, password storage, and digital signatures because it is fast and difficult to reverse (one-way). Hashes are not meant to be reversed at all, so they are not good for passwords, but intended primarily for data integrity as mentioned. Common hash functions include MD5, SHA-1, and SHA-256, and for this challenge we will be using MD5

#### MD5Sum
You can read a little more about how to perform hashing in my [Cracking Tools](https://github.com/Texas-Tim/CyberSecurityPractice/tree/main/CrackingTools/Hashes) but instead of creating a file, we're going to use the `echo` function in linux cli. Run the following to get your hash:

`echo -n "<your string>" | md5sum`

* "echo" copies whatever you provide and prints it
* "-n" is the flag that tells echo not to include a new line as that would change the hash
* "<string>" - your string
* "|" tells linux to run whatever is next using the output of whatever was previous
* "md5sum" is the linux md5 hash function

Run through the exercise 3 times to grab the flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}
    </pre>
   </details>