# Natas Level 3

* Username: natas3
* URL: http://natas3.natas.labs.overthewire.org

### Step by Step Walkthrough:
I have a feeling I'm in for a journey on Natas...The page opens with us immediately seeing that there is "nothing on this page". So, lets look in the sources. 

What you need to realize, is that you can traverse webpages the same way you might a directory... We can see that the folder "files" holds the "pixel.png". (I downloaded it to see if there was something in the pixel and there isn't). But! We can traverse to that folder in the webpage url: ```http://natas2.natas.labs.overthewire.org/files```

#### Final Answer: 
There is a file in there we couldn't see earlier called ```users.txt```! This is a file hosted on the server that the server has access to, but a good webpage does not let visitors see. Clicking in, you can find the password

<details><summary>pwd</summary>
    <pre>
    3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
    </pre>
   </details>