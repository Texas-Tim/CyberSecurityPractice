**Challenge:** Binary Search

**Level:** Easy

**Challenge Author:** Jeffery John

### Description

Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.

Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!

### Step-by-Step Walkthrough
To be honest, I'm not sure why this challenge lets you download the files. I suppose it can help you walk through the logic of what's going on. To play and grab the flag, you'll have to use the provided instance. Let's explore Binary Search!

#### What is Binary Search
Binary Search is a searching pattern that relies on boolean values of True and False to determine the position of an object in an array. It relies on the array to store values in some sort of order, for example, lets say you had an array of 1-1000 as we do in this challenge. Binary search techniques expect you to start at 500 and the result would tell you which half of the array your value is in. This effectively eliminates half of the array in one go. 


#### Binary Search Effective Speed
Binary Search's effective speed is denoted as `O(log n)`. This means that as the dataset size increases, binary search effective speed grows in `log n` time, which is much better than linear time. Linear implies you're checking each and every item one at a time until you find the obect.

The `Big O` notation is a common measuring notation measuring the effectiveness of algorithms and is what we use to compare one algorithm to another. Read more on `Big O` notation [here](https://en.wikipedia.org/wiki/Big_O_notation)
 

So let's practice, play the game, find the value and learn how one of the simplest search algorithms works by getting hands on!

<details><summary>Flag</summary>
    <pre>
    picoCTF{g00d_gu355_bee04a2a}
    </pre>
   </details>