**Challenge:** Time Machine

**Level:** Easy

**Challenge Author:** Jeffery John

### Description: 

What was I last working on? I remember writing a note to help me remember...

### Step-by-Step Walkthrough:
First things first, let's take a look at what we're provided with. `challenge.zip` includes a message which reads: `This is what I was working on, but I'd need to look at my commit history to know why...` as well as a `.git` folder. 

For simplicity, I removed the period in the file name, because typically any file with a period at the beginning is hidden.

`commit history` is a clue for us to view the commit history in the `.git` folder, which is located in two places. 

1. Commit Edit Message
2. Logs

Both of these will net you the flag we seek

<details><summary>Flag</summary>
    <pre>
    picoCTF{t1m3m@ch1n3_5cde9075}
    </pre>
   </details>