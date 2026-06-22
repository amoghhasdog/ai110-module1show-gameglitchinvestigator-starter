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

Purpose: A number guessing game where you try to find the secret number before running out of attempts.

Bugs found: Attempts count didn't match between sidebar and main screen and Enter didn't submit guesses.

Fixes applied: Started attempts at 0 and wrapped the input in a st.form so Enter works.

## 📸 Demo Walkthrough

1. Open the app and pick a difficulty (e.g. Normal).
2. Type a guess (like 40) and press Enter or click Submit.
3. Game says "Too Low" or "Too High" with the correct hint.
4. Keep guessing until you win or run out of attempts.
5. Click New Game to start over.

## 🧪 Test Results

```
pytest tests/
9 passed in 0.03s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
