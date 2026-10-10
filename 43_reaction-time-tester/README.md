# Real-Time Reaction Time Tester

This project is a windowed reaction time tester using **Pygame**. It introduces students to interactive game design using object-oriented principles and real-time graphical rendering.

---

## What’s Provided

A partially working version of a reaction time tester with:

- A grey "wait" screen that turns green at a random moment
- Click (or press `Space`) as fast as possible once it turns green
- A running average reaction time and round counter

You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Clone the repo or download the project folder.
2. Make sure you have Python 3.10+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Refine Input Timing Detection

> Reaction times are measured from when the round *started*, not from when the screen actually turned green - so every recorded time is inflated by however long the wait phase lasted, and clicking during the grey "wait" screen gets timed and recorded exactly like a real reaction instead of being flagged as a false start. Investigate and enhance input handling so only genuine reactions after "go" are recorded, measured from the moment "go" happened.


### Task 2: Implement Game Over Condition

> Add a screen that displays the final results (every reaction time and the average) once all rounds are complete, then gracefully waits for input instead of just printing to the console.


### Task 3: Add Replay Option

> After the results screen, allow the user to play again by choosing a difficulty (Easy, Medium, or Hard wait-time range/round count), or exit.


### Task 4: Add Sound Feedback

> Add basic sound effects for the "go" cue, a false start, and the session ending.


---

## Expected Behavior

- Each round starts with a grey screen for a random, unpredictable delay
- The screen turns green at a random moment, at which point the player should click or press `Space` as fast as possible
- Reacting after "go" records and displays that round's reaction time in milliseconds
- Reacting before "go" should be treated as a false start rather than a valid time
- After a short pause, the next round begins automatically; the session ends after the configured number of rounds

## Controls and Difficulty

- During a round, click anywhere in the game window or press `Space` to react. An input before the green cue is a false start; that attempt is not included in the results, and a fresh attempt starts after the pause.
- On the results screen, click **Easy**, **Medium**, or **Hard** to start a fresh five-round session. Click **Exit** or close the window to quit.

| Difficulty | Random wait before green | Valid rounds |
| --- | ---: | ---: |
| Easy | 1,500–3,000 ms | 5 |
| Medium | 1,000–2,500 ms | 5 |
| Hard | 500–1,500 ms | 5 |

## Sound Effects

The game creates short tones with Pygame's mixer when the green cue appears, a false start occurs, and the session ends. No sound files or extra packages are required. If audio initialization or playback is unavailable, the game continues silently with all gameplay and menu features available.

**Implementation status:** Tasks 1–4 are implemented: reactions are timed from the green cue, false starts are excluded, session results and replay are available, and each sound is triggered once for its event.

---

## Folder Structure

```
reaction-time-tester-main/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   └── round.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history
