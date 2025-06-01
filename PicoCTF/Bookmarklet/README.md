**Challenge:** Bookmarklet

**Level:** Easy

**Challenge Author:** Jeffery John

### Description: 
Why search for the flag when I can make a bookmarklet to print it for me?

### Step-by-Step Walkthrough:
Starting up the instance, we are immediately met with a message to run a script to find the flag using something called a `bookmarklet`

```
javascript:(function() {
    var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓË¨ËÓ§Èí";
    var key = "picoctf";
    var decryptedFlag = "";
    for (var i = 0; i < encryptedFlag.length; i++) {
        decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
    }
    alert(decryptedFlag);
})();
```

#### Bookmarklet
A bookmarklet is a small JavaScript program stored as a bookmark in a web browser. When you click the bookmarklet, it runs the JavaScript code on the current web page, allowing you to quickly perform actions like modifying the page, extracting data, or automating tasks. Bookmarklets are often used for convenience or web development/debugging.

#### Step 1
The intended way to solve this challenge is to create a bookmarklet, by creating a new bookmark and pasting the code into the URL.

Clicking the bookmark will then reveal the flag

#### Notes
This can be solved in any manner that runs the javascript. Analyzing this code does not reveal anything that is unique or specific to the website. 

For example, if you `inspect` the page, then paste the code into the console tab, you'll also receive the flag.

<details><summary>Flag</summary>
    <pre>
    picoCTF{p@g3_turn3r_e8b2d43b}
    </pre>
   </details>