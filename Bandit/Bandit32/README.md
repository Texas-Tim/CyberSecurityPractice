# Bandit Level 32

### Level Goal
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

### Commands you may need to solve this level
> git 

### Step by Step Walkthrough:
This level has some tricky parts. According to the level description, you're intended to push the file to the repository. 

Typically, the command is ```git add .``` to add all the files you created. You can check the status of added files using ```git status```. Using this command, you can see that your file hasn't been added, huh, odd. Let's force it to be added with ```git add . -f``` which will ignore any "ignore" commands. 

Using ```git status``` again we can see that worked! Use ```git commit -m "push"``` to commit your changes and ```git push``` to add it to the repository. 

Although you'll get an error message, you'll also see a remote message telling you the password. Well done!


* UserName: bandit32

<details><summary>Flag</summary>
    <pre>
    pwd: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K
    </pre>
   </details>