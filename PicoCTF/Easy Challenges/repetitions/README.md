**Challenge:** repetitions

**Level:** Easy

**Challenge Author:** Theoneste Byagutangaza

### Description: 
Can you make sense of this file?

### Step-by-Step Walkthrough:
As the title suggests, we'll be running through multiple decode operations.

#### Step 1
The `==` at the end of this one indicates base64 encoding. Let's run `echo <message> | base64 -d` to decode it. Remember to add quotations if you're on multiple lines

#### Step 2
This one also has `==` so were back to base64. Run it again!

#### Step 3
This time there's no `==` but the title says repetition. So let's try base64 once more

#### Step 4
The message keeps getting shorter! We soldier on with base64

#### Step 5
This time there is `==` so we were likely on the right track! Let's do it again

#### Step 6
Once more, into the dark

#### Step 7
This one finally nets us the flag. Persistance is key!

<details><summary>Flag</summary>
    <pre>
    picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190}
    </pre>
   </details>