# Bandit Level 15

### Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

### Commands you may need to solve this level
> ssh, telnet, nc, openssl, s_client, nmap

### Helpful Reading Material
- How the Internet works in 5 minutes (YouTube) (Not completely accurate, but good enough for beginners)
- IP Addresses
- IP Address on Wikipedia
- Localhost on Wikipedia
- Ports
- Port (computer networking) on Wikipedia

### Step by Step Walkthrough:
This one gave me pause, as I was able to successfully utilize netcat, "nc", command to reach port 30000. But, since this was my first time, there was no feedback and I didn't realize I was connected. You're just met with an empty space as if the connection is pending. Simply submitting the password nets you the next pword.
Final command: 

```nc localhost 30000```


* UserName: bandit15

<details><summary>Flag</summary>
    <pre>
    pwd: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
    </pre>
   </details>