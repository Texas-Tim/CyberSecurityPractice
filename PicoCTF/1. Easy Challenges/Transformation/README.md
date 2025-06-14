**Challenge:** Transformation

**Level:** Easy

**Challenge Author:** madStacks

### Description: 
I wonder what this really is... `enc`

```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

### Step-by-Step Walkthrough:
This is another one I was unable to solve. After doing some reading online, I don't believe this should be in the "easy" category of picoCTF. There are a few concepts we should recognize about this challenge and I'll try to walk us through it. I am going to avoid long explanations for each concept as there are just too many.

1. the provided join is what was used to encode the `enc` file. Therefore, this is a `reverse engineering` challenge
2. `ord` is a function to translate characters into their `unicode integer` form (exact opposite of `chr`)
3. `chr` is a function to translate integers into their `unicode characters` form (exact opposite of `ord`)
4. `<<` is what is called a `bitshift`, you bitshift left or right.
5. `range(0, len(flag), 2)` is a method to skip every other index. If len(flag) is 5, it will index at 0,2,4.

Putting everything together, our encoder takes two indexed values and adds them together after doing some manipulation.

1. Take the first two characters in the flag
2. Transform the first character into unicode value and bitshift left by 8
3. Transform the second character into unicode value and add it to the first one
4. Transform the final value back into the unicode character
5. Append this character to the string
6. Take the next two characters and iterate from step 2



```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

This one I looked up the answer for a little too early. As such, I don't feel right providing an answer for this one until I've had a chance to forget the answer and come back to it

<details><summary>Flag</summary>
    <pre>
    
    </pre>
   </details>