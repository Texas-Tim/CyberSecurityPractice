# Bandit Level 17

### Level Goal
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

### Commands you may need to solve this level
> ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, ss

### Helpful Reading Material
- Port scanner on Wikipedia

### Step by Step Walkthrough:
Notes: I got lost a bit on this one, I kept thinking that ```ss``` was the command to use, but it's not. Use ```nmap``` to start scanning the port range provided with ```nmap -p 31000-32000 localhost```
- 31046/tcp open  
- 31518/tcp open  
- 31691/tcp open  
- 31790/tcp open  
- 31960/tcp open

Now that we have our open ports, we need to identify SSL/TLS. With only 5 ports, we can easily brute force this, but let's see if there's an option to identify SSL support easily. Looks like adding the flags ```--script ssl-cert``` will give us both the ports and the ones with SSL capability.

Thus, our final commands look like
1. ```nmap -p 31000-32000 localhost --script ssl-cert```
2. ```ncat localhost 31790 --ssl```

> kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

#### Additional Notes: 
This doesn't give us a pwd at all! But, this should look familiar. This is a private key, which we can use to ssh into the next level! This part isn't rocket science, so if you're not comfortable with SSH keys, don't stress. You simply need to create a file that ends in either ".pem" or ".private". I named mine "bandit17.pem", opened it with notepad (or you can use the CLI with "vi" or "nano") and copy the private key into your new file. Then pass it in like we learned earlier using the command "ssh bandit.labs.overthewire.org -p 2220 -l bandit17 -i <private_key>" 

It hurts a little that I don't have a pwd for Level17...(hint, look in the /etc/bandit_pass" directory for all pwds)


* UserName: bandit17
* pwd: EReVavePLFHtFlFsjn3hyzMlvSuSAcRD