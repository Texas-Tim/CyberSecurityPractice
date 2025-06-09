**Challenge:** Wave a flag

**Level:** Easy

**Challenge Author:** syreal

### Description: 
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

### Step-by-Step Walkthrough:
It's always funny how many ways there are to solve a challenge. I opened up the `warm` file in a text editor and used `ctr-f` to find the flag pretty quick. Let's run through what the challenge intends for you to do though

#### Investigation - executing a program
To execute a program in Linux, use the terminal and type:

`./<program>`

Replace `program` with the name of your executable file (for example, ./warm). 

The program will return with

`bash: ./warm: Permission denied`

What's going on? You can try running with sudo, but you'll run into the same issue. Permissions can be global, or they can be on individual files. Use the following command to check permissions of individual files

`ls -l <filename>`

Executing this on the program `warm`, we get:

`-rw-r--r-- 1 <user> <user> 10936 <date> warm`

#### Learning - file permissions breakdown

The string `-rw-r--r--` represents the file permissions in Linux. Here’s what each section means:
```
-rw-r--r--
│ │  │  │
│ │  │  └─ Other users' permissions
│ │  └──── Group's permissions
│ └─────── Owner's permissions
└───────── File type
```

Breakdown:

File type (first character):
```
'-' : Regular file
'd' : Directory
'l' : Symbolic link
```

Owner permissions (next 3 characters):
```
'r' : Read
'w' : Write
'-' : No execute
```

Group permissions (next 3 characters):
```
'r' : Read
'-' : No write
'-' : No execute
```

Other (world) permissions (last 3 characters):
```
'r' : Read
'-' : No write
'-' : No execute
```

Summary:
* The owner can read and write.
* The group can only read.
* Others can only read.

In other words, the file does not grant permissions for anyone to execute it. We need to change this to let the file be executable!

#### Action - changing file permissions
Changing file permissions requires using the linux command `chmod`

chmod is a command-line utility in Unix/Linux used to change the permissions of files or directories. It stands for "change mode." With chmod, you can set who can read, write, or execute a file.

Example:
```
chmod +x filename   # Adds execute permission
chmod 755 filename  # Sets permissions to rwxr-xr-x
```

To change the file permissions for the `warm` file, run the following command

`chmod +x warm`

Then run:

`./warm`

Finally, the program successfully executes. The program asks you to add a flag, so run it again with the help flag and obtain your reward.

<details><summary>Flag</summary>
    <pre>
    picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
    </pre>
   </details>