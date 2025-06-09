**Challenge:** GET aHEAD

**Level:** Easy

**Challenge Author:** madStacks

### Description: 
Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:28916/

### Step-by-Step Walkthrough:
We are immediately greeted by a website with webpage that provides the option for 2 different colors, Red and Blue. 

#### Investigation - Inspector
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

lets start with opening up the web page inspector using `f12`

The only thing that stands out is that the buttons are using a PHP method to either `GET` or `POST` to a backend server. Let's click the buttons to see what they do while keeping the inspection window open.

#### Investigation - Methods
Okay, this one stumped me for awhile. I had to look at the hints provided. The title makes it clear that we are looking at different methods, it's also strange to have a `GET` method and a `POST` method that have similar results. Nevertheless, nothing seemed to even provide a hint.

Looking at the hints, they suggest using `Burp` which is a tool to intercept messages coming to and from the website to its backend server. We can use it to edit the methods and see what we get as a response.

#### Investigation - Burp
If you don't have `Burp Suite`, I'd strongly suggest downloading it. We'll need it for this challenge.

Playing around, I noticed that the response is determined by what type of method we are submitting, not by whether we choose `Red` or `Blue`. Therfore, we should see what other methods we can submit.

Besides GET and POST, HTTP supports several other methods, including:

1. HEAD: Same as GET, but only retrieves the headers (no response body).
2. PUT: Uploads or replaces a resource at the specified URL.
3. DELETE: Removes the specified resource.
OPTIONS: Describes the communication options for the target resource.
4. PATCH: Partially modifies a resource.
5. TRACE: Echoes back the received request, used for diagnostics.
6. CONNECT: Establishes a tunnel to the server.

Since `HEAD` is part of the title, lets use that one!

What is returned is an empty page. Submitting any other method gives a white page with the buttons, but a `HEAD` method is blank. Another clue that it's the correct submission. 

In `Burp` moving to the `Target` tab, if we open up the `Response Headers` on the `HEAD` method, we see a new value called `Flag` which has our flag!


<details><summary>Flag</summary>
    <pre>
    picoCTF{r3j3ct_th3_du4l1ty_70bc61c4}
    </pre>
   </details>