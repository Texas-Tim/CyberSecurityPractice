**Challenge:** Apriti sesamo

**Level:** Medium

**Challenge Author:** Junias Bonou

### Description: 
I found a web app that claims to be impossible to hack!
Try it [here](http://verbal-sleep.picoctf.net:57184/)!

### Step-by-Step Walkthrough:
First, `Apriti sesamo` is `Open sesame` in Italian, which is also apparently the name for "Sesame Street" in that part of the world.

## Investigation - web page
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

On the page, we have a login button and some text with nothing immediately standing out on the inspect console.

## Investigation - testing common vulnerabilities
Attempting to login and randomly choose some usernames and passwords doesn't give me anything helpful either, not even using Burp. But this is a `.php` webserver, so let's test some injections.

Unfortunately, this was a dead end as well. I wasn't able to find any specific vulnerabilities. At this point, I go check the hints and see if I'm missing something obvious.

## Investigation - emacs
I'm always a little salty when the challenge relies on hints for you to be able to solve it. Maybe there's a reference to `emacs` somewhere that someone more familiar would be able to guess, but it was lost on me.

Moving on from my rant, the hint points at `backup files` and `emacs`. Looking online, backup files are represented with a `~` at the end of the file. Adding this character to the end of `http://verbal-sleep.picoctf.net:57184/impossibleLogin.php` brings us to a similar page, but the inspector console has a new piece of information:

```
<?php
 if(isset($_POST[base64_decode("\144\130\x4e\154\x63\155\x35\x68\142\127\125\x3d")])&& isset($_POST[base64_decode("\143\x48\x64\x6b")])){$yuf85e0677=$_POST[base64_decode("\144\x58\x4e\154\x63\x6d\65\150\x62\127\x55\75")];$rs35c246d5=$_POST[base64_decode("\143\x48\144\153")];if($yuf85e0677==$rs35c246d5){echo base64_decode("\x50\x47\112\x79\x4c\172\x35\x47\x59\127\154\163\132\127\x51\x68\111\x45\x35\166\x49\x47\132\163\131\127\x63\x67\x5a\155\71\171\111\x48\x6c\166\x64\x51\x3d\x3d");}else{if(sha1($yuf85e0677)===sha1($rs35c246d5)){echo file_get_contents(base64_decode("\x4c\151\64\166\x5a\x6d\x78\x68\x5a\x79\65\60\145\110\x51\75"));}else{echo base64_decode("\x50\107\112\171\x4c\x7a\65\107\x59\x57\154\x73\x5a\127\x51\x68\x49\105\x35\x76\111\x47\132\x73\131\127\x63\x67\x5a\155\71\x79\x49\110\154\x76\x64\x51\x3d\75");}}}?>
```

## Investigation - code review
with some `base64` decoding of the hex values, we can identify which of these sections we need to pay attention to. There is this interesting line:

`if(sha1($yuf85e0677)===sha1($rs35c246d5))...echo file_get_contents(../flag.txt)`

We can see that the variable `yuf85e0677` is related to the username and the variable `rs35c246d5` is related to the password (this is clear in that they are assigned in the code above with assignements), so maybe we can look into that. `sha1` is a hash function and `===` is the strict comparison operator, ie they have to be "exactly" the same datatype and result. 

Going a little farther up, we see another interesting line:

`if($yuf85e0677==$rs35c246d5)...echo Failed! No flag for you`

So there are two steps. We need a username and a password that are not similar, but that collide when hashed by `sha1`. Although `sha1` is older and has been proven to have collisions, this is not an easy task, and beyond what we would be expected to perform in a simple online challenge, or at least, I was unable to find anything to input. I'm a bit lost about what to do next here.

## Note - Solution
It turns out, that there is a way we can submit a collision. I found the examples on `shattered.io` with the two files that showed a collision, but I didn't know we could submit a file in the login page. I'll share my learning's with you here. Simply call the website from your cli as so:

```
curl -X POST -F "username=<shattered-1.pdf" -F "pwd=<shattered-2.pdf" http://verbal-sleep.picoctf.net:57184/impossibleLogin.php
```

This was a fun solution, because not only did I learn that you could submit files using a `curl` command, but I learned an example of how `SHA1` collides

## Note - Alternative solution
While looking at various solutions to this problem, I came across a method to simply bypass the checks entirely. By using `Burp` to intercept the web traffic, we can edit the `username=` and `password=` fields to `username[]=` and `password[]=`. This changes the data type from a string, to a list for the input. You still have to have different input for the first check (I tried), but the second check will return `null` for both values, making it equal. What a cool solution!

I could not for the life of me figure out how to recreate this in the console, but still cool!

<details><summary>Flag</summary>
    <pre>
    picoCTF{w3Ll_d3sErV3d_Ch4mp_9c79e5f6}
    </pre>
   </details>