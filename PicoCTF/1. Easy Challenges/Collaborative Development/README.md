**Challenge:** Collaborative Development

**Level:** Easy

**Challenge Author:** Jeffery John

### Description: 
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?

### Step-by-Step Walkthrough:
Another Git challenge by Jeffery! We already know how to navigate github with `checkout`, let's see what he has in store for us this time.

## Investigation - checkout
The `flag.py` file has a script which simply prints out a message and is not that useful for us.

Reviewing the logs, we see lots of commits this time. I perused a few of the branches and quickly realized the intention for this challenge was not to use `git checkout`, although it would certainly work, instead we are supposed to navigate three `branches`. In fact, running `git branch -a` will show you all the branches we need to search. The commit messages in the logs provides us a hint for which ID's we are looking for. I will leave that as an exercise for the reader.

## Investigation - git diff
I used `git diff` to quickly compare the values within the `flag.py` across different branches. This can be done with the following script: `git diff <id 1>:flag.py <id 2>:flag.py`

This quickly shows me what the difference is between files, and I can see that the flag has three parts. I have to copy the flag contents, but nothing too difficult.

##### Final Notes
If there is a method for quickly printing or merging I'm unaware. Most of the solutions I found online also used the `diff` method. I'm pretty certain you "could" merge the branches into one, but I'm not familiar enough with Git for that at the moment. You'd also have to deal with merge conflicts since the file has recurring aspects.

<details><summary>Flag</summary>
    <pre>
    picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_6c06cec1}
    </pre>
   </details>