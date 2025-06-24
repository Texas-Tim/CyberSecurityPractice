**Challenge:** Let's Warm Up

**Level:** Easy

**Challenge Author:** Sanjay C/Danny Tunitis

### Description: 
Kishor Balan tipped us off that the following code may need inspection: [link](https://jupiter.challenges.picoctf.org/problem/9670/) or http://jupiter.challenges.picoctf.org:9670

### Step-by-Step Walkthrough:
We are immediately greeted by a website with `I made a website`. The title of the page (and the challenge) is directing us towards inspections

## Investigation - web page
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

lets start with opening up the web page inspector using `f12`

Ah Ha! The first part of the flag is embedded in the `source` page. Based on the comments, this is just 1/3. 

Let's check out the `What` and the `How` sections of the page.

The `How` part of the page suggests that we check out other elements that make up the webpage, such as `css` and `js`. 

## Learning - CSS
CSS (Cascading Style Sheets) is a language used to describe the appearance and formatting of a website written in HTML. CSS controls the layout, colors, fonts, spacing, and overall visual presentation of web pages, allowing you to separate content (HTML) from design (CSS).

## Learning - JS
JS stands for JavaScript, a programming language commonly used to create interactive and dynamic content on websites. JavaScript runs in the browser and can manipulate HTML, CSS, and handle user events, making web pages more responsive and functional.

## Investigation - Inspect all the pages
Checking out the other pages in the `source tab` of the `inspection panel` nets us all three parts of the flag. Nice Work!


<details><summary>Flag</summary>
    <pre>
    picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}
    </pre>
   </details>