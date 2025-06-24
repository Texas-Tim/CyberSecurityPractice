**Challenge:** head-dump

**Level:** Easy

**Challenge Author:** Prince Niyonshuti N.

### Description: 
Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.

The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.

### Step-by-Step Walkthrough:
In this challenge, we're immediately presented with a website which we can explore. Although not immediately obvious, one of the posts on the home page leads to some Documentation which lists all the API calls the website supports. 

## Investigation - heap
Since it closely resembles the challenge name, `/heapdump` under the "Diagnosing" section seems suspicious. You can execute it on the page itself, but the file is what we really need, so either download the file or add it to the URL to get the file on your local system.

The Heap Dump is just that. A dump of what is currently on the heap, more on that when you google, but in short, it's a stack of memory.

Perusing the file won't get you anywhere quickly, but just in case, let's search using either the CLI `grep` or `ctr-f`. It turns out that the flag is hiding in the middle of the heap! (I just searched for `picoCTF`)

<details><summary>Flag</summary>
    <pre>
    picoCTF{Pat!3nt_15_Th3_K3y_ad7ea5ae}
    </pre>
   </details>