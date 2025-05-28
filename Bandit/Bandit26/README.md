# Bandit Level 26

### Level Goal
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.

### Commands you may need to solve this level
> ssh, cat, more, vi, ls, id, pwd


### Step by Step Walkthrough:
I'll admit this is another one that completely stumped me. Even reading some of the online tutorials didn't clear it up for me. The initial steps are pretty simple. There is an RSA key sitting in the main directory. Okay, grab it, move it to my local computer, change permissions to avoid public key, and try to log in....Nope, immediately kicked out. What's going on?

#### Shell: 
A "shell" is a concept most of us don't have to worry about too much. As I understand it, the shell is what sets your experience for your cli access. A users default shell can be found in the ```/etc/passwd``` file. 

For bandit26, the shell they use is ```/usr/bin/showtext```. Note that for most users, the default is ```/bin/bash``` which is the traditional shell "bash".

#### Next: 
So, lets look at the ```/usr/bin/showtext``` shell, which is a bash script. Using ```cat``` you can see a specific line that looks out of place: ```more ~/text.txt```. Although we don't have access to this file, we can assume that this is the reason for us being kicked out.

#### more: 
the ```more``` command is simply a method to parse through a file, on its own it is quite simple. What is going on though, is that once the more command finishes, it's automatically exiting. This seems to be why we cannot stay logged in. So what we need to do is interrupt the command from finishing. 

What you need to do, is make your terminal window small enough that the more command output cannot simply fit on your screen, forcing it to go into a "discovery" mode. It's a little unorthodox, but real life doesn't fit typical puzzles either. So, we're learning I guess.

#### Password: 
Getting the password from here is relatively simple. Once you're in discovery mode for ```more``` press ```v``` which will open a "vi" session or "vim" session. This will allow you to interact with the console while within the ```more``` session. Within "vi", press ```:e``` which allows you to connect to the console, then grab the password for bandit26 just for fun. 

This doesn't solve the issue with the command running immediately upon connection, so we still need to do something about that shell...

#### Shell2: 
Now that you know how to connect via ```more``` we need to change our shell we're using. The command to open a new shell within "vi" is ```:shell```. using this command just takes us back to the ```more``` output, so we need to reset the shell variable. We can do this with ```:set shell=/bin/bash```. 

Run ```:shell``` once more, and you're in! This is the "fairly easy" method to correctly log in to level 26. Roll Eyes


* UserName: bandit26

<details><summary>Flag</summary>
    <pre>
    pwd: s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
    </pre>
   </details>