**Challenge:** Local Authority

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Can you get the flag?

### Step-by-Step Walkthrough:
Upon first opening the page, the first thing you see is a login page.

## Investigation - web page
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

lets start with opening up the web page inspector, it's using php for the login, but otherwise you don't initially see anything on this page, but lets just keep it open.

Putting in a random username and password, leads us to a fail page. However, it's a good thing we kept the inspector open! The username and password logic is on the browser side, big mistake! Input the correct username and password and grab the flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}
    </pre>
   </details>