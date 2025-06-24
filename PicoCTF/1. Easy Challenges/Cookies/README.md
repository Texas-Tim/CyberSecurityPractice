**Challenge:** Cookies

**Level:** Easy

**Challenge Author:** madStacks

### Description: 
Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:27177/.

### Step-by-Step Walkthrough:
Upon opening the webpage, you are greeted by a website with a prompt that allows you to input different cookies

## Investigation - Web Page
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

## Investigation - Inspecting Cookies  
lets start with opening up the web page inspector. We'll open it up and keep an eye on either the `Network` or `Application > Storage > Cookies` tab

A cookie in a web browser, is a small piece of data stored by your web browser. Each cookie is sent by a website to remember information about your visit. Cookies are often used for session management, personalization, and tracking.

Submitting various cookies in the prompt field returns either a note that it's a valid cookie, or an invalid one. The "cookie" in the inspection report also seems to assign a value to the cookie name. For example, if it's invalid, it returns

`cookie   name=-1`

if it's a valid cookie, it returns 

`cookie   name=<value>`

where sugar has a value of 7, snickerdoodle has a value of 0, chocolate chip has a value of 1, etc.

Let's try changing this value (yes you can do that) and see what happens.

## Investigation - Editing cookie values
I wasn't able to figure out a way to change it in the `Networking` tab, but you can in the `Application > Storage > Cookies` tab. Just click in the `Value` section and edit it to any integer. You'll need to refresh the page for it to take effect.

As you can see, the page updates automatically with a different cookie based on the value. We'll need to try various integers to find the one that holds the flag.

There are ways to automate this, and I'm not sure how many valid cookie types there are, but just submitting the right number shouldn't take too long. Try it out for yourself and if you need a hint, I'll include the correct number below.

<details><summary>Cookie</summary>
    <pre>
    18
    </pre>
   </details>

Grab your prize and lets go!

<details><summary>Flag</summary>
    <pre>
    picoCTF{3v3ry1_l0v3s_c00k135_064663be}
    </pre>
   </details>