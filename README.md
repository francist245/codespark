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
| 🔀 Making Decisions | if/elif/else, nested conditionals, complex logic |
| 🔁 Loops | for, while, range, break/continue, FizzBuzz |
| 🔧 Functions | def, parameters, return, scope, Text RPG project |
| 📚 Data Structures | Lists, dicts, tuples, sets |
| 🏗️ OOP | Classes, objects, inheritance, polymorphism, RPG project |
| 📁 Error Handling & Data | try/except/finally, JSON parsing |
| 🌐 How the Internet Works | IP, DNS, HTTP, APIs, REST concepts |
| ☁️ Azure & The Cloud | Cloud computing, Azure services, Met Office supercomputer |
| 🤖 AI & Machine Learning | ML concepts, KNN classifier, AI ethics |
| 🎮 Game Development | Text games, ASCII art, dungeon crawler project |

---

## 🌟 Joshua's Learning Path (Age 5)

| Module | Topics |
|--------|--------|
| 🖥️ Hello, Computer! | What computers are, print(), first programs |
| 🎩 Magic Variables | Variables as labelled boxes, = assignment |
| 💬 Ask and Answer | input(), interactive programs |
| 🤔 Yes or No? *(with a grown-up)* | if/else decisions, simple password checker |
| 🔄 Do It Again! *(with a grown-up)* | for loops, range(), counting |
| 🎮 My First Game! *(with a grown-up)* | Number guessing game — using everything! |

---

## 🔒 Safety Features

- **Sandboxed code execution** — dangerous modules (`os`, `subprocess`, `socket`, etc.) are blocked
- **Age-appropriate restrictions** — Joshua has tighter limits than Toby (no classes, fewer modules)
- **Profile-gated OOP** — `class` definitions only enabled for Toby (M6+ needs them)
- **Content guardrails** — all exercises are educational, no network exploitation or harmful patterns
- **Execution timeout** — infinite loops stop after 8 seconds
- **69 automated tests** — sandbox security verified on every change

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

---

## 📊 Curriculum Stats

| Profile | Modules | Lessons | Steps | Total XP |
|---------|---------|---------|-------|----------|
| Toby (10) | 11 | 26 | 122 | 3,475 |
| Joshua (5) | 6 | 8 | 37 | 850 |
| **Total** | **17** | **34** | **159** | **4,325** |
