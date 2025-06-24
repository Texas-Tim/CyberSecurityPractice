**Challenge:** Unminify

**Level:** Easy

**Challenge Author:** Jeffery John

### Description: 

I don't like scrolling down to read the code of my website, so I've squished it. As a bonus, my pages load faster!
Additional details will be available after launching your challenge instance.

### Step-by-Step Walkthrough:
Spinning up the instance and visiting the web page, we are greeted with a cryptic message, telling us our browser has the flag, but we need to figure out how to read it. 

## Investigation - web page
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

Let's open up an inspector panel and look at the source element. we can `inspect` the page with `F12` or by right clicking on the page

And voila, there's the flag just slightly hidden as a `Class Title`. 

<details><summary>Flag</summary>
    <pre>
    picoCTF{pr3tty_c0d3_b99eb82e}
    </pre>
   </details>