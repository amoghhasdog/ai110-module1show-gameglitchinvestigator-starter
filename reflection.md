# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Upon first running the game, one thing caught my eye immediately. I noticed that it said "Attempts left: 7" in the blue. However, on the left panel, it said "Attempts allowed: 8." Another I noticed as I started testing the game was pressing the Enter key didn't actually enter the number input. Nothing would happen.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Opening the game for the first time. | Polished, complete menu free from errors. | Showed 8 attempts on the left and 7 attempts on the main screen. | Displayed allowed attempts should be consistent throughout game. |
| Pressing Enter on number input. | Enters number as guess. | Nothing occurs. | Number should be inputted as a guess but instead nothing happens. |
| Clicking New Game button. | A new game starts, which allows us to enter new guesses for the new number. | Nothing occurs. | Clicking New Game should allow me to make guesses for the new number, but I cant't.|

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
