**Challenge:** Commitment Issues

**Level:** Easy

**Challenge Author:** Jeffery John

### Description: 
I accidentally wrote the flag down. Good thing I deleted it!

### Step-by-Step Walkthrough:
downloading the `.git` file, I save it without the period so that it won't be hidden, our first job is just to understand the information that we have.

#### Step 1
The message text isn't helpful, so we look to the logs. In the logs, we see two commits and clearly the first one has the flag. I'm not that familiar with Github, so I don't know if there's a method to view the original file within the `.git` folder, but I wasn't able to find it, so I had to copy the `git` folder to a `.git` folder and run the command `git init` which creates a repository for us. Since the `.git` folder already exists, it will just utilize that instead of creating a new one.

#### Step 2
Our next step is to `checkout` the initial commit, which we can do by running `git checkout <id>` where `id` is the commit id. This can be found if we look at the logs. It will be a long string. In fact, there are two long strings. The first one is the commit id you're currently on, the second looks to be a new commit id. We want the one associated with the original commit.

#### Step 3
Now that we are on the original commit, we can see that `message.txt` has a new message!


<details><summary>Flag</summary>
    <pre>
    picoCTF{s@n1t1z3_c785c319}
    </pre>
   </details>