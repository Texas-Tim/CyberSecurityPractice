**Challenge:** logon

**Level:** Easy

**Challenge Author:** bobson

### Description: 
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? [link](https://jupiter.challenges.picoctf.org/problem/13594/) or http://jupiter.challenges.picoctf.org:13594

### Step-by-Step Walkthrough:
Upon opening the webpage, you are greeted by a website with a prompt that allows you to login with a username and password. (Note, after solving it, I'm not positive what the intended solution is supposed to be, but I will share how I cracked this one)

#### Investigation
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

Let's open up an inspector panel and look at the source element.

The inspection panel doesn't really give anything away. I noticed a script running from the main page, and any scripts should probably occur on the backend. This might be a hint later

#### Investigation - Logon
Logging in as various entities at random works, not sure why right now, but there is no flag and there doesn't seem to be any obvious methods to move around.

Reading the description to the challenge suggest we should log in as `Joe`, so let's try that next.

Joe's password is actually being authenticated, but it's still not letting us in. Since we're getting nowhere with random guesses, let's pivot and use `burp` to capture what's being sent and received.

#### Investigation - Burp
`burp-suite` is a tool to capture packets and change parameters before they get sent. It's useful for when you need a little more information.

In this case, `burp` is unnecessary, but it did help me see the cookies that was in the web page when I was logged in as a random user. I noticed a cookie called `Admin` was set to `False`, which might mean authentication is being handled client side! Always a bad idea.

#### Action - Obtaining Admin access
Moving back to the browser, we need to get admin access. To do that, we should change the value of the cookie to let us in. Right now, it's set to `False`. Let's set it to `True`, refresh the page and Voila! We have the flag


<details><summary>Flag</summary>
    <pre>
    picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}
    </pre>
   </details>