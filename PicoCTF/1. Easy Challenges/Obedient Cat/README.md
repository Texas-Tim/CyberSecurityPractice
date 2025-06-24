**Challenge:** Obedient Cat

**Level:** Easy

**Challenge Author:** syreal

### Description: 
This file has a flag in plain sight (aka "in-the-clear").

### Step-by-Step Walkthrough:
I had to look at the hints just to understand the intention for this challenge. I believe it wants to teach you how to use `wget` and `cat`.

To get the flag, just download the file and open it. That's it.

## Learning - wget
`wget` is a command-line utility used to download files from the internet. It supports HTTP, HTTPS, and FTP protocols. You can use it to retrieve files from web servers directly to your computer.

Example:

`wget http://example.com/file.txt`

to get the file from the website, run:

`wget https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag`

## Learning - cat
cat is a command-line utility in Unix/Linux used to display the contents of files. It stands for "concatenate" and can also be used to join multiple files together.

Example

`cat <filename>`

To look at the file from the CLI, use:

`cat flag`


<details><summary>Flag</summary>
    <pre>
    picoCTF{s4n1ty_v3r1f13d_2fd6ed29}
    </pre>
   </details>