# Bandit Level 14

### Level Goal
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

### Commands you may need to solve this level
> ssh, telnet, nc, openssl, s_client, nmap

### Helpful Reading Material
- SSH/OpenSSH/Keys

### Step by Step Walkthrough:
The challenge here shifts a little bit away from compression to RSA keys, ie public and private keys. The challenge page explains exactly what you need to do. Pass the key automatically while SSHing into the next level. No password required to access. Once you're in, locate the password in 

> /etc/bandit_pass/bandit14 

which you will need for the next level.

Final command: 
```ssh bandit.labs.overthewire.org -p 2220 -l bandit14 -i sshkey.private```

* UserName: bandit14

<details><summary>Flag</summary>
    <pre>
    pwd: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
    </pre>
   </details>