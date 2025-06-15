**Challenge:** dont-use-client-side

**Level:** Easy

**Challenge Author:** Alex Fulton/Danny

### Description: 
Can you break into this super secure portal? [link](https://jupiter.challenges.picoctf.org/problem/17682/) or http://jupiter.challenges.picoctf.org:17682

### Step-by-Step Walkthrough:
Upon opening the webpage, you are greeted by a website with a prompt that allows you to login with your credentials

#### Investigation
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

Let's open up an inspector panel and look at the source element.

#### Investigation - Password verification

Any password runs checks agains the correct value, normally this is done on the host machine, but the source page shows the password checks are performed on the client side, aka in the browser. You can see why that would be insecure as we can simply read what the password is supposed to be. 

#### Action - Unscramble the flag
There's a small hiccup, the password check is sectioned into parts and we have to do a bit of work to unscramble, but the logic is pretty straightforward.

Unscramble the flag and submit it to complete the challenge

<details><summary>Flag</summary>
    <pre>
    picoCTF{no_clients_plz_b706c5}
    </pre>
   </details>