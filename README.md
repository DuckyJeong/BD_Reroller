This script doesn't work in your environment unless you match some of the codes with image files used for image matching(screenshot & locate) functions in pyautogui.

# Automated BD Rerolloer
Let's contract a legend mercenary in a mobile game.

This python script tries to automate rerolling for a legendary package (10 contracts/summons) which requires a gamer to clear 2-10 stage and get at least 600 diamonds.

# Dependencies
'pyautogui' as the main framework for automated tasks.
'opencv' and 'pytessearct' for a few recognition features.
'time' to manage delays intentionally

# Features
1) Emulator Functions
- locateemul() searches an emulator icon on the main screen and moves it oonto the left-upper edge. It's necessary to place an emulator on the edge in this version.

2) Button Search Functions
- searchskip(): tries to find a 'skip' button on the screen. If a button is found, it will be clicked and the gamer will proceed on. Else, it continues to search the button until it finds one.
- searchtutor(): tries to find a 'tutor's portrait' on the screen. If she is found, an exit button will be clicked and the gamer will proceed on. Else, it continues to search the button until it finds one.
- checkskip() and checktutor(): one-time-checker versions of 'searchskip()' and 'searchtutor()'

3) Reroll Process Management
 a. Quest manager
 -searchquest(): tries to find a 'quest' menu title on the screen to determine if the gamer is on the 'quest' menu. If it isn't on the quest menu.
 -acceptquest(): simply clicks a static cordinates referring to the 'to accept' button.
 -endquest(): does the same thing to 'acceptquest()' and press 'esc' twice for each quest reward.
 -setquest(): sets a quest number manually and executes the remaining processes after the quest. It only works on a quest interface where the gamer can accpet the certain quest.
 -skipintro(username): skips the intro phase of the game and set an account name passed as 'username'. After that, it will triger 'skipgreeting()'
 -skipgreeting(): skips greetings and notices coming up until the gamer actually controls anything in the game. After that, it will triger the main quest loop.
 - excecutequest(): performs tasks for quest conditions like 'clear a certain stage', 'contract with a certain scroll for a mercenary type'. It follows specifically instructed orders(with bunch of if-elif conditions referring quest numbers). 
 
 b. Battle manager
 - readyforbattle(): tries to find a 'to start battle' button on the screen. If the button is found, it will automatically set up a team using the originally provided auto set-up feature in the game. Else, it will be checked whether a tutorial or skip phase is on the screen and skip them to proceed on.
 - readyfornext(): tries to find a 'to the next field' button on the screen and do the same task with 'readyforbattle()'. A skip or a tutorial pahse are also handled similarly to 'readyforbattle()'
 
 c. Contract manager
 - getmission(): gets mission rewards from the mission interface. It checks if there's an active 'reward' button and click the button until it finds no reward on the screen. 
 - getpackage(): purchases a legendary scroll package at the event web page in the game. And it accesses to the mailbox to get the package
 - summonleg(): accesses to the contract shop and uses the legendary scroll package.

4) Recognizer and Reroller (working)
 a. Contract result recognition
 b. Reroll code recognition

# Remarks
I'm a newbie programmer. This project is my first work with any computer programming language. I know the codes are terribly unorganized and have many redundant expressions. Even the script wouldn't work on your environment. But, any suggestion or advice is more than welcome :) Thank you for taking your time to read the codes.
