"""
Joshua's Curriculum - Age 5

6 Modules designed for a 5-year-old:
  M1: Hello, Computer!     - What computers are, first print()
  M2: Magic Variables      - Variables as labelled boxes
  M3: Ask and Answer       - input() and talking to programs
  M4: Yes or No?           - if/else with everyday examples
  M5: Do It Again!         - for loops with range()
  M6: My First Game!       - Number guessing game (project)

All 'voice' fields are spoken aloud by the TTS engine.
All 'content' fields are displayed on screen.
"""

JOSHUA_MODULES = [
    # ================================================================
    # MODULE 1: Hello, Computer!
    # ================================================================
    {
        'id': 'j_m1',
        'title': 'Hello, Computer! 🖥️',
        'icon': '🖥️',
        'description': 'Find out what computers are and make one say hello!',
        'badge': 'Computer Explorer',
        'badge_icon': '🖥️',
        'color': '#FF6B6B',
        'prerequisite_modules': [],
        'lessons': [
            {
                'id': 'j_m1_l1',
                'title': 'What is a Computer?',
                'icon': '💻',
                'xp': 50,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Welcome, Joshua! 👋',
                        'content': (
                            "Hi Joshua! 👋\n\n"
                            "Welcome to KidsCode!\n"
                            "Your very own coding adventure! 🚀"
                        ),
                        'voice': (
                            "Hi Joshua! Welcome to Kids Code — your very own coding adventure!"
                        ),
                    },
                    {
                        'type': 'story',
                        'title': 'Computers are Amazing! 🌟',
                        'content': (
                            "A computer is a super-fast machine! 💻\n\n"
                            "It can play games 🎮, show videos 🎬,\n"
                            "and help you learn to code! 📚"
                        ),
                        'voice': (
                            "A computer is a super-fast machine! "
                            "It can play games, show videos, and help you learn to code! "
                            "Are you ready? Let's go!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Computers Follow Instructions 📋',
                        'content': (
                            "Imagine you are a robot 🤖\n\n"
                            "If I say:\n"
                            "  1️⃣  Clap your hands\n"
                            "  2️⃣  Stamp your feet\n"
                            "  3️⃣  Spin around!\n\n"
                            "You would follow those instructions in ORDER!\n\n"
                            "That is EXACTLY what a computer does.\n"
                            "We write instructions and the computer follows them — super fast! ⚡"
                        ),
                        'voice': (
                            "Imagine you are a robot! "
                            "If I say clap your hands, stamp your feet, spin around — you would follow those instructions in order! "
                            "That is exactly what a computer does. "
                            "We write instructions and the computer follows them, super fast!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Python is a Coding Language 🐍',
                        'content': (
                            "To talk to a computer, we use a special language!\n\n"
                            "We are going to learn PYTHON 🐍\n\n"
                            "Python is NOT a snake — it is a coding language!\n"
                            "It has a funny name, but it is great for YOU! 😄"
                        ),
                        'voice': (
                            "To talk to a computer, we use a special language! "
                            "We are going to learn Python! "
                            "Python is not a snake — it is a coding language! "
                            "It has a funny name, but it is great for you!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Python is Everywhere! 🌍',
                        'content': (
                            "Loads of people use Python every day! 🌍\n\n"
                            "The people who made YouTube used Python! 🎬\n\n"
                            "So did the people who made Instagram! 📸"
                        ),
                        'voice': (
                            "Loads of people use Python every day! "
                            "The people who made YouTube used Python! "
                            "So did Instagram! Pretty cool, right?"
                        ),
                    },
                    {
                        'type': 'exercise',
                        'title': 'Make the Computer Talk! 🗣️',
                        'content': (
                            "Let's make the computer say something!\n\n"
                            "We use  print()  to make the computer display words.\n\n"
                            "Press the big green RUN button to try it!\n\n"
                            "Then change the words inside the speech marks!"
                        ),
                        'voice': (
                            "Now it is your turn! "
                            "We use the word print with brackets to make the computer display words. "
                            "Press the big green Run button to try it, then change the words!"
                        ),
                        'starter_code': 'print("Hello, World!")',
                        'prefill': True,
                        'expected_output': 'Hello, World!',
                        'hints': [
                            'Make sure you have speech marks " " around the words!',
                            'The brackets () must be there — print needs them!',
                            'Capital letters matter — use print not Print',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Quick Quiz! 🧠',
                        'question': 'What does  print()  do?',
                        'voice': 'Quick quiz time! What does the print command do?',
                        'options': [
                            '🖨️  It prints on paper',
                            '📺  It displays words on the screen',
                            '🔊  It makes a sound',
                            '🎮  It starts a game',
                        ],
                        'answer': 1,
                        'explanation': 'print() displays words on the screen — brilliant!',
                        'explanation_voice': 'That is right! Print shows words on the screen. Well done!',
                    },
                ],
            },
            {
                'id': 'j_m1_l2',
                'title': 'Your First Real Program! 🌟',
                'icon': '🌟',
                'xp': 75,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Programs are Lists of Instructions',
                        'content': (
                            "A PROGRAM is a list of instructions for the computer.\n\n"
                            "Just like a recipe tells you how to bake a cake 🎂:\n\n"
                            "  🥚  Step 1: Get the eggs\n"
                            "  🍯  Step 2: Add the sugar\n"
                            "  🥄  Step 3: Mix it all up\n"
                            "  🔥  Step 4: Put it in the oven\n\n"
                            "A program tells the computer EXACTLY what to do, step by step!"
                        ),
                        'voice': (
                            "A program is a list of instructions for the computer. "
                            "Just like a recipe tells you how to bake a cake, "
                            "a program tells the computer exactly what to do, step by step!"
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'A Program with Multiple Steps',
                        'content': (
                            "A program can have LOTS of  print()  instructions!\n\n"
                            "Look at this program — it draws a shape with words:"
                        ),
                        'voice': "A program can have lots of print instructions! Look at this example.",
                        'code': (
                            'print("*****")\n'
                            'print("* Hi! *")\n'
                            'print("*****")'
                        ),
                        'expected_output': '*****\n* Hi! *\n*****',
                    },
                    {
                        'type': 'exercise',
                        'title': 'Write Your Own Message!',
                        'content': (
                            "Now write a program that prints your name three times!\n\n"
                            "Change the word  Joshua  inside the speech marks.\n\n"
                            "Try to add something fun on the third line!"
                        ),
                        'voice': (
                            "Your turn! Write a program that prints your name three times. "
                            "Change the word inside the speech marks to your name. "
                            "Then try to add something fun on the third line!"
                        ),
                        'starter_code': (
                            'print("Joshua")\n'
                            'print("Joshua")\n'
                            'print("Joshua is AWESOME! 🌟")'
                        ),
                        'prefill': True,
                        'expected_output': None,  # Free-form exercise
                        'hints': [
                            'You can change what is in the speech marks to anything you like!',
                            'Try adding emoji between the speech marks 😄',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Quiz Time! 🌟',
                        'question': 'How many print() statements can a program have?',
                        'voice': 'Quiz! How many print statements can a program have?',
                        'options': [
                            '🔢  Only 1',
                            '🔢  Only 3',
                            '♾️  As many as you want!',
                            '🔢  Only 10',
                        ],
                        'answer': 2,
                        'explanation': 'You can have as many print() statements as you like! Programs can be thousands of lines long!',
                        'explanation_voice': 'Correct! You can have as many print statements as you want. Amazing!',
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 2: Magic Variables 🎩
    # ================================================================
    {
        'id': 'j_m2',
        'title': 'Magic Variables 🎩',
        'icon': '🎩',
        'description': 'Learn to store things in magic boxes called variables!',
        'badge': 'Variable Wizard',
        'badge_icon': '🎩',
        'color': '#4ECDC4',
        'prerequisite_modules': ['j_m1'],
        'lessons': [
            {
                'id': 'j_m2_l1',
                'title': 'Variables are Magic Boxes! 📦',
                'icon': '📦',
                'xp': 75,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'The Magic Box! 🎩✨',
                        'content': (
                            "Imagine you have a magic box 📦\n\n"
                            "You can put your name inside it!\n"
                            "You can take it out whenever you want.\n"
                            "You can even change what is inside!\n\n"
                            "In Python, these magic boxes are called VARIABLES 🎩\n\n"
                            "A variable stores information so the computer can remember it!"
                        ),
                        'voice': (
                            "Imagine you have a magic box! "
                            "You can put your name inside it, take it out whenever you want, "
                            "and even change what is inside! "
                            "In Python, these magic boxes are called variables. "
                            "A variable stores information so the computer can remember it!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Creating a Variable',
                        'content': (
                            "To make a variable, we use the equals sign  =\n\n"
                            "    name = \"Joshua\"\n\n"
                            "This means:  Put the word Joshua into a box called name\n\n"
                            "    age = 5\n\n"
                            "This means:  Put the number 5 into a box called age\n\n"
                            "The = sign is like an arrow pointing left:\n"
                            "    name  ←  \"Joshua\""
                        ),
                        'voice': (
                            "To make a variable, we use the equals sign. "
                            "name equals Joshua — this means put the word Joshua into a box called name. "
                            "age equals 5 — this means put the number 5 into a box called age. "
                            "The equals sign is like an arrow saying: put this thing into that box."
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Joining Words Together with print() 🔗',
                        'content': (
                            "You can put MORE than one thing inside print()!\n\n"
                            "Use a  ,  comma  to separate them:\n\n"
                            "    print(\"My name is\", name)\n\n"
                            "Python puts a space between them automatically! ✨\n\n"
                            "Try it! Put some words and a variable together."
                        ),
                        'voice': (
                            "You can put more than one thing inside print! "
                            "Use a comma to separate them. "
                            "Python puts a space between them automatically! "
                            "So print My name is comma name shows My name is Joshua!"
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Using Variables with print()',
                        'content': "We can use our variable inside print() to show what is in the box!",
                        'voice': "We can use our variable inside print to show what is inside the box!",
                        'code': (
                            'name = "Joshua"\n'
                            'age = 5\n'
                            'print(name)\n'
                            'print(age)\n'
                            'print("My name is", name)'
                        ),
                        'expected_output': 'Joshua\n5\nMy name is Joshua',
                    },
                    {
                        'type': 'exercise',
                        'title': 'Make Your Own Variables! 🎩',
                        'content': (
                            "Create two variables:\n\n"
                            "  1️⃣  name  — put YOUR name in it\n"
                            "  2️⃣  age   — put YOUR age in it\n\n"
                            "Then print them both out!"
                        ),
                        'voice': (
                            "Create two variables: name with your name inside, "
                            "and age with your age inside. Then print them both!"
                        ),
                        'starter_code': (
                            'name = "Joshua"\n'
                            'age = 5\n'
                            'print("My name is", name)\n'
                            'print("I am", age, "years old")'
                        ),
                        'prefill': True,
                        'expected_output': None,
                        'hints': [
                            'Text (words) go in speech marks: "like this"',
                            'Numbers do NOT need speech marks: age = 5',
                            'Try changing Joshua to your own name!',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Magic Quiz! 🎩',
                        'question': 'What symbol do we use to put something into a variable?',
                        'voice': 'Quiz! What symbol puts something into a variable?',
                        'options': ['➕  Plus sign +', '=  Equals sign =', '❓  Question mark ?', '⭐  Star *'],
                        'answer': 1,
                        'explanation': 'We use = to put things into variables. Like name = "Joshua"!',
                        'explanation_voice': 'Brilliant! We use the equals sign to put things into variables!',
                    },
                ],
            },
            {
                'id': 'j_m2_l2',
                'title': 'Changing Variables! 🔄',
                'icon': '🔄',
                'xp': 75,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Variables Can Change! 🔄',
                        'content': (
                            "The MAGIC thing about variables is that they can CHANGE!\n\n"
                            "Imagine your magic box 📦 has the number 5 in it.\n"
                            "You can REPLACE it with a new number!\n\n"
                            "    score = 0\n"
                            "    score = 10\n"
                            "    score = 25\n\n"
                            "Now score holds the number 25!\n\n"
                            "The old value is replaced — like swapping something in your box! 🔄"
                        ),
                        'voice': (
                            "The magic thing about variables is that they can change! "
                            "Imagine your magic box has the number 5 in it. "
                            "You can replace it with a new number! "
                            "Score equals zero, then score equals ten, then score equals twenty-five. "
                            "Now score holds twenty-five! The old value is replaced."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'A Score Counter',
                        'content': "Watch as the score changes in this program:",
                        'voice': "Watch as the score changes in this program!",
                        'code': (
                            'score = 0\n'
                            'print("Score:", score)\n'
                            'score = 10\n'
                            'print("Score:", score)\n'
                            'score = 15\n'
                            '# We gave score 5 more points!\n'
                            'print("Score:", score)'
                        ),
                        'expected_output': 'Score: 0\nScore: 10\nScore: 15',
                    },
                    {
                        'type': 'exercise',
                        'title': 'My Favourite Things! ⭐',
                        'content': (
                            "Make a variable called  favourite_colour\n"
                            "Start it as  'red'\n"
                            "Then change it to  'blue'\n"
                            "Print the colour both times!"
                        ),
                        'voice': (
                            "Make a variable called favourite colour, start it as red, "
                            "then change it to blue and print the colour both times!"
                        ),
                        'starter_code': (
                            'favourite_colour = "red"\n'
                            'print("My favourite colour is", favourite_colour)\n'
                            'favourite_colour = "blue"\n'
                            'print("Now my favourite colour is", favourite_colour)'
                        ),
                        'prefill': True,
                        'expected_output': None,
                        'hints': ['Change the colour names in the speech marks!'],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Quick Quiz!',
                        'question': 'If you put 3 in a box, then put 7 in the SAME box — what is in the box now?',
                        'voice': 'If you put 3 in a box, then put 7 in the same box — what is in the box now?',
                        'options': ['🔢  3', '🔢  10', '🔢  7', '🔢  0'],
                        'answer': 2,
                        'explanation': '7! The new value replaced the old one. Like swapping toys in your box!',
                        'explanation_voice': 'Correct! 7 is in the box. The new value replaced the old one. Like swapping toys!',
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 3: Ask and Answer 💬
    # ================================================================
    {
        'id': 'j_m3',
        'title': 'Ask and Answer 💬',
        'icon': '💬',
        'description': 'Make a program that asks you questions! 💬',
        'badge': 'Conversation Coder',
        'badge_icon': '💬',
        'color': '#A8E6CF',
        'prerequisite_modules': ['j_m2'],
        'lessons': [
            {
                'id': 'j_m3_l1',
                'title': 'Asking Questions with input()',
                'icon': '❓',
                'xp': 100,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Programs Can Ask Questions! ❓',
                        'content': (
                            "So far our programs just DO things.\n"
                            "But programs can also ASK for information!\n\n"
                            "We use  input()  to ask a question.\n"
                            "Whatever the user types gets stored in a variable.\n\n"
                            '    name = input("What is your name? ")\n'
                            '    print("Hello,", name)'
                        ),
                        'voice': (
                            "So far our programs just do things. "
                            "But programs can also ask for information! "
                            "We use input with brackets to ask a question. "
                            "Whatever the user types gets stored in a variable."
                        ),
                    },
                    {
                        'type': 'exercise',
                        'title': 'A Friendly Greeter!',
                        'content': (
                            "Write a program that:\n"
                            "  1️⃣  Asks for someone's name\n"
                            "  2️⃣  Says hello to them!\n\n"
                            "The code is almost ready — just press Run!"
                        ),
                        'voice': (
                            "Write a program that asks for someone's name and says hello to them. "
                            "The code is almost ready, just press Run!"
                        ),
                        'starter_code': (
                            'name = input("What is your name? ")\n'
                            'print("Hello,", name, "! Nice to meet you! 👋")'
                        ),
                        'prefill': True,
                        'expected_output': None,
                        'hints': ['Press Run and type your name when asked!'],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Input Quiz!',
                        'question': 'What does input() do?',
                        'voice': 'Quiz! What does input do?',
                        'options': [
                            '📺  Shows words on the screen',
                            '💬  Asks the user to type something',
                            '🔢  Does maths',
                            '🎵  Plays music',
                        ],
                        'answer': 1,
                        'explanation': 'input() asks the user to type something in. That answer goes into a variable!',
                        'explanation_voice': 'Correct! Input asks the user to type something, and stores their answer!',
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 4: Yes or No? 🤔
    # ================================================================
    {
        'id': 'j_m4',
        'title': 'Yes or No? 🤔',
        'icon': '🤔',
        'description': 'Teach your program to make decisions with if and else!',
        'assisted': True,
        'badge': 'Decision Maker',
        'badge_icon': '🤔',
        'color': '#FFD93D',
        'prerequisite_modules': ['j_m3'],
        'lessons': [
            {
                'id': 'j_m4_l1',
                'title': 'Making Decisions with if!',
                'icon': '↔️',
                'xp': 100,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Is It Raining? ☔',
                        'content': (
                            "Every day we make decisions:\n\n"
                            "  ☔  IF it is raining → take an umbrella\n"
                            "  ☀️  ELSE → leave the umbrella at home\n\n"
                            "Programs can make decisions too!\n\n"
                            "In Python we use  if  and  else\n"
                            "to tell the program WHAT to do in different situations."
                        ),
                        'voice': (
                            "Every day we make decisions! "
                            "If it is raining, take an umbrella. Otherwise, leave it at home. "
                            "Programs can make decisions too! "
                            "In Python we use if and else to tell the program what to do."
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'The if Statement',
                        'content': (
                            "Here is how if works in Python:\n\n"
                            '    colour = "red"\n'
                            '    if colour == "red":\n'
                            '        print("🍎 It is red!")\n'
                            "    else:\n"
                            '        print("It is a different colour!")\n\n'
                            "The  ==  means  'is it the same?'\n\n"
                            "🟡  See the GAP (spaces) before print?\n"
                            "    Python uses that gap to know what is inside the if!"
                        ),
                        'voice': (
                            "Here is how if works. We check something — like what colour it is. "
                            "If it is true, we run the code with the gap in front. "
                            "If it is false, we run the else part instead. "
                            "See the spaces before print? Python needs those — we call it the gap!"
                        ),
                    },
                    {
                        'type': 'exercise',
                        'title': 'The Password Checker! 🔑',
                        'content': (
                            "Let's make a simple password checker!\n\n"
                            "If the secret word is correct → say Welcome!\n"
                            "If it's wrong → say Try again!\n\n"
                            "Run the code and try entering  dragon  as the password!"
                        ),
                        'voice': (
                            "Let's make a password checker! "
                            "If the secret word is correct, say welcome. "
                            "If it is wrong, say try again. "
                            "Run the code and try entering dragon as the password!"
                        ),
                        'starter_code': (
                            'secret = "dragon"\n'
                            'guess = input("What is the secret word? ")\n'
                            'if guess == secret:\n'
                            '    print("🎉 Welcome! You know the secret!")\n'
                            'else:\n'
                            '    print("❌ Oops! That is not right. Try again!")'
                        ),
                        'prefill': True,
                        'expected_output': None,
                        'hints': [
                            'Try typing exactly: dragon',
                            'The == means "is it the same?" — make sure you have two equals signs!',
                            'Capital letters matter — dragon is different to Dragon!',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Decision Quiz!',
                        'question': 'In Python, what symbol checks if two things are EQUAL?',
                        'voice': 'Quiz! What symbol checks if two things are equal?',
                        'options': ['= (one equals)', '== (two equals)', '+ (plus sign)', '? (question mark)'],
                        'answer': 1,
                        'explanation': '== (double equals) checks if two things are equal. = (single) stores a value!',
                        'explanation_voice': 'Brilliant! Double equals checks if two things are equal. Single equals stores a value!',
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 5: Do It Again! 🔄
    # ================================================================
    {
        'id': 'j_m5',
        'title': 'Do It Again! 🔄',
        'icon': '🔄',
        'description': 'Make the computer repeat things over and over! 🔄',
        'assisted': True,
        'badge': 'Loop Master',
        'badge_icon': '🔄',
        'color': '#C3A4E8',
        'prerequisite_modules': ['j_m4'],
        'lessons': [
            {
                'id': 'j_m5_l1',
                'title': 'Loops — Repeat with for!',
                'icon': '🔁',
                'xp': 125,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Counting Sheep! 🐑',
                        'content': (
                            "Imagine you need to count 5 sheep 🐑🐑🐑🐑🐑\n\n"
                            "You could write:\n"
                            '    print("1 sheep")\n'
                            '    print("2 sheep")\n'
                            '    print("3 sheep")\n'
                            '    print("4 sheep")\n'
                            '    print("5 sheep")\n\n'
                            "But what if you need to count 100 sheep? 😅\n\n"
                            "There is a MUCH better way — a LOOP! 🔄\n"
                            "A loop makes the computer repeat things for you!"
                        ),
                        'voice': (
                            "Imagine you need to count 5 sheep. "
                            "You could write five separate print statements. "
                            "But what if you need to count 100 sheep? "
                            "There is a much better way — a loop! "
                            "A loop makes the computer repeat things for you!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'The for Loop',
                        'content': (
                            "A  for  loop repeats code a set number of times.\n\n"
                            "    for number in range(1, 6):\n"
                            "        print(number)\n\n"
                            "range(1, 6) counts: 1, 2, 3, 4, 5 🐑🐑🐑🐑🐑\n\n"
                            "(It stops just BEFORE 6!)\n\n"
                            "🟡  See the GAP before print?\n"
                            "    That tells Python what goes inside the loop!"
                        ),
                        'voice': (
                            "A for loop repeats code a set number of times. "
                            "For number in range 1 to 6 — this counts 1, 2, 3, 4, 5. "
                            "See the gap before print? That tells Python what goes inside the loop. "
                            "Range stops just before the last number!"
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Counting Sheep with range()! 🐑',
                        'content': (
                            "Let's count 3 sheep first — watch!\n\n"
                            "range(1, 4) counts: 1 🐑  2 🐑  3 🐑  STOP!\n\n"
                            "The last number is like a WALL 🧱\n"
                            "We stop BEFORE we hit it!"
                        ),
                        'voice': (
                            "Let's count 3 sheep first! "
                            "Range 1 to 4 counts 1, 2, 3 — then STOP! "
                            "The last number is like a wall. We stop before we hit it!"
                        ),
                        'code': (
                            'for number in range(1, 4):\n'
                            '    print(number, "🐑")'
                        ),
                        'expected_output': '1 🐑\n2 🐑\n3 🐑',
                    },
                    {
                        'type': 'exercise',
                        'title': 'Count to 10! 🔢',
                        'content': (
                            "Write a loop that counts from 1 to 10!\n\n"
                            "Hint:  range(1, 11)  counts from 1 up to 10\n"
                            "(range stops BEFORE the last number!)"
                        ),
                        'voice': (
                            "Write a loop that counts from 1 to 10! "
                            "Remember that range 1 comma 11 counts from 1 up to 10. "
                            "Range stops before the last number!"
                        ),
                        'starter_code': (
                            'for number in range(1, 11):\n'
                            '    print(number)'
                        ),
                        'prefill': True,
                        'expected_output': '1\n2\n3\n4\n5\n6\n7\n8\n9\n10',
                        'hints': [
                            'range(1, 11) starts at 1 and goes up to but not including 11',
                            'Make sure print(number) is indented with 4 spaces!',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Loop Quiz!',
                        'question': 'What does  range(1, 4)  count to?',
                        'voice': 'Quiz! What does range 1 to 4 count?',
                        'options': ['🔢  1, 2, 3, 4', '🔢  1, 2, 3', '🔢  0, 1, 2, 3', '🔢  4, 3, 2, 1'],
                        'answer': 1,
                        'explanation': 'range(1, 4) counts 1, 2, 3 — it stops BEFORE 4!',
                        'explanation_voice': 'Correct! Range 1 to 4 gives 1, 2, 3 — it stops just before the last number!',
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 6: My First Game! 🎮
    # ================================================================
    {
        'id': 'j_m6',
        'title': 'My First Game! 🎮',
        'icon': '🎮',
        'description': "Put it all together and build your first game — a number guessing game!",
        'assisted': True,
        'badge': 'Game Creator',
        'badge_icon': '🎮',
        'color': '#FF8B8B',
        'prerequisite_modules': ['j_m5'],
        'lessons': [
            {
                'id': 'j_m6_l1',
                'title': 'Number Guessing Game! 🎲',
                'icon': '🎲',
                'xp': 200,
                'steps': [
                    {
                        'type': 'story',
                        'title': "You're Going to Make a GAME! 🎉",
                        'content': (
                            "🎉 AMAZING! You have learned so much!\n\n"
                            "  ✅  Variables (magic boxes)\n"
                            "  ✅  print() and input()\n"
                            "  ✅  if / else decisions\n"
                            "  ✅  for loops\n\n"
                            "Now let's use ALL of it to build a REAL game! 🎮"
                        ),
                        'voice': (
                            "Amazing! You have learned so much! Variables, print and input, "
                            "if else decisions, and loops! "
                            "Now let's use ALL of it to build a real game!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'The Guessing Game Plan 🎲',
                        'content': (
                            "Here is how our game will work:\n\n"
                            "  🎲  The computer has a SECRET number\n"
                            "  ❓  YOU type a guess\n"
                            "  ✅  If you are RIGHT — you win! 🏆\n"
                            "  ❌  If you are WRONG — try again!\n\n"
                            "We already know everything we need:\n"
                            "  •  input() to ask for a guess\n"
                            "  •  if / else to check the answer"
                        ),
                        'voice': (
                            "Here is how our game works. "
                            "The computer has a secret number. You type a guess. "
                            "If you are right, you win! If you are wrong, try again! "
                            "We already know everything we need — input and if and else!"
                        ),
                    },
                    {
                        'type': 'exercise',
                        'title': 'Build the Guessing Game! 🎮',
                        'content': (
                            "The secret number is 7! 🤫\n\n"
                            "Type a number and press RUN to play!\n\n"
                            "Can you guess it? 🏆"
                        ),
                        'voice': (
                            "The secret number is 7 — but shh, don't tell! "
                            "Type a number and press Run to play! "
                            "Can you guess it?"
                        ),
                        'starter_code': (
                            'secret = 7\n'
                            'print("🎲 I am thinking of a number between 1 and 10!")\n'
                            '\n'
                            'guess = input("What is your guess? ")\n'
                            '\n'
                            'if guess == str(secret):\n'
                            '    print("🎉 YES! You got it! Amazing! 🏆")\n'
                            'else:\n'
                            '    print(f"❌ Not quite! The number was {secret}. Try again! 😊")'
                        ),
                        'prefill': True,
                        'expected_output': None,
                        'hints': [
                            'Try typing: 7 — that is the secret number!',
                            'Try typing a different number to see what happens!',
                            'Ask a grown-up to help you change the secret number!',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Final Quiz! 🏆',
                        'question': 'What does  input()  do in our game?',
                        'voice': 'Final quiz! What does input do in our guessing game?',
                        'options': [
                            '🎲  Picks a random number',
                            '💬  Asks the player to type something',
                            '📺  Shows the answer on screen',
                            '🔊  Makes a sound',
                        ],
                        'answer': 1,
                        'explanation': 'input() asks the player to type something — their guess! We learned this in Module 3.',
                        'explanation_voice': 'That is right! Input asks the player to type their guess. You remembered! Well done!',
                    },
                ],
            },
        ],
    },
]
