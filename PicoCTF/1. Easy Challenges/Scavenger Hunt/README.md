**Challenge:** Scavenger Hunt

**Level:** Easy

**Challenge Author:** madStacks

### Description: 
There is some interesting information hidden around this site http://mercury.picoctf.net:5080/. Can you find it?

### Step-by-Step Walkthrough:
We are immediately greeted by a website with `Just some boring HTML`. This is a scavenger hunt, so I expect each step will hint at the next! Let's go check out the HTML of the page

## Investigation - web page
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

lets start with opening up the web page inspector using `f12`

Ah Ha! The first part of the flag is embedded in the `source` page. We don't know how many parts we need to find, but clicking on the page hints that we might want to check out the `HTML`, `CSS` and `JS (Javascript)` pages. Let's look at those as well

## Investigation - CSS
`JS` didn't have anything immediate, but the `CSS` page did, teaching us a little about what a .css file does for the webpage. Part 2 done!

## Investigation - JS
Going back to the `JS` page, there's a question here: `How can I keep Google from indexing my website?`

I would suggest googling to learn more about what it means to index a page, but the question is pointing us to a `robots.txt` file. It's the common file for all webpages that tells browsers (and users) what is and is not appropriate for the page.

Within the page, we find another hint:

`I think this is an apache server... can you Access the next flag?`

## Investigation - Apache
This is where I got stumped and had to look up some help on google. To access a server, we need some way to interact with the webpage, but there aren't any forms?

The one thing that I see is that the word "Access" is caps, which is likely a hint it has something to do with access.

## Learning - .htaccess
A .htaccess file is a configuration file used by the Apache web server to control settings for the directory it is placed in and its subdirectories. It can be used to:

Restrict or allow access to files and directories
Set up URL redirection or rewriting
Specify custom error pages
Control caching and MIME types
Set password protection
.htaccess files are often used to manage access control and security on web servers.

The `.htaccess` file has the next part of our flag! And another hint:

`I love making websites on my Mac, I can Store a lot of information there.`

Another hint towards something I'm unfamiliar with, something about a Mac Store, for me google, for you, just a couple of lines

## Learning - .DS_Store
.DS_Store is a hidden file created by macOS in directories to store custom attributes of a folder, such as icon positions, window size, and view settings. It stands for "Desktop Services Store."

On web servers, .DS_Store files can sometimes be accidentally uploaded and may reveal information about the directory structure or files present in that folder, which can be useful in security challenges or penetration testing.

In this case though, we have our final flag piece! 

<details><summary>Flag</summary>
    <pre>
    picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}
    </pre>
   </details>