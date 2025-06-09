**Challenge:** Secret of the Polyglot

**Level:** Easy

**Challenge Author:** syreal

### Description: 

The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file? The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?

### Step-by-Step Walkthrough:
Polyglot means: `knowing or using several languages`, that hint along with the phrase `they're getting conflicting information on what type of file it is` immediately stands out to me. Let's download the file and inspect it. The file is titled: `flag2of2-final.pdf` which tells us two things:

1. opening the file provides us with what looks like part of a flag: `1n_pn9_&_pdf_1f991f77}`
2. there is likely only one other flag file to complete the challenge

We'll start by changing the file type to other common file types and see what we can find.

changing to .doc and .xml and .txt revealed metadata about the document, but nothing helpful. Then I remembered that .pdf files are non-structured documents with some similarities to images. I am likely to get some pushback on that statement, but viewing the file as an image, by changing the file to .png, showed me the first half of the flag, so either way, problem solved

<details><summary>Flag</summary>
    <pre>
    picoCTF{f1u3n7_1n_pn9_&_pdf_1f991f77}
    </pre>
   </details>