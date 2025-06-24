**Challenge:** Super SSH

**Level:** Easy

**Challenge Author:** Jeffery John

### Description: 
Using a Secure Shell (SSH) is going to be pretty important.

### Step-by-Step Walkthrough:
As the title and description implies, the challenge is to properly SSH into the host. 

## Investigation - SSH
Here's how to SSH into a host with a port identifier: `ssh -p 2222 user@host`

With the following inputs for my instance

port: `52836`
password: `6dd28e9b`
user: `ctf-player`
host: `titan.picoctf.net`

Replacing the above components, we get: `ssh -p 52836 ctf-player@titan.picoctf.net`

allow the connection and input the password, remembering that the password does not show keystrokes, and you should receive your flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{s3cur3_c0nn3ct10n_5d09a462}
    </pre>
   </details>