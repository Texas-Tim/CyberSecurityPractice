**Challenge:** YaraRules0x100

**Level:** Medium

**Challenge Author:** Nandan Desai / syreal

### Description: 
Dear Threat Intelligence Analyst,
Quick heads up - we stumbled upon a shady executable file on one of our employee's Windows PCs. Good news: the employee didn't take the bait and flagged it to our InfoSec crew.

Seems like this file sneaked past our Intrusion Detection Systems, indicating a fresh threat with no matching signatures in our database.

Can you dive into this file and whip up some YARA rules? We need to make sure we catch this thing if it pops up again.

Thanks a bunch!

Unzip the archive with the password: `picoctf`, although I've included the unzipped file here

Once you have created the YARA rule/signature, submit your rule file as follows:

`socat -t60 - <instanceid> < sample.txt`

(In the above command, modify "sample.txt" to whatever filename you use).

When you submit your rule, it will undergo testing with various test cases. If it successfully passes all the test cases, you'll receive your flag.

### Step-by-Step Walkthrough:
After a little bit of researching, I decided that YARA rules are not something I'd like to dive into for now. I may come back to this at a later date



## Learning - YARA rules
YARA rules are a way to describe and identify patterns of malware, files, or data using a specialized rule-based language. YARA is widely used in cybersecurity and malware analysis to detect and classify files based on textual or binary patterns.

A YARA rule typically consists of:

* Meta section: Describes the rule (author, description, etc.).
* Strings section: Lists the patterns to search for (text, hex, regex).
* Condition section: Defines the logic for when the rule matches.

Example:

```
rule ExampleRule
{
    meta:
        description = "Detects example malware"
    strings:
        $a = "malicious_string"
        $b = { 6A 40 68 00 30 00 00 }
    condition:
        $a or $b
}
```

YARA rules help analysts and security tools scan files and memory for known patterns of malicious or suspicious content.

## Action - Creating our YARA rule
For simplicity, I'm going to be working out of a `sample.txt` file.

Our rule will need to match the signatures from the `suspicious.exe` executable



<details><summary>Flag</summary>
    <pre>
    
    </pre>
   </details>