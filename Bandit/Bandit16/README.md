# Bandit Level 16

### Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

### Commands you may need to solve this level
> ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, ss

### Helpful Reading Material
- Secure Socket Layer/Transport Layer Security on Wikipedia
- OpenSSL Cookbook - Testing with OpenSSL

### Step by Step Walkthrough:
Similar challenge to 15, but with a twist. instead of just connecting via a port, you need to connect with a secure ssl connection (ssl is outdated, but it's still an encrypted connection). "nc" isn't enough, now we need to use "ncat"

Final command: ```ncat localhost 30001 --ssl```

Alternative command: ```openssl s_client -connect localhost:30001```

* UserName: bandit16

<details><summary>Flag</summary>
    <pre>
    pwd: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
    </pre>
   </details>