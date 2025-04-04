**Challenge:** hashcrack

**Level:** Easy

**Challenge Author:** Nana Ama Atombo-Sackey

### Description: 
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

### Step-by-Step Walkthrough:
The challenge is pretty straightforward. It provides a webserver you can netcat into using the local webshell provided by PicoCTF. Once accessed, it provides a list of 3 hashes you have to crack, one at a time.

You can either input into a hash cracker, lots of free tools online are available, or you can learn how to use a tool yourself. I used "hashcat" with the dictionary "rockyou.txt"

- hash1: ```482c811da5d5b4bc6d497ffa98491e38```
- hash type: ```MD5```
- password: ```password123```
\n
- hash2: ```b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3```
- hash type: ```SHA-1```
- password: ```letmein```
\n
- hash3: ```916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745```
- hash type: ```SHA-256```
- password: ```qwerty098```
\n
* Flag: ```picoCTF{UseStr0nG_h@shEs_&PaSswDs!_dcd6135e}```