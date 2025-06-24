**Challenge:** Static ain't always noise

**Level:** Easy

**Challenge Author:** syreal

### Description: 
Can you look at the data in this binary: `static`? This BASH script: `ltdis.sh` might help!

### Step-by-Step Walkthrough:
Once again, a simple `ctr-f` or `grep` command nets you the flag fairly easily. Nevertheless, let's try to do this challenge the intended way. Unfortunately, I won't be able to explain why they are teaching us these skills, nor how to properly apply them, but I can at least walk us through the process.

## Investigation - analyzing the files
We have two files to look into. `ltdis.sh` is a bash program that runs a dissassembly script. It helps automate the process of disassembling a binary file (like static). It typically uses tools such as objdump, strings, or nm to extract assembly code, function names, and readable strings from the binary. This makes it easier to analyze the binary for hidden information, such as flags or secrets, without manually running each tool.

Second is the `static` file. This is a binary file. A binary file is a file that contains data in a format that is not plain text. Instead, it is made up of bytes that may represent compiled programs, images, audio, or other types of data. In the context of challenges like this, a binary file usually refers to a compiled executable program that you can run or analyze, but not read directly as text.

## Investigation - dissassembly
To run a bash script, anything that includes `#!/bin/bash` at the beginning, you just use `bash <file>` to run it. Since this is a dissassembly file, we should also include `static` as an argument. Run the following command:

`bash ltdis.sh static`

We receive the following response, and two new files:

```
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

We see that we have a list of all strings extracted from the binary. We can much more easily peruse this file and grab the flag.

#### Note: 
As mentioned, this file already had the flag in it. The process of "dissassembling" was unnecessary for this challenge. However, much more complex binaries, likely with multiple targets and in unknown formats or patterns would make this exercise much more valuable

<details><summary>Flag</summary>
    <pre>
    picoCTF{d15a5m_t34s3r_1e6a7731}
    </pre>
   </details>