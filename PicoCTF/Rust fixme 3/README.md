**Challenge:** Rust fixme 3

**Level:** Easy

**Challenge Author:** Taylor McCampbell

### Description: 
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!

### Step-by-Step Walkthrough:
Now that we're basically old hats with Rust, this challenge should be no problem! Let's run the code and see what errors we get

1. error[E0133]: call to unsafe function is unsafe and requires unsafe function or block --> src/main.rs:31:31

```
let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ call to unsafe function

For more information about this error, try `rustc --explain E0133`.
```

Running ```rustc --explain E0133``` as suggested by the error describes what's called "unsafe functions" which are essentially functions that should only be called with specific intent because they are more dangerous. It describes a wrapper that we need to put the function call in.

Getting the syntax was a bit tricky, I'd suggest attempting it on your own before looking at the answer. Just follow the guidelines in the error codes and you'll get it. The trick is how to properly wrap the function with the following wrapper

```
unsafe {
    dangerous_fn()
}
```

I found some references to instantiating the instance of "unsafe function with something like this: ```unsafe fn dangerouns_fn() {}``` But it ran just fine without it, so I'm not sure what's going on with that. Just run the code once you've worked out all the bugs and submit our flag!


<details><summary>Flag</summary>
    <pre>
    picoCTF{n0w_y0uv3_f1x3d_1h3m_411}
    </pre>
   </details>