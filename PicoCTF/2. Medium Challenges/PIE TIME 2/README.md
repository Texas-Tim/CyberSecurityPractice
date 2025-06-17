**Challenge:** PIE TIME 2

**Level:** Medium

**Challenge Author:** Darkraicg492

### Description: 
Can you try to get the flag? I'm not revealing anything anymore!!

### Step-by-Step Walkthrough:
We've been here before with [PIE TIME 1](https://github.com/Texas-Tim/CyberSecurityPractice/tree/main/PicoCTF/1.%20Easy%20Challenges/PIE%20Time%20-%20Position%20Independent%20Executable)! But when we log in, there's a twist. Before we enter the address, we need to enter our name. Before we move on, let's look at this line a little deeper:


#### Learning - fgets
fgets is a C standard library function used to read a line of text from a file or input stream (such as `stdin`). It reads up to a specified number of characters or until a newline is encountered, whichever comes first, and stores the result in a buffer.

`char *fgets(char *str, int n, FILE *stream);`

* `str`: Pointer to the buffer where the read string will be stored.
* `n`: Maximum number of characters to read (including the null terminator).
* `stream`: Input stream (e.g., `stdin` for standard input).

The line on `vuln.c` reads:

`fgets(buffer, 64, stdin);`

where `buffer` will be our name input. Just to see what happens, I input >64 characters in a name, and it only grabbed the first 63 as expected, the threw a `Segfault` error. This is likely exploitable, but I'm not sure I understand how right now, so let's move on.

#### Investigation - Binary Ninja
Opening our `vuln` file with `Binary Ninja`, we find the addresses we're looking for (although, I recently discovered that the command `objdump -d vuln` will provide similar results):

* win: `0x00000136a`
* main: `0x000001400`
* call_functions: `0x0000012c7`

I added in the `call_functions` since we are working out of that function when we input our address. Let's find the difference between `call_functions` and `win`

* `|win-call| = |136a - 12c7| = A3`
* `|win-main| = |136a - 1400| = 96`

Thus, I believe we need to move `A3` memory spaces, although I'm not certain whether that should be forwards, or backwards.

##### Note
At this point, I made a mistake above, that we would need to move `A3` spaces in memory, so if you're following this, just be aware to take what I say with a grain of salt. I'm learning, and so are you!

Here's our next hurdle, the process never prints out the memory space like it did in `PIE TIME 1`.

After a bit of research, I learned something new about string inputs: `format strings`

#### Learning - format strings
Format strings are special strings used in programming (especially in C) to specify how data should be formatted and displayed. They contain placeholders (like %s, %d, %p, etc.) that are replaced by variable values when the string is processed by functions such as printf, sprintf, or scanf.

Examples:

`printf("Hello, %s! You are %d years old.\n", name, age);`

* %s is replaced by a string (name)
* %d is replaced by an integer (age)

In security:

If user input is used directly as a format string (e.g., printf(user_input);), it can lead to a format string vulnerability, allowing attackers to read or write arbitrary memory. Here's a list of all the format specifiers used in `C`

| Specifier | Description | Example Output |
| --- | --- | --- | --- |
| %d | Signed decimal integer | 42 |
| %i | Signed decimal integer (same as %d) | 42 |
| %u | Unsigned decimal integer | 42 |
| %x | Unsigned hexadecimal (lowercase) | 2a |
| %X | Unsigned hexadecimal (uppercase)	| 2A |
| %o | Unsigned octal | 52 |
| %f | Floating-point number (decimal notation) | 3.141593 |
| %e | Floating-point (scientific notation, lower) | 3.141593e+00 |
| %E | Floating-point (scientific notation, upper) | 3.141593E+00 |
| %c | Single character | A |
| %s | String | hello |
| %p | Pointer (address) | 0x7ffd5c3b2e18 |
| %% | Literal percent sign | % |

Pretty quickly, we can see that `%p` is likely what we want! Put that in as our name and we should get back a memory address

#### Investigation - Memory Addresses
What I found is that entering `%p` gives you a seemingly random memory address. I attempted to add or subtract `A3` from it, but no dice on the flag. I did learn, however, that you can enter `%p` multiple times. Since we are limited to 64 characters, I used the following:

`%p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p`

which gave me 21 different pieces of memory. Connecting to the instance multiple times (and even restarting it) and inputting that string, I noticed a few patterns. Some of the memory addresses were random, while others showed up consistently, and even repeatedly, for example:

```
0x628cc0ad72a1 (nil) 0x628cc0ad72df 0x7ffe0cb98c00 0x7c 0x7ffe0cbfb228 0x74d1ad49f6a0 0x7025207025207025 0x2520702520702520 0x2070252070252070 0x7025207025207025 0x2520702520702520 0x2070252070252070 0x7025207025207025 0xa702520702520 0x628c95ec71c0 0x5134f6bb5d9c4400 0x7ffe0cb98c60 0x628c95ec7441 (nil) 0x74d1ad2d6083
```

* `(nil)`: x2, #2, #20 position
* `0x7c`: x1, #5 position
* `0x7025207025207025`: x3, #8, #11, #14 position
* `0x2520702520702520`: x2, #9, #12 position
* `0x2070252070252070`: x2, #10, #13 position
* `0xa702520702520`: x1, #15 position

The rest of the memory addresses also had some consistencies, but only the first 4 characters, or the last 3 characters. For sake of space, I won't list all the similarities here, but go check it out for yourself.

Do any of the memory addresses in the list correspond to the memory address spaces of our functions? Unfortunately, not exactly. I even re-downloaded the binary just in case things could change. I'm also going to relist the binary differences between functions here:

* `|win-call| = |136a - 12c7| = A3`
* `|win-main| = |136a - 1400| = 96`
* `|call-main| = |12c7 - 1400| = 139`

#### Investigation - Solution
This is where I would have been unable to move forward if there wasn't a walkthrough available on the internet. I had to look up what I was missing. There was a tool that I wasn't aware of that we can use to compare parts of memory addresses. Any debugger that can `dissassemble` will do, but I used `gdb`

#### Learning - gdb and dissassemble
`gdb (GNU Debugger)` is a command-line tool used to debug programs, especially those written in C and C++. It allows you to run programs step by step, set breakpoints, inspect variables and memory, and analyze program execution to find bugs or vulnerabilities.

In `gdb`, the `disas` command is short for disassemble. It displays the assembly instructions for a function or a range of memory addresses in the program you are debugging.

Example usage:

`disas main`

This will show the assembly code for the main function.

#### Action - Solution
Now that we're armed with the tools we need, let's use the `gdb - disas` command to check memory. Since this debugger only works on an existing file, it's a good thing they made the `vuln` binary available to us. Just run: `gdb vuln` to get started.

Since we already have quite a lengthy walkthrough, I won't give all of the breakdown of how to use `gdb` here. Suffice to note, we use `r` to rerun the file, `c` to continue after a breakpoint, and `disas` to "disassemble" the functions and see their spots in memory. The nice thing about having this file locally and being run on its own, is that the memory addresses aren't changing. So we can play around as much as we'd like!

To continue, run:

1. `r` to start the program
2. `%p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p` to list all the memory addresses
3. `quit`
4. `disas win`
5. `disas main`
6. `disas call_functions`

Capturing and analyzing each of the above lists, we receive a few important pieces of information

1. We can confirm that the different memory addresses for each function are what we'd expect
2. One of the memory addresses that are listed in step `2` exists within the disassembled `main` function

Since we know that the memory addresses listed in step `2` have a consistent pattern, we should be able to identify this same piece of memory when we connect to our instance online.

To solve this challenge, you will need to:
1. Identify the memory bit that's in the `main` function
2. Change the last three digits to reflect the initial memory address of `main`
3. Find the difference between the `win` and `main` functions
4. Perform the appropriate arithmetic 
5. Submit the result

##### Note
I found the solution slightly unsatisfying, although I learned a lot throughout the process. What I don't understand is why the memory addresses were consistently returned in the same pattern each time I took advantage the format string vulnerability. I also don't understand why those specific memory addresses returned. For example, why didn't we see any memory spaces from the other functions? 

The main challenge was using the `debugger` and `dissassemble` steps to identify that the memory spaces were associated with one of the functions, then recognizing that there was something close in one of the returned memory addresses when inserting the format strings. All in all, quite a fun challenge!

<details><summary>Flag</summary>
    <pre>
    picoCTF{p13_5h0u1dn'7_134k_bb903549}
    </pre>
   </details>