**Challenge:** WebDecode

**Level:** Easy

**Challenge Author:** Nana Ama Atombo-Sackey

### Description: 

Do you know how to use the web inspector?
Additional details will be available after launching your challenge instance.

### Step-by-Step Walkthrough:
Our first step as always, is to take a hint from the title and immediately open to the "inspect" portion of the webpage. This can be done by either pressing `F12`, or right clicking in choosing `inspect`. Once in the inspect screen, I prefer to start my investigations in the `Sources` tab which shows all the page documents, files and images associated with that page. 

The next step is to see what information we are working with. The web page has some snarky comments, some images and some page links.

Looking at the source code for `index.html` doesn't reveal anything either, at least not for the `home page`. Let's start looking at the other links

`About` is the second link to consider, and there's an odd phrase embedded in the code here in the `about class`: `cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMTBmOTM3NmZ9`. It's likely not ceasar cipher with the addition of numbers, but might be some other code. 

I like to default to a (cipher identifier tool)[https://www.dcode.fr/cipher-identifier] which strongly suggests we look into a Base64 decoder, luckily it also provides you with that decoding tool. Input our code, and voila! Flag found

<details><summary>Flag</summary>
    <pre>
    picoCTF{web_succ3ssfully_d3c0ded_10f9376f}
    </pre>
   </details>