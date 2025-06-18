**Challenge:** hash-only-2

**Level:** Medium

**Challenge Author:** Junias Bonou

### Description: 
Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!

### Step-by-Step Walkthrough:
We are immediately asked to connect to an instance and run a binary. There is a v1 of this challenge, but I ran this first as it came up before v1. The biggest difference it seems is that in v1, you're allowed to `scp` the binary file, which may have some insight to the challenge

#### Investigation - Finding the binary
Logging in to the instance, I immediately made an assumption that the challenge was broken. Running `ls -a` showed nothing of value, so where is the promised binary? 

Let's see what happens if we just type `flaghasher`

ahHa! We received our hash, and it even indicates that it's encrypted with `MD5`. We learned the following information

1. Hash value: `b5953e013f83240dab571e2bf2c21f5d`
2. Flag location: `/root/flag.txt`
3. Encryption variation: `MD5`

#### Investigation - binary exploit?
Similar to `hash-only-1`, we can try to get some information dumps. However, the only one that we really need to do is confirm that our script has the same vulnerability. But, we don't know where it's located. As we learned about `PATH` in the last challenge, we need to learn a little more about `bin` for this challenge 

#### Learning - bin
bin is short for binary and commonly refers to a directory (like /bin or /usr/bin) on Unix/Linux systems that contains executable binary files (programs and commands). These directories store essential system programs and utilities that users and the system can run.

#### Investigation - finding flaghasher
We don't have permissions to use `cd`, but we do have permissions to use `ls` and `find`. We can use these to explore our server. Let's start by using `ls /bin`

No luck! At this point, I didn't want to search every directory, so after a bit of trial and error I used `find /usr -name "flaghasher"`, which quickly identified the directory

`/usr/local/bin/flaghasher`

voila! Now I can target the script. Use:

`strings /usr/local/bin/flaghasher`

and there it is! Looks like they didn't fix the vulnerability from last time, so let's try creating our vulnerability package again

Oops, running any sort of redirect seems to hit an error.

`echo '#!/bin/bash' > md5sum` results in `-rbash: md5sum: restricted: cannot redirect output`

So it looks like they added additional security after all! Let's see if we can crack it and force the file md5sum to be created.

##### Note: hint
<details><summary>Flag</summary>
    <pre>
    I spend a lot of time in this walkthrough going down false paths before understanding what the issue really is. If you want to skip a lot of these ramblings and testing, go to `Investigation - rbash to bash` near the end.
    </pre>
   </details>


#### Investigation - creating the malicious file

creating the file is simple, however, within the file, we need to add in our script:

```
#!/bin/bash
/bin/sh
```

After a bit of googling options, most of my other options, such as `printf`, `cat`, `nano`, and `vi` were not viable either, with similar redirect warnings, or just weren't installed commands (I tried installing, but I don't have the required permissions for that either).

However, it's worth noting that `echo` and the other commands did work, so they weren't directly blocked. I found a method to append text using `dd`. Let's remind ourselves what dd is for.

#### Learning - dd
dd is a Unix/Linux command-line utility used to copy and convert raw data from one location to another. It can read and write data at the byte or block level, making it useful for tasks like creating disk images, cloning drives, backing up partitions, and writing ISO files to USB drives.

Example usage:

`dd if=/dev/sda of=backup.img bs=4M`

* if= specifies the input file or device.
* of= specifies the output file or device.
* bs= sets the block size for reading and writing.

dd is a powerful tool for low-level data copying and manipulation.

#### Investigation - Creating md5sum
It seems that `dd` commands can go through because of the level it's writing at. We can use this to write to our file. Use the following commands to create and append to our file:

1. `touch md5sum`
2. `echo '#!/bin/bash' | dd of=md5sum oflag=append conv=notrunc`
3. `echo '/bin/sh' | dd of=md5sum oflag=append conv=notrunc`

where:
* `of=filename` specifies the output file.
* `oflag=append` tells dd to append to the file.
* `conv=notrunc` prevents truncating the file.

This script will replace `md5sum` and instead drop us into a root shell. Now lets give our file executable permissions:

`chmod +x md5sum`

Next, prepend the directory with your file to PATH. The current directory is `.`:

`export PATH=.:$PATH`

And we've run into the next hurdle, we receive a message: `-rbash: PATH: readonly variable`

#### Investigation - working around readonly
I identified the physical location of PATH in `/etc/environment`, but it was write protected even for `dd`. This isn't working, as we're simply too locked down from a permissions perspective. We need a different `shell` to work out of.

#### Learning - shells
A shell is a program that provides a command-line interface for users to interact with the operating system. It allows you to enter commands, run scripts, manage files, and control processes. Common shells include `bash`, `zsh`, and `sh`.

* `sh (the Bourne Shell)`
One of the original Unix command-line shells and scripting languages. It provides a command-line interface for running commands and writing shell scripts. Many modern shells, like `bash` and `zsh`, are based on or compatible with `sh`. On most systems, `sh` is a symbolic link to another shell (often `bash` or `dash`) for compatibility.

* `Bash (Bourne Again SHell)`
A widely used command-line shell and scripting language for Unix and Linux systems. It allows users to interact with the operating system by typing commands, running scripts, automating tasks, and managing files and processes. `Bash` is the default shell on most Linux distributions.

* `zsh (Z Shell)`
A powerful Unix/Linux command-line shell and scripting language, similar to Bash but with more advanced features. It offers improved tab completion, better customization, powerful scripting capabilities, and many user-friendly enhancements. `zsh` is popular among developers and is the default shell on macOS since Catalina.

To see what `shell` we are in, we can use the command: `echo $SHELL`

We are using `rbash`! Before I had looked into shells, I didn't realize that this was the source of our issues. But looking back, I can see that `rbash` was clearly stated as the root cause. I would say that we wasted all that time, but we learned a lot, including more about `shells`!

# Investigation - rbash to bash
rbash (restricted Bash) is a restricted version of the Bash shell. It limits the user’s ability to perform certain actions, such as changing directories, modifying environment variables, redirecting output, or running programs using absolute or relative paths. rbash is often used to provide a more controlled or secure shell environment, especially in restricted user accounts or CTF challenges.

This is the source of all of our issues! Let's see if they also protect from switching `shells`. Just type in `bash` or `sh` (`bash` is much better)

And it works! We are able to switch to a shell that is less protected and now we can edit the `PATH` without issues. Simply run through the exercise, drop into `root` and grab the flag! 

<details><summary>Flag</summary>
    <pre>
    picoCTF{Co-@utH0r_Of_Sy5tem_b!n@riEs_5547c7aa}
    </pre>
   </details>