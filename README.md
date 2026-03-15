# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
To guess a number with as few hints as possible to get as high a score as possible.

- [ ] Detail which bugs you found.
Fixed: parse_guess to parse and accept only accpetable guesses
      check_guess to return hint properly based on secret and guess
      difficulty range to normal, high and easy to ranges that make sense.

- [ ] Explain what fixes you applied.
Moved game logic into utility files, fixed reversed higher/lower hints, fixed guess parsing so only valid integers are accepted, and corrected the difficulty ranges for Easy, Normal, and Hard. Added tests and ran `pytest` until all tests passed.


## 📸 Demo

![alt text](image.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
