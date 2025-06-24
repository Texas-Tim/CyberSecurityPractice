**Challenge:** Warmed Up

**Level:** Easy

**Challenge Author:** Sanjay C/Danny Tunitis

### Description: 
What is 0x3D (base 16) in decimal (base 10)?

### Step-by-Step Walkthrough:

## Learning - Base16
Base16, also known as hexadecimal, is a number system that uses 16 symbols to represent values. The symbols are 0-9 for values zero to nine and A-F (or a-f) for values ten to fifteen. It is commonly used in computing to represent binary data in a more readable form.

Example:
* Decimal 15 is F in base16.
* Decimal 26 is 1A in base16.

You can find the a more complete example list of hexadecimal representations online

Hexadecimal is often used for memory addresses, color codes, and encoding binary data. 

## Learning - Base10
Base 10, also known as the decimal system, is the standard number system that uses ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Each digit’s place value is a power of 10. It is the most commonly used number system in everyday life.

## Investigation - conversion
The `int` cast command `int()` can be used to convert from hexadecimal `base16` to decimal `base10`:

`int(<hex>, 16)`

just replace the `<hex>` with the correct value and submit the flag in the correct format

<details><summary>Flag</summary>
    <pre>
    picoCTF{61}
    </pre>
   </details>