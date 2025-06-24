**Challenge:** 2Warm

**Level:** Easy

**Challenge Author:** Sanjay C/Danny Tunitis

### Description: 
Can you convert the number 42 (base 10) to binary (base 2)?

### Step-by-Step Walkthrough:
The format of this really threw me off, but looking at the hint shows the intended flag if you need a pointer.

## Learning - Binary
Binary is a number system that uses only two digits: 0 and 1. It is the base-2 numeral system, which computers use to represent and process all data. Each digit in binary is called a bit. In binary, numbers are represented by combinations of 0s and 1s, where each position represents a power of 2.

Example:

`The decimal number 5 in binary is 101 (which is 1×2² + 0×2¹ + 1×2⁰)`

## Action
You can either work out the solution on your own as the number 42 is fairly simple, or you can use python to assist you:

`bin(42)`

<details><summary>Flag</summary>
    <pre>
    picoCTF{101010}
    </pre>
   </details>