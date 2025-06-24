**Challenge:** hash-only-1

**Level:** Medium

**Challenge Author:** Junias Bonou

### Description: 
Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!

### Step-by-Step Walkthrough:
We are immediately asked to connect to an instance and run a binary. There is a v2 of this challenge

## Investigation - running the binary
Logging in to the instance, we see the `flaghasher` binary. Run it with `./flaghasher`

From the results, we learn the following information

1. Hash value: `cba918c000164f89fa4f30dbde448602`
2. Flag location: `/root/flag.txt`
3. Encryption variation: `MD5`

At this point, I played around with hashcat, but didn't get anywhere. Since MD5 doesn't have any known vulnerabilities, and Hashes are intended to be uncrackable, this means there's something I don't know and a new tool to introduce.

## Learning - PATH
The PATH environment variable in `Bash` (and other shells) is a list of directories that the shell searches when you enter a command. When you type a command (like `ls` or `python`), `Bash` looks through each directory listed in PATH (from left to right) to find an executable file with that name.

Example:

`echo $PATH`

might output:

`/usr/local/bin:/usr/bin:/bin:/home/user/bin`

If you type `ls`, `Bash` will look for `ls` in `/usr/local/bin`, then `/usr/bin`, then `/bin`, and so on, until it finds it.

## Investigation - Binary
Since we have access to the binary, let's explore that a little more. I ran a series of debugging and investigation commands I've learned recently from these challenges:

1. `objdump -d flaghasher | less` - gives us the equivalent of `Binary Ninja`, but unfortunately didn't give much I could use
2. `gdb flaghasher` then `disas main` ran through the main function of the binary, and gave interesting, but unusable information since we have no way (that I'm aware of) to effect the memory
3. `nm flaghasher` lists all the functions and confirms that `main` is likely the only interesting one
4. `strings, ltrace and strace` all provide some insight into a single command:

`system("/bin/bash -c 'md5sum /root/flag.txt'")`

This command indicates something interesting, that it's running `md5sum` as `bash`. This means that if we have permissions to put a file in the `PATH`, we can possibly run it prior to the actual call to `md5sum`. First, let's refresh on `bash`

## Learning - Bash
`Bash`, (Bourne Again SHell), is a widely used command-line shell and scripting language for Unix and Linux systems. It allows users to interact with the operating system by typing commands, running scripts, automating tasks, and managing files and processes. `Bash` is the default shell on most Linux distributions.

you can run `Bash` within a script. In fact, most shell scripts are `Bash` scripts! You can:

* Start a script with a shebang line to specify Bash: `#!/bin/bash`
* Call Bash explicitly within another script: `bash -c "echo Hello from Bash"`
* Run a Bash script from another script: `bash myscript.sh`

This allows you to execute `Bash` commands or scripts from within other scripts or programs.

## Learning - PATH Exploitation
PATH exploitation is a technique where an attacker takes advantage of how the shell uses the PATH environment variable to locate executables. If a program runs a command without specifying its full path (e.g., using `ls` instead of `/bin/ls`), and the attacker can modify the PATH, they can place a malicious executable with the same name earlier in the PATH. When the program runs the command, it executes the attacker’s version instead of the intended system command.

Example:

1. Attacker creates a fake `ls` script in `/tmp/fakebin`
2. Attacker sets `PATH=/tmp/fakebin:$PATH`
3. If a program runs `ls`, it will execute the fake script

PATH exploitation allows attackers to run their own code by tricking a program into using a malicious executable found earlier in the PATH.

## Action - PATH Exploitation
Let's take what we just learned, and attempt to set up our own `md5sum` executable. We are taking advantage of the `flaghasher` script permissions, which will call our fake executable with higher permissions than our own. Note that this is only possible, because the call to `md5sum` does not indicate the full path `/usr/bin/md5sum`, instead relying on the `PATH` shortcut.

While logged in to the instance, create a new file called `md5sum`

within the file, add in our script:

```
#!/bin/bash
/bin/sh
```

Give our file executable permissions:

`chmod +x md5sum`

This script will replace `md5sum` and instead drop us into a root shell.

Prepend the directory with your file to PATH. The current directory is `.`:

`export PATH=.:$PATH`

If successful, this will grant a root shell. Now let's run the flaghasher script again!

<details><summary>Flag</summary>
    <pre>
    picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_04d0aaff}
    </pre>
   </details>