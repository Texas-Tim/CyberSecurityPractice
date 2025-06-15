**Challenge:** strings it

**Level:** Easy

**Challenge Author:** Sanjay C/Danny Tunitis

### Description: 
Using `netcat (nc)` is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at `port 41120` to get the flag?

### Step-by-Step Walkthrough:
This challenge is pretty straight forward

#### Learning - netcat (nc)
`netcat` (often abbreviated as `nc`) is a command-line networking utility used to read from and write to network connections using TCP or UDP. It is often called the "Swiss Army knife" of networking because it can be used for tasks such as:

* Connecting to remote servers (like a simple client)
* Listening for incoming connections (like a simple server)
* Transferring files between computers
* Port scanning
* Debugging and testing network services

Example usage:
`nc example.com 80`

This connects to example.com on port 80.

#### Action - connection
Let's connect to our website with netcat:

`nc jupiter.challenges.picoctf.org 41120`

Voila!

<details><summary>Flag</summary>
    <pre>
    picoCTF{nEtCat_Mast3ry_3214be47}
    </pre>
   </details>