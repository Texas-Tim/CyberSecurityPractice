**Challenge:** IntroToBurp

**Level:** Easy

**Challenge Author:** Nana Ama Atombo-Sackey & Sabine Gisagara



### Step-by-Step Walkthrough:
I am completely new to Burp. As this is a new tool, much of my explanations are likely to be...lacking in some way. 

#### What is Burp?
Burp Suite is a popular cybersecurity tool used for web application security testing. It acts as an intercepting proxy, allowing you to inspect, modify, and replay requests and responses between your browser and a web server. Burp Suite is widely used by penetration testers and security researchers to find vulnerabilities such as SQL injection, XSS, authentication flaws, and more.

#### Step 1
First, let's explore Burp a little. The Live Task is not needed for this task, and I'm not really sure what it is, so lets move on to Target. The page should be empty, and prompting you to open the browser. This allows you to set the target host you're planning to investigate. Clicking on `Open Browser` and posting `http://titan.picoctf.net:<PORT>/` will allow you to view the responses you're getting from that site.

##### Note
If your browser is just hanging, check in Burp, is the Proxy tab highlighted? This happened to me and it means that the page has been intercepted and is waiting for your interaction before sending a response to the webserver

#### Step 2
At this point, just play around with the website a little and see the various responses. You will notice that the webpage has two pages. The main page, and `/dashboard`. You should see the following status codes:

1. 200 - all is well
2. 302 - redirecting

Our goal seems to be to overcome the OTP, but we don't yet know how

#### Step 3
Now that we've explored the website, lets take a look at the Proxy tab. Proxy in Burp allows you to intercept the requests before they get sent to the web server. You can manipulate the data or just look at the request information. If you haven't already turned on `Intercept`, go ahead and do so now. You'll have to maneuver around the pages online again, but once you do, you'll start to see that the web page just never loads.

We need to `Forward` the request in the Burp tool. This forwards the request to the web server and removes it from the proxy list. Everything in the proxy list is waiting for you to approve sending to it's destination. Note that you can also see all the details about the request itself. At the moment, nothing seems unusual

#### Step 4
Now that you understand Proxy, right click on one of the requests and send it to the `Repeater` The Repeater allows you to quickly resubmit requests which allows you to quickly change the values of any of the forms that you've filled out. Such as the OTP, which is what is currently blocking you. I'd suggest playing around in the Request box and changing the value of the OTP.

##### Note
It's worth noting that OTP are not supposed to accept text, but it does. It also accepts the value of nothing, but returns a permission denied each time.

#### Step 5
At this point, we know that the OTP is not being filtered and is accepting any value. The first thing we should try is not submitting the OTP at all, but removing it. And this also turns out to be the final trick! This can be done on the Proxy tab, or the repeater tab to obtain the flag. Well done!


<details><summary>Flag</summary>
    <pre>
    picoCTF{#0TP_Bypvss_SuCc3$S_e1eb16ed}
    </pre>
   </details>