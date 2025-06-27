**Challenge:** Chronohack

**Level:** Medium

**Challenge Author:** Theoneste Byagutangaza

### Description: 
Can you guess the exact token and unlock the hidden flag?
Our school relies on tokens to authenticate students. Unfortunately, someone leaked an important file for token generation. Guess the token to get the flag.

### Step-by-Step Walkthrough:
connecting to the instance, we're asked to `Enter your guess for the token (or exit): `. There might be something we have to submit to take advantage of the input opportunity, or it might just be reverse engineering the code. Let's take a look at the code base.

## Investigation - code
A few things stand out, without knowing what's relevant, here's what I see:

1. The token is made up of 62 characters: `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`
2. The token is `randomly` generated, and seeded using the time function. Since there is no truly `random` element, this might be where we can take advantage
3. The function `flag()` simply prints the flag, so we're not dealing with encryption
4. The token length is `20`
5. You're provided `50` guesses, implying some element of brute force

There's no other calls to the flag other than guessing the token, and although we could try escaping, there's no `print` function call, so I'm going to go the brute force route, auto generating 50 submissions quickly after calling into the instance.

Submitting all of the guesses might be the most difficult part of this challenge. Upon copy and pasting 50 tokens of 20 character length, I was unable to tell if the system was properly parsing it. If we can find a way to quickly submit 50 guesses, we can simply tune our `time.time()` call to compensate for the time between the instance call and our function call

## Investigation - generating the token
In order to generate our list of 50 tokens, I created a python file called `token_guesser.py` which takes in a `seed` input, which is just the current `Epoch` value times `1000`, then outputs 50 tokens to a file, iterating from the generated seed by `1` each time. 

My plan is to call my function to generate my tokens, then quickly call the `picoCTF` server. I found I can perform these calls some time between `400 and 800 ms`. 

Just for fun, I timed the runtime of both the `token_generator.py` and the `token_guesser.py` scripts. Both of them ran in under a single millisecond. Thus, the only thing really holding us back is how fast my fingers can move.

Since we have up to 50 guesses, generating and brute forcing our way through would be simple. I'm still uncertain how the server takes input submitted in bulk though.

I use the following to call `$EPOCHREALTIME` to get my seed:

`printf "%.0f\n" $(echo "$EPOCHREALTIME * 1000" | bc -l)`

* `printf`: allows me to print in the `CLI`
* `"%.0f\n"`: removes any floating point numbers
* `$EPOCHREALTIME`: is a cached value updated with the current EPOCH time and is available by default
* `echo "$EPOCHREALTIME * 1000"` allows me to pipe it to the `bc` command
* `bc -l`: performs the requested math

## Investigation - submitting the tokens in bulk
As I suspected, the system didn't seem to like me submitting 50 guesses at a time with copy and paste. After a little bit of online searching, I realized that you can submit them with the following:

`nc verbal-sleep.picoctf.net <port> < tokens.txt`

where `<` tells the server to `print` all the values in the file. After a few more tries, and setting my `equalizer` to `400`, I was able to move fast enough to net myself the flag

## Final Notes
This challenge had a lot of ambiguity to it, with a lot depending on how fast your fingers were to submit. Although, looking back, I suppose a `bash` script might have made things simpler. A little testing with the provided script and my script could have let me time things more consistently.

All in all, the challenge was straightforward and simple to understand, and challenging but satisfying to execute. I learned a lot and quite enjoyed learning about how "random" randomness is in coding environments

<details><summary>Flag</summary>
    <pre>
    picoCTF{UseSecure#$_Random@j3n3r@T0rs8a8d9ae0}
    </pre>
   </details>