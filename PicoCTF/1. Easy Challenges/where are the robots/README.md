**Challenge:** where are the robots

**Level:** Easy

**Challenge Author:** Zaratec/Danny

### Description: 
Can you find the robots?  [link](https://jupiter.challenges.picoctf.org/problem/36474/) or http://jupiter.challenges.picoctf.org:36474

### Step-by-Step Walkthrough:
We are immediately greeted by a website with `Where are the robots?`.

#### Investigation
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

lets start with opening up the web page inspector using `f12`

#### Investigation - Robots
Unfortunately, nothing is in the source, and there are no interactive elements. Let's consider the hints of the challenge.

We are being directed towards `robots`

In a webpage, every page has a `robots.txt` file associated with it. `robots.txt` is a plain text file placed in the root directory of a website to instruct web crawlers and search engines which pages or directories should not be indexed or crawled. It is part of the Robots Exclusion Protocol and is commonly used to control access to certain parts of a website.

Example content:
```
User-agent: *
Disallow: /private/
```

This tells all web crawlers not to access the /private/ directory.

#### Action - identifying hidden/disallowed pages
Let's take a look at this site's `robots.txt` at: `https://jupiter.challenges.picoctf.org/problem/36474/robots.txt`

Bingo! We see that there is a hidden file

```
User-agent: *
Disallow: /477ce.html
```

Let's check out: `https://jupiter.challenges.picoctf.org/problem/36474/477ce.html`

Voila! There's the flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
    </pre>
   </details>