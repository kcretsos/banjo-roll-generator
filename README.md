# banjo-roll-generator
Created by Kevin Cretsos
kjcretsos@gmail.com
10-02-2020
************************
This program generates a random 5 string banjo roll from JSON files. Rolls can range from 1, 2, 3, or 4 finger combos. The program also randomizes string patterns (T = 2-5, I = 2-3, M = 1). Rules: no two fingers will repeat sequentially (ie. end of roll #1 (x) to start of roll #2 (x+1)). If start of current finger sequence does not equal end of previous sequence, print the roll. Otherwise search for another sequence until the above condition is met. Repeat as many rolls as needed with the loop variable 
************************
Fingers Key:
	T = Thumb finger
	I = Index finger
	M = Middle finger
Strings Key:
	5 = 5th string
	4 = 4th string
	3 = 3rd string
	2 = 2nd string
	1 = 1st string
************************
To get started I installed Python 3.7 Anaconda with Spyder IDE. Place your files in the Spyder directory. For example, in Windows: C:\Users\myName\.spyder-py3\

To open and edit the JSON files with different combinations, you can use Notepad++
************************
