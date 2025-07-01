**Challenge:** Event-Viewing

**Level:** Medium

**Challenge Author:** Venax

### Description:
One of the employees at your company has their computer infected by malware! Turns out every time they try to switch on the computer, it shuts down right after they log in. The story given by the employee is as follows:
1. They installed software using an installer they downloaded online
2. They ran the installed software but it seemed to do nothing
3. Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.

See if you can find evidence for the each of these events and retrieve the flag (split into 3 pieces) from the correct logs!

### Step-by-Step Walkthrough:
This is my first foray into Windows Logs Event Viewer, so I don't know a lot about this. However, the task breaks it down for you. We are searching for 3 parts to the flag, hidden in 3 files that relate to those in the description.

## Investigation - Flag: Part 1
`They installed software using an installer they downloaded online`

Our first task is to identify the software they installed. After playing around with the filters, sorters and other things, I saw a `Source` called `MsiInstaller`. I looked through a few files and saw one that installed a piece of software called: `Totally_Legit_Software`. That seems pretty suspicious! The manufacturer is titled: `cGljb0NURntFdjNudF92aTN3djNyXw==` which is standard `base64` encoding. Putting it through a decoder nets us `picoCTF{Ev3nt_vi3wv3r_`. Woohoo!

## Investigation - Flag: Part 2
`They ran the installed software but it seemed to do nothing`

There's got to be a better way of searching through these files. Windows event viewer is the worst. I'm using the `Find` function, which doesn't let you parse through the notes when you click "find next". But after sorting by date and time (we need the first time that they ran the software) and searching for `Totally_Legit_Software`, I found `\REGISTRY\MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` which runs the executable. I changed my search for that, and found something that had an `ObjectValue` of `Immediate Shutdown (MXNfYV9wcjN0dHlfdXMzZnVsXw==)` pretty quickly. Translating it from `base64` nets us: `1s_a_pr3tty_us3ful_`

Looking a little closer at this latest log, I also noticed that `custom_shutdown.exe` was a new installed executable. I'll try searching for that next

## Investigation - Flag: Part 3
`Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.`

Now we're looking for a bootup sequence, or maybe an error sequence. Let's search for `custom_shutdown.exe`

Hmm... nothing, but we know what we're looking for now. The installed script installed our shutdown executable and set it to run on login. We're looking for a shutdown sequence. Simply searching for `shutdown` will net you the flag

## Note - Intended solution
The manner of my getting to the flag was not ideal, and when I looked online at other solutions, people would post the correct ID's to search for, making the challenge seem to be incredibly simple (Just know what ID's to look for and its easy!) But even knowing the ID's, it's not enough to simply search "what is the WEV Event ID for installing a program, or running it!" You have to be very specific with precise language to get the correct ID. So part of the solution is learning what questions to ask around a Windows environment and I'm happy with the learning that I got and that I got myself a flag.

For those interested, the correct IDs to search for are:
* Installation → Event ID 1033
* Registry Change → Event ID 4657
* Shutdown → Event ID 1074

I still don't understand exactly why no. 2 is a registry change...

<details><summary>Flag</summary>
    <pre>
    picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}
    </pre>
   </details>