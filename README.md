# KidsCode 🚀
### Interactive Python Coding Education for Toby (10) and Joshua (5)

---

## 🚀 How to Launch

**Double-click** `install_and_run.bat`  
— or —  
Open a terminal in this folder and run:
```
python main.py
```

That's it! First launch installs any missing packages automatically.

---

## 👦 Toby's Learning Path (Age 10)

| Module | Topics |
|--------|--------|
| 🐍 Python Foundations | Variables, data types, maths, f-strings, I/O |
| 🔀 Making Decisions | if/elif/else, comparison & logical operators |
| 🔁 Loops | for, while, range, break/continue, FizzBuzz |
| 🔧 Functions *(coming)* | def, parameters, return, scope, lambdas |
| 📚 Data Structures *(coming)* | Lists, dicts, tuples, sets |
| 🏗️ OOP *(coming)* | Classes, objects, inheritance |
| 📁 Files & Exceptions *(coming)* | File I/O, try/except, JSON |
| 🌐 Networking *(coming)* | Internet, HTTP, APIs, web scraping (ethical) |
| ☁️ Azure & Cloud *(coming)* | Azure VMs, Storage, Functions, AI services |
| 🤖 AI & Machine Learning *(coming)* | ML concepts, scikit-learn, AI ethics |
| 🎮 Game Development *(coming)* | pygame: Pong → Platform game → Tetris |

---

## 🌟 Joshua's Learning Path (Age 5)

| Module | Topics |
|--------|--------|
| 🖥️ Hello, Computer! | What computers are, print(), first programs |
| 🎩 Magic Variables | Variables as labelled boxes, = assignment |
| 💬 Ask and Answer | input(), interactive programs |
| 🤔 Yes or No? | if/else decisions, simple password checker |
| 🔄 Do It Again! | for loops, range(), counting |
| 🎮 My First Game! | Number guessing game — using everything! |

---

## 🔒 Safety Features

- **Sandboxed code execution** — dangerous modules (`os`, `subprocess`, `socket`, etc.) are blocked
- **Age-appropriate restrictions** — Joshua has tighter limits than Toby
- **Content guardrails** — all exercises are educational, no network exploitation or harmful patterns
- **Execution timeout** — infinite loops stop after 8 seconds

---

## 🔊 Voice & Sound

- **Text-to-Speech** via `pyttsx3` (offline, no internet needed)
- Joshua's voice: slower, friendly female voice
- Toby's voice: normal pace male voice  
- Sound effects: fanfares on completion, beeps for correct/wrong answers
- Toggle voice on/off with the 🔊 button in any lesson

---

## ➕ Adding More Content

Lesson content lives in:
- `kidscode/curriculum/joshua_curriculum.py` — Joshua's modules
- `kidscode/curriculum/toby_curriculum.py` — Toby's modules

Each lesson follows this structure:
```python
{
    'id': 'unique_id',
    'title': 'Lesson Title',
    'icon': '🐍',
    'xp': 100,
    'steps': [
        {'type': 'teach',    'title': '...', 'content': '...', 'voice': '...'},
        {'type': 'example',  'code': '...', 'expected_output': '...'},
        {'type': 'exercise', 'starter_code': '...', 'expected_output': '...', 'hints': [...]},
        {'type': 'quiz',     'question': '...', 'options': [...], 'answer': 0},
    ],
}
```

---

## 📁 File Structure

```
KidsCode/
├── main.py                          ← Run this!
├── install_and_run.bat              ← Windows launcher
├── requirements.txt
└── kidscode/
    ├── app.py                       ← Main application
    ├── audio_engine.py              ← TTS + sounds
    ├── sandbox.py                   ← Safe code execution
    ├── progress_tracker.py          ← XP, badges, progress
    ├── ui/
    │   ├── profile_screen.py        ← Profile selection
    │   ├── home_screen.py           ← Module dashboard
    │   ├── lesson_viewer.py         ← Lesson steps display
    │   └── code_editor.py           ← Code editor + runner
    └── curriculum/
        ├── curriculum_manager.py
        ├── joshua_curriculum.py     ← Joshua's lessons
        └── toby_curriculum.py       ← Toby's lessons

~/KidsCode/data/progress.json        ← Progress saved here
```

---

*Built with Python + tkinter + pyttsx3 · Completely offline · No data shared*
