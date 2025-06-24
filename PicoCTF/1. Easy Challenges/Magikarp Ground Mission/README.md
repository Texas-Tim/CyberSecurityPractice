**Challenge:** Magikarp Ground Mission

**Level:** Easy

**Challenge Author:** syreal

### Description: 
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin.

* User: `ctf-player`
* Password: `b60940ca`
* SSH: `ssh ctf-player@venus.picoctf.net -p 50171`

### Step-by-Step Walkthrough:
ssh into the instance and use `ls` to see what we're working with. We immediately see that there are 3 parts of the flag with the first part in the current directory. Instructions for the second are also there.

## Investigation - Part 2/3
The instructions say:

`Next, go to the root of all things, more succinctly `/``

use the `cd` command to move to the `root` directory with:

`cd /`

This will bring you to the `root` directory with the 2nd part of the flag, and the instructions for the third

## Investigation - Part 3/3
The instructions say: 

`Lastly, ctf-player, go home... more succinctly '~'`

use the `cd` command to move to the `home` directory with:

`cd ~`

This will bring you to the `home` directory with the 3rd and final part of the flag! Nice work

<details><summary>Flag</summary>
    <pre>
    picoCTF{xxsh_0ut_0f_\/\/4t3r_c1754242}
    </pre>
   </details>