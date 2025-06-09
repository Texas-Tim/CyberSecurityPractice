**Challenge:** Flag Hunters

**Level:** Easy

**Challenge Author:** SYREAL

### Description: 
Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you.
- webshell: ```nc verbal-sleep.picoctf.net 51134```

### Step-by-Step Walkthrough:
Not going to lie, this one stumped me for quite a bit. The challenge presents you with the source code built in python. Easy right? Well, the code is split up into multiple refrains with a chorus and a "crowd" participation section. After the first verse and chorus, it asks the "crowd" to input whatever you want. Clearly, we're dealing with unsanitized input. But how can we manipulate it the way we want?

When inspecting the code, I suggest strongly that you run it locally and step through it to understand the code. I like to use the Ipython environment which has a local debugger tool which makes it easy to walk through it step by step. 

Inspecting the code closely, youll discover that there's a specific line that tells the code what to print next, the line: ```elif re.match(r"RETURN [0-9]+", line):```. Our goal is to target that line using the only method of input we have, the Crowd Chant. 

A little more inspection reveals that the code uses a number system with ```lip```. We want it to be 0, which we can do if we input RETURN 0.

Ah! A snag, inputting RETURN 0 doesn't work. What's going on? Well, the code has a line that lets it know it has a crowd section and appends the string "Crowd: " to the song. Thus, inputting "RETURN 0" results in "Crowd: Return 0" which is not what we want! We need an alternative.

This is where I got stuck, and I had to look up the answer. It turns out that all the code block needs to work as we want is a split execution, which can be done with the semicolon ```;```. Adding a semicolon simply allows you to run multiple commands per line. 

Input: ```something;RETURN 0``` will net us the result we want and allow us to grab the flag!

### Hints
- When dealing with any challenge, the first thing to do is identify where the exploits are going to be and what kind they are. Sometimes we're guided, sometimes we're not. The title to this challenge doesn't give us a lot of guidance, but we are provided with the source code. It's very very rare to not use what you're provided with in some way in these types of challenges.

- The second thing I'll suggest here is after investigation, the code we're dealing with only has one access point. We cannot provide input in any other way as there is only one method call for user input and it only asks us once, thus we have to be dealing with a input trick of some kind.

<details><summary>Flag</summary>
    <pre>
    picoCTF{70637h3r_f0r3v3r_ac197d12}
    </pre>
   </details>