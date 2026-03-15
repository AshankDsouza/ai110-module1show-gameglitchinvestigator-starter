# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1) Bug #1
The problem:
It kept prompting me with "go lower" even when I entered 1 which 
is the least you can go. I believe the hints were in reverse.
So, it said go higher when you actually had to go lower and it 
said go lower when you actually had to go higher. 

Expected:
When the target is 65 and you select 45 it should say "GO HIGHER".
When the target is 65 and you select 85 it should say "GO LOWER".


2) Bug #2
The problems:
When you click new game, the input text from the earlier game does 
get cleared out, a new game does not get started.

Expected:
When you click a new game, the screen should be reset. The entered text should clear, the "You won" message should be cleared and we should be able to enter new guesses for a new game. 

3) Bug #3
On the left side we have the easy, normal, hard dropdown
Easy ranges from 1 to 20
Normal ranges from 1 to 100
Hard ranges from 1 to 50

This is clearly not attended to match with the easy, normal, hard options. 

Expected:
Easy ranges from 1 to 20
Normal ranges from 1 to 50 
Hard ranges from 1 to 100

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggestion:
"Yes — the core conflict in bug 1 is between the comparison result and the hint text in app.py:32-47.

In app.py:37-40, when guess > secret, the code correctly labels the outcome as "Too High" but returns the message "Go HIGHER!". Those two statements contradict each other."

How I verified it? --> Wrote unit tests, refactored, ran the tests and saw they all passed and then verified the second through the UI

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
There were none. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Wrote unit tests, and ran them to check if the bug was fixed. 
Verified again through the UI. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I fixed rather than wrote test_guess_too_high, but it needed a lot of refactoring to work as a test. It showed me some of the utls functions were not refactored to the utils file and that there was bug where it was giving the hint backwards. 


- Did AI help you design or understand any tests? How?
AI helped me refactoring and writing these tests:
test_get_range_easy
test_get_range_normal
test_get_range_hard

AI helped in doing the grunt work, I did not have to specify the correct output which is obvious. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

In Streamlit, the app script runs again from top to bottom every time the user interacts with something, like pressing a button or typing in a field. At first this felt weird, because I expected the app to keep its place like a normal web app. Session state is what makes that possible: it stores values like score, attempts, secret number, and game status so they survive those reruns. Without session state, every interaction would reset the game and lose progress. I now think of Streamlit as "rerun everything, but keep important values in session state."



---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Writing tests to specify correct behavior and functionality. 
Using tests as a way of prompting the agent in a correct direction and also to align with correctness in an objective and repeatable way. 

- What is one thing you would do differently next time you work with AI on a coding task?

Start with writing test cases due to the aforementioned advantages. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.

It help me understand how refactoring should work. How to verify correctness of AI generated code. 
