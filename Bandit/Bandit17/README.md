# Bandit Level 17

### Level Goal
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

### Commands you may need to solve this level
> ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, ss

### Helpful Reading Material
- Port scanner on Wikipedia

### Step by Step Walkthrough:



* UserName: bandit17
* pwd: 