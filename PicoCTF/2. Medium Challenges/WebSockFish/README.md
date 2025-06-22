**Challenge:** WebSockFish

**Level:** Medium

**Challenge Author:** Venax

### Description: 
Can you win in a convincing manner against this chess bot? He won't go easy on you!

### Step-by-Step Walkthrough:
As usual, I got about 99% of the way, then struggled because I didn't really understand what I was looking at.

#### Investigation
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

Upon opening the webpage, you are greeted by a website with a sassy fish and a chess board. You can try and beat the fish, but just winning doesn't seem to be enough to grab the flag. There's also nothing immediately obvious about the inspector console

I've never tried to take advantage of a websocket before, so a lot of things went over my head until I solved it and went to go check out someone else's walkthrough. I'll do my best to share what each step means here.

#### Learning - Websockets
WebSockets are a communication protocol that enables bi-directional, real-time, and persistent communication between a client and a server over a single, long-lived connection. Unlike traditional HTTP, which relies on a request-response model, WebSockets are statefull, allowing for continuous data exchange in both directions without the overhead of establishing a new connection for each message. 

In order to look closer at what's going on behind the scenes, let's open up `Burp Suite` and see what's happening on the websocket side.

#### Investigation - Websockets
Open up a browser on the `proxy` tab and input the webpage. Since I don't really understand how to use `burp`, I had to make sure that `intercept` was off for the websockets information to actually flow. You can see everything popping up in order as you make a move. 

It seems pretty straightforward, you make a move, and information is passed via websocket in the form of `eval #`, where `#` is the overall "score" of advantage. In other words, a higher positive number means that the fish is winning, and a negative number means the player has the advantage.

Let's forward this score to a repeater and see what happens if we send a reallly low score.

Just play around with this, and if you show you're winning overwhelmingly, you'll get a response back with the flag!


<details><summary>Flag</summary>
    <pre>
    picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_e5e75e69}
    </pre>
   </details>