**Challenge:** DISKO 1

**Level:** Easy

**Challenge Author:** Darkraicg492

### Description: 

Can you find the flag in this disk image?

### Step-by-Step Walkthrough:
I'm not entirely certain what you are expected to do in this challenge, but I'll walk through my learning and we can at least obtain the flag.

The problem provides us with a .dd file

#### what is a .dd file?
A .dd file is a raw disk image file created by the dd command on Unix/Linux systems. It is an exact, bit-for-bit copy of a storage device (such as a hard drive, USB stick, or partition). This type of file is often used in digital forensics and data recovery because it preserves all data, including deleted files and filesystem metadata.

.dd files are often parsed with the `strings` command, which is a cli command, and these types of commands often come with a manual. Using `man strings`, the description for the command reads: `strings - print the sequences of printable characters in files`. 

### Step 1
The first thing I noticed was how the file has various bits of data in it and strings all over the place coupled with corrupted data.

Just using `strings disko-1.dd` starts printing all the legible strings line by line. I quickly put a stop to that.

### Step 2
We need a method to grab a specific string. Since we already know the format of the data we are looking for, we can try to use `grep` to obtain what we need. I used the following command

`strings disko-1.dd | grep 'picoCTF{[^}]*}'`

Thankfully, this simple regex statement worked like a charm and we have the flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
    </pre>
   </details>