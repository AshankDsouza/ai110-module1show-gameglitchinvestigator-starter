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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
