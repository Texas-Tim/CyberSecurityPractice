# Bandit Level 21

### Level Goal
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

### Commands you may need to solve this level
> ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)

### Step by Step Walkthrough:
This one took some effort, and a lot of googling. I was unaware how simple it was to set up your own server to send messages. Once I understood the assignment, it just took some studying of netcat ```nc``` to set up a server to send messages automatically. 

Using a while statement, use nc in listening mode ```-l``` and set a port number ```-p``` to send a message to any connection on that port

Final command: ```while true; do echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 50000; done```


* UserName: bandit21
* pwd: EeoULMCra2q0dSkYj561DX7s1CpBuOBt