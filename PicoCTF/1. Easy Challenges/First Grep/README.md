**Challenge:** First Grep

**Level:** Easy

**Challenge Author:** Alex Fulton/Danny Tunitis

### Description: 
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

### Step-by-Step Walkthrough:
These challenges always make me laugh a bit as these days, there are lots and lots of methods to grab information. But let's solve it the intended way, with `grep`

## Learning - Grep
grep is a command-line utility in Unix/Linux used to search for specific patterns or text within files. It stands for "Global Regular Expression Print." grep prints lines from files or input that match a given pattern.

Example usage:

`grep "search_term" filename`

This command will display all lines in filename that contain search_term.

## Investigation - Grep
Let's use the pattern defined above to parse our file for the flag. We know that the flag follows the pattern of `picoCTF{}`, but we don't know what's in the middle. We could use `regex` but that's too complicated, let's just `grep` the first part.

`grep picoCTF file`

And voila! We have our flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{grep_is_good_to_find_things_dba08a45}
    </pre>
   </details>