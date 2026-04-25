"""
Toby's Curriculum - Age 10

11 Modules from Python basics through to Game Development:
  M1:  Python Foundations      - Variables, types, I/O, maths, f-strings       (fully built)
  M2:  Making Decisions        - if/elif/else, nested conditionals, logic       (fully built)
  M3:  Loops                   - for, while, range, break/continue              (fully built)
  M4:  Functions               - def, parameters, return, scope                 (fully built)
  M5:  Data Structures         - list, dict, tuple, set                         (fully built)
  M6:  Object-Oriented Python  - classes, init, self, inheritance, OOP project  (fully built)
  M7:  Files & Exceptions      - file I/O, try/except, modules                  (stub)
  M8:  Networking Basics       - internet, HTTP, APIs (conceptual + requests)   (stub)
  M9:  Azure Fundamentals      - Cloud, Azure services, deploying (conceptual)  (stub)
  M10: Introduction to AI/ML   - What is AI, data, ML concepts, ethics          (stub)
  M11: Game Development        - text-based games, ASCII art, dungeon crawler   (fully built)
"""

# ---------------------------------------------------------------------------
# Helper: stub module builder (for modules 4-11 that have an overview lesson)
# ---------------------------------------------------------------------------

def _stub_module(module_id, title, icon, description, badge, badge_icon, color,
                 prereqs, overview_content, overview_voice, coming_soon_lessons):
    """Creates a module with one overview lesson and coming-soon placeholders."""
    lessons = [
        {
            'id': f'{module_id}_l1',
            'title': f'{title} — Overview',
            'icon': icon,
            'xp': 50,
            'steps': [
                {
                    'type': 'teach',
                    'title': f'Welcome to {title}',
                    'content': overview_content,
                    'voice': overview_voice,
                },
                {
                    'type': 'teach',
                    'title': '🔜 Coming Next…',
                    'content': (
                        "This module is being built! Here is what is coming:\n\n"
                        + '\n'.join(f'  • {ls}' for ls in coming_soon_lessons)
                        + "\n\nKeep completing earlier modules to unlock more content!"
                    ),
                    'voice': (
                        f"This module is being built! More lessons for {title} are coming soon. "
                        "Keep completing earlier modules!"
                    ),
                },
            ],
        }
    ]
    return {
        'id': module_id,
        'title': title,
        'icon': icon,
        'description': description,
        'badge': badge,
        'badge_icon': badge_icon,
        'color': color,
        'prerequisite_modules': prereqs,
        'lessons': lessons,
    }


TOBY_MODULES = [
    # ================================================================
    # MODULE 1: Python Foundations
    # ================================================================
    {
        'id': 't_m1',
        'title': 'Python Foundations 🐍',
        'icon': '🐍',
        'description': 'Master variables, data types, maths, and user input in Python.',
        'badge': 'Python Starter',
        'badge_icon': '🐍',
        'color': '#00B4D8',
        'prerequisite_modules': [],
        'lessons': [
            # ---- Lesson 1: Variables & Data Types ----
            {
                'id': 't_m1_l1',
                'title': 'Variables & Data Types',
                'icon': '📦',
                'xp': 100,
                'steps': [
                    {
                        'type': 'story',
                        'title': '🚀 Mission Briefing — Python Foundations',
                        'content': (
                            "Welcome to Python HQ, Agent Toby! 🕵️\n\n"
                            "Your mission: master the core building blocks of Python.\n\n"
                            "Every program ever written — from Minecraft to Instagram to AI —\n"
                            "starts with the same basics you are about to learn.\n\n"
                            "Complete all three Foundation lessons and you will earn the\n"
                            "🐍 Python Starter badge and unlock the next module.\n\n"
                            "Ready? Your coding adventure starts NOW."
                        ),
                        'voice': (
                            "Welcome to Python HQ, Agent Toby! "
                            "Your mission: master the core building blocks of Python. "
                            "Every program ever written — from Minecraft to Instagram to AI — "
                            "starts with the same basics you are about to learn. "
                            "Ready? Your coding adventure starts now!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Variables Store Information',
                        'content': (
                            "In Python, a variable is a named container for data.\n\n"
                            "    name = \"Toby\"       # str  (text)\n"
                            "    age  = 10            # int  (whole number)\n"
                            "    height = 1.45        # float (decimal number)\n"
                            "    is_cool = True       # bool  (True or False)\n\n"
                            "Python figures out the TYPE automatically — nice!\n\n"
                            "Variable naming rules:\n"
                            "  ✅  snake_case for names (e.g. my_name)\n"
                            "  ✅  Start with a letter or _\n"
                            "  ❌  No spaces, no starting with a number\n"
                            "  ❌  No Python keywords (if, for, while, ...)"
                        ),
                        'voice': (
                            "In Python, a variable is a named container for data. "
                            "You can store text — called a string — whole numbers called integers, "
                            "decimal numbers called floats, and True or False values called booleans. "
                            "Python figures out the type automatically. "
                            "Use snake case for variable names — words joined with underscores."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Data Types in Action',
                        'content': "Let's look at different data types and how to check them:",
                        'voice': "Let's look at different data types and how to check them.",
                        'code': (
                            'name = "Toby"\n'
                            'age = 10\n'
                            'height = 1.45\n'
                            'is_brilliant = True\n'
                            '\n'
                            'print(type(name))        # <class str>\n'
                            'print(type(age))         # <class int>\n'
                            'print(type(height))      # <class float>\n'
                            'print(type(is_brilliant)) # <class bool>\n'
                            '\n'
                            '# Convert between types\n'
                            'age_text = str(age)      # 10 -> "10"\n'
                            'score = int("42")        # "42" -> 42\n'
                            'print("I am", age_text, "years old")'
                        ),
                        'expected_output': (
                            "<class 'str'>\n<class 'int'>\n"
                            "<class 'float'>\n<class 'bool'>\nI am 10 years old"
                        ),
                    },
                    {
                        'type': 'exercise',
                        'title': 'Personal Profile Program',
                        'content': (
                            "Create variables for yourself and print a nice profile.\n\n"
                            "The variables are set up — YOUR JOB is to write the print statements!\n\n"
                            "Requirements:\n"
                            "  1. Print the name using an f-string\n"
                            "  2. Print the age with 'years old' after it\n"
                            "  3. Print the height with 'm' after it\n"
                            "  4. Print whether you are a coder\n\n"
                            "f-string hint: f\"Hello {name}\" puts the variable inside the string."
                        ),
                        'voice': (
                            "Your turn! The variables are already set up — "
                            "your job is to write the four print statements using f-strings. "
                            "An f-string starts with the letter f before the quote, "
                            "and you put the variable name inside curly braces."
                        ),
                        'starter_code': (
                            '# Variables are set up — YOUR JOB: write the 4 print statements!\n'
                            'name = "Toby"        # change to YOUR name\n'
                            'age = 10             # change to YOUR age\n'
                            'height = 1.45        # your height in metres\n'
                            'is_coder = True\n'
                            '\n'
                            '# Write your print statements below using f-strings:\n'
                            '# Example: print(f"Name: {name}")\n'
                            '\n'
                            '# YOUR CODE HERE:\n'
                        ),
                        'expected_output': None,
                        'hints': [
                            'f-strings start with f before the quote: f"Hello {name}"',
                            'Put the variable name inside curly braces: {age}',
                            'You need 4 print() calls — one for each variable',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Data Types Quiz',
                        'question': 'Which data type holds the value  3.14 ?',
                        'voice': 'Quiz! Which data type holds the value 3.14?',
                        'options': ['str', 'int', 'float', 'bool'],
                        'answer': 2,
                        'explanation': '3.14 is a decimal number, so it is a float. int is whole numbers only.',
                        'explanation_voice': 'Correct! 3.14 is a float — a decimal number. Great work!',
                    },
                ],
            },

            # ---- Lesson 2: Maths & Operators ----
            {
                'id': 't_m1_l2',
                'title': 'Maths & Operators',
                'icon': '🧮',
                'xp': 100,
                'steps': [
                    {
                        'type': 'teach',
                        'title': "Python's Arithmetic Operators",
                        'content': (
                            "Python can do maths easily:\n\n"
                            "    +    Addition          5 + 3 = 8\n"
                            "    -    Subtraction       10 - 4 = 6\n"
                            "    *    Multiplication    6 * 7 = 42\n"
                            "    /    Division          10 / 4 = 2.5\n"
                            "    //   Floor Division    10 // 3 = 3 (no remainder)\n"
                            "    %    Modulus           10 % 3 = 1 (remainder only)\n"
                            "    **   Power             2 ** 8 = 256\n\n"
                            "Modulus (%) is super useful — it tells you the REMAINDER.\n"
                            "It is perfect for checking if a number is odd or even!"
                        ),
                        'voice': (
                            "Python has all the arithmetic operators you know from maths, "
                            "plus a few extras. Floor division gives the whole number part only. "
                            "Modulus gives you the remainder. Double star is power — two to the eight is 256! "
                            "Modulus is super useful for checking if a number is odd or even."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Operators in Practice',
                        'content': '',
                        'voice': 'Here are some operator examples to try.',
                        'code': (
                            'a = 17\n'
                            'b = 5\n'
                            'print(f"{a} + {b} = {a + b}")\n'
                            'print(f"{a} - {b} = {a - b}")\n'
                            'print(f"{a} * {b} = {a * b}")\n'
                            'print(f"{a} / {b} = {a / b}")\n'
                            'print(f"{a} // {b} = {a // b}  (floor)")\n'
                            'print(f"{a} % {b} = {a % b}   (remainder)")\n'
                            'print(f"2 ** 10 = {2 ** 10}  (2 to the power 10)")\n'
                            '\n'
                            '# Odd or even check (you will learn if/else in Module 2!):\n'
                            'num = 42\n'
                            'remainder = num % 2\n'
                            'print(f"{num} divided by 2 has remainder {remainder}")\n'
                            '# If remainder is 0, the number is even!'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Build a Calculator!',
                        'content': (
                            "Build a mini calculator that:\n"
                            "  1. Asks for two numbers\n"
                            "  2. Prints the result of +, -, *, /\n"
                            "  3. BONUS: also shows // and %\n\n"
                            "Note: input() always returns a string —\n"
                            "use  float()  to convert it to a number!"
                        ),
                        'voice': (
                            "Build a mini calculator that asks for two numbers and shows all the operations. "
                            "Remember: input always returns a string, so use float to convert it to a number!"
                        ),
                        'starter_code': (
                            'a = float(input("Enter first number: "))\n'
                            'b = float(input("Enter second number: "))\n'
                            '\n'
                            'print(f"{a} + {b} = {a + b}")\n'
                            'print(f"{a} - {b} = {a - b}")\n'
                            'print(f"{a} * {b} = {a * b}")\n'
                            'print(f"{a} / {b} = {a / b}")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Use float() not int() so decimal numbers work too',
                            'Try dividing by zero — what happens?',
                            'BONUS: Add if b != 0: before the division to prevent errors!',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Operators Quiz',
                        'question': "What is the result of  17 % 5 ?",
                        'voice': 'Quiz! What is 17 modulo 5?',
                        'options': ['3', '2', '3.4', '85'],
                        'answer': 1,
                        'explanation': '17 = (5 × 3) + 2 — the remainder is 2. So 17 % 5 = 2.',
                        'explanation_voice': 'Correct! 17 divided by 5 is 3 remainder 2, so 17 modulo 5 equals 2!',
                    },
                ],
            },

            # ---- Lesson 3: Input, Output & Strings ----
            {
                'id': 't_m1_l3',
                'title': 'Input, Output & Strings',
                'icon': '💬',
                'xp': 100,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Working with Strings',
                        'content': (
                            "Strings are sequences of characters.\n\n"
                            '    s = "Hello, World!"\n'
                            "    len(s)           # 13 — length\n"
                            '    s.upper()        # "HELLO, WORLD!"\n'
                            '    s.lower()        # "hello, world!"\n'
                            '    s.replace("World", "Toby")  # "Hello, Toby!"\n'
                            '    s[0]             # "H"  — indexing starts at 0!\n'
                            '    s[7:12]          # "World"  — slicing\n'
                            '    "Hello" + " " + "Toby"  # Concatenation\n\n'
                            "f-strings (formatted strings) are the modern way to\n"
                            "embed values in text:\n\n"
                            '    name = "Toby"\n'
                            '    age = 10\n'
                            '    print(f"Hi {name}, you are {age} years old!")'
                        ),
                        'voice': (
                            "Strings are sequences of characters. "
                            "You can find their length, convert to upper or lower case, "
                            "replace parts, and slice out portions. "
                            "Indexing starts at zero — the first character is index zero. "
                            "F-strings are the modern way to embed values directly in text strings."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'String Methods in Action',
                        'content': "Watch these string operations run — then try changing the string!",
                        'voice': "Watch these string methods in action, then try changing the string yourself.",
                        'code': (
                            's = "Hello, World!"\n'
                            'print(s.upper())                    # HELLO, WORLD!\n'
                            'print(s.lower())                    # hello, world!\n'
                            'print(len(s))                       # 13\n'
                            'print(s[7:12])                      # World  (index 7 up to 12)\n'
                            'print(s.replace("World", "Toby"))   # Hello, Toby!\n'
                            'print("World" in s)                 # True\n'
                            '\n'
                            'name = "Toby"\n'
                            'age = 10\n'
                            'print(f"Hi {name}, you are {age} years old!")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'String Analyser',
                        'content': (
                            "Write a program that:\n"
                            "  1. Asks the user to enter a sentence\n"
                            "  2. Prints the sentence in UPPERCASE\n"
                            "  3. Prints the number of characters\n"
                            "  4. Prints whether it contains the word 'Python'\n"
                        ),
                        'voice': (
                            "Write a string analyser. Ask for a sentence, print it in uppercase, "
                            "show its length, and check whether it contains the word Python."
                        ),
                        'starter_code': (
                            'sentence = input("Enter a sentence: ")\n'
                            '\n'
                            '# YOUR CODE BELOW:\n'
                            '# 1. Print the sentence in UPPERCASE using .upper()\n'
                            '# 2. Print how many characters it has using len()\n'
                            '# 3. Print whether it contains the word "Python"\n'
                            '#    Hint: use  "Python" in sentence\n'
                        ),
                        'expected_output': None,
                        'hints': [
                            '"Python" in sentence checks if the word Python appears',
                            'Try typing: I love Python programming',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'String Quiz',
                        'question': 'What is the index of the FIRST character in a Python string?',
                        'voice': 'Quiz! What is the index of the first character in a Python string?',
                        'options': ['1', '0', '-1', 'It depends'],
                        'answer': 1,
                        'explanation': 'Python (like most languages) uses zero-based indexing. s[0] is the first character.',
                        'explanation_voice': 'Correct! Python uses zero-based indexing. The first character is always at index zero.',
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 2: Making Decisions
    # ================================================================
    {
        'id': 't_m2',
        'title': 'Making Decisions 🔀',
        'icon': '🔀',
        'description': 'Use if, elif, and else to control your program\'s flow.',
        'badge': 'Logic Thinker',
        'badge_icon': '🔀',
        'color': '#F7B731',
        'prerequisite_modules': ['t_m1'],
        'lessons': [
            {
                'id': 't_m2_l1',
                'title': 'if, elif, else',
                'icon': '↔️',
                'xp': 125,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Mission: Decision Engine 🕵️',
                        'content': (
                            "Agent Toby — your programs need to make CHOICES.\n\n"
                            "A weather app chooses what to display.\n"
                            "A game decides if you win or lose.\n"
                            "A ticket machine calculates your price.\n\n"
                            "All of this is powered by one idea:\n"
                            "    if this... elif that... else otherwise\n\n"
                            "Master conditional statements and your programs\n"
                            "can respond intelligently to any situation! 🧠"
                        ),
                        'voice': (
                            "Agent Toby — your programs need to make choices. "
                            "A weather app, a game, a ticket machine — all powered by if, elif, else. "
                            "Master conditional statements and your programs can respond to anything!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Conditional Statements',
                        'content': (
                            "Conditional statements let your program choose what to do.\n\n"
                            "    if condition:\n"
                            "        # runs when condition is True\n"
                            "    elif another_condition:\n"
                            "        # runs when first is False but this is True\n"
                            "    else:\n"
                            "        # runs when all conditions are False\n\n"
                            "Comparison operators:\n"
                            "    ==   equal to\n"
                            "    !=   not equal to\n"
                            "    <    less than\n"
                            "    >    greater than\n"
                            "    <=   less than or equal to\n"
                            "    >=   greater than or equal to\n\n"
                            "Logical operators:\n"
                            "    and    both must be True\n"
                            "    or     at least one must be True\n"
                            "    not    flips True to False"
                        ),
                        'voice': (
                            "Conditional statements let your program choose what to do. "
                            "If the condition is true, the first block runs. "
                            "Elif checks another condition if the first was false. "
                            "Else runs when everything else is false. "
                            "You can combine conditions with and, or, and not."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Grade Calculator',
                        'content': "A classic use of if/elif/else — calculating letter grades:",
                        'voice': "Here is a classic example — a grade calculator using if, elif, and else.",
                        'code': (
                            'score = int(input("Enter your score (0-100): "))\n'
                            '\n'
                            'if score >= 90:\n'
                            '    grade = "A ⭐"\n'
                            'elif score >= 80:\n'
                            '    grade = "B 👍"\n'
                            'elif score >= 70:\n'
                            '    grade = "C 🙂"\n'
                            'elif score >= 60:\n'
                            '    grade = "D 😐"\n'
                            'else:\n'
                            '    grade = "F — Keep trying! 💪"\n'
                            '\n'
                            'print(f"Your grade: {grade}")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Age-Based Ticket Pricer',
                        'content': (
                            "Build a cinema ticket price calculator:\n\n"
                            "  Under 5:   FREE 🎉\n"
                            "  5 to 12:   £5.00 (child)\n"
                            "  13 to 17:  £8.00 (teen)\n"
                            "  18 to 64:  £12.00 (adult)\n"
                            "  65+:       £6.00 (senior)\n\n"
                            "Use if/elif/else and f-strings for the output."
                        ),
                        'voice': (
                            "Build a cinema ticket price calculator with different prices for each age group: "
                            "free for under 5, five pounds for children, eight for teens, "
                            "twelve for adults, and six for seniors."
                        ),
                        'starter_code': (
                            'age = int(input("Enter your age: "))\n'
                            '\n'
                            '# Default values (your code will overwrite these):\n'
                            'price = 0\n'
                            'category = "Unknown"\n'
                            '\n'
                            '# DONE FOR YOU — the first branch as a model:\n'
                            'if age < 5:\n'
                            '    price = 0\n'
                            '    category = "Child (Free!)"\n'
                            '\n'
                            '# YOUR CODE: add elif branches for 5-12, 13-17, 18-64, and 65+\n'
                            '# Prices: £5, £8, £12, £6\n'
                            '\n'
                            'print(f"Category: {category}")\n'
                            'print(f"Ticket price: £{price:.2f}")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Use <= (less than or equal) for range checks',
                            '{price:.2f} in an f-string shows 2 decimal places',
                            'Try age = 10, then 0, then 70',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Logic Quiz',
                        'question': 'What does  (5 > 3) and (10 < 8)  evaluate to?',
                        'voice': 'Quiz! What does 5 greater than 3 AND 10 less than 8 evaluate to?',
                        'options': ['True', 'False', 'Error', 'None'],
                        'answer': 1,
                        'explanation': '5 > 3 is True. 10 < 8 is False. True AND False = False. Both must be True for "and" to be True.',
                        'explanation_voice': '5 greater than 3 is True, but 10 less than 8 is False. True AND False equals False!',
                    },
                ],
            },

            # ---- Lesson 2: Nested Conditionals & Project ----
            {
                'id': 't_m2_l2',
                'title': 'Nested if & Complex Logic',
                'icon': '🧩',
                'xp': 150,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Mission: Logic Architect 🧠',
                        'content': (
                            "Agent Toby — time to level up your logic.\n\n"
                            "Real software makes LAYERS of decisions:\n"
                            "  A sat-nav checks the road, then traffic, then weather.\n"
                            "  A game checks your health, your inventory, AND the enemy.\n\n"
                            "This is called NESTED logic — decisions inside decisions.\n"
                            "Master this and you can build anything. 🏗️"
                        ),
                        'voice': (
                            "Agent Toby, time to level up your logic. "
                            "Real software makes layers of decisions — nested logic. "
                            "Master this and you can build anything!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Nested if & Complex Conditions',
                        'content': (
                            "Nested if — an if inside another if:\n\n"
                            "    if has_ticket:\n"
                            "        if age >= 18:\n"
                            "            print('Welcome to the film!')\n"
                            "        else:\n"
                            "            print('Sorry, 18+ only.')\n"
                            "    else:\n"
                            "        print('Buy a ticket first!')\n\n"
                            "Guard clauses — check edge cases first:\n\n"
                            "    if not username:\n"
                            "        print('Error: no username')\n"
                            "    elif len(username) < 3:\n"
                            "        print('Username too short')\n"
                            "    else:\n"
                            "        print(f'Welcome, {username}!')\n\n"
                            "Combining conditions:\n"
                            "    if temp > 30 and humidity > 80:\n"
                            "        print('Tropical!')\n\n"
                            "Truthiness — these are 'falsy' in Python:\n"
                            "    False, 0, '', [], {}, None\n"
                            "Everything else is 'truthy'."
                        ),
                        'voice': (
                            "Nested if means putting an if inside another if — decisions within decisions. "
                            "Guard clauses check edge cases first so the main logic stays clean. "
                            "You can combine conditions with and, or, and not. "
                            "Python also has truthiness — zero, empty strings, and empty lists count as false."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Temperature Advisor',
                        'content': 'A weather advisor with nested conditions for temperature, rain and wind:',
                        'voice': 'Here is a temperature advisor with nested conditions for weather.',
                        'code': (
                            'temp = 22\n'
                            'raining = True\n'
                            'wind_speed = 35\n'
                            '\n'
                            'if temp < 10:\n'
                            '    advice = "Cold! Wear a coat. 🧥"\n'
                            '    if raining:\n'
                            '        advice += " And grab an umbrella! ☂️"\n'
                            '    if wind_speed > 40:\n'
                            '        advice += " Watch out — it is windy! 💨"\n'
                            'elif temp < 25:\n'
                            '    advice = "Nice and warm. 😎"\n'
                            '    if raining:\n'
                            '        advice += " Light rain — maybe a jacket."\n'
                            '    if wind_speed > 30:\n'
                            '        advice += " A bit breezy today!"\n'
                            'else:\n'
                            '    advice = "Hot! Stay hydrated! 🥤"\n'
                            '    if raining:\n'
                            '        advice += " Warm rain — unusual!"\n'
                            '\n'
                            'print(f"Temperature: {temp}°C")\n'
                            'print(f"Raining: {raining}")\n'
                            'print(f"Wind: {wind_speed} mph")\n'
                            'print(f"Advice: {advice}")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Adventure Game Decision Tree 🗺️',
                        'content': (
                            "Build a text adventure with nested decisions!\n\n"
                            "The player explores a dungeon and faces choices:\n"
                            "  1. Choose a path (left, right, or straight)\n"
                            "  2. Each path has a sub-choice\n"
                            "  3. Each combination gives a different outcome\n\n"
                            "Complete the branches marked with TODO comments."
                        ),
                        'voice': (
                            "Build a text adventure with nested decisions! "
                            "The player chooses a path, then faces a sub-choice. "
                            "Complete all the branches to finish the adventure!"
                        ),
                        'starter_code': (
                            'import random\n'
                            '\n'
                            'print("=== DUNGEON ADVENTURE ===")\n'
                            'print("You enter a dark dungeon...")\n'
                            'print("Three tunnels stretch ahead.")\n'
                            '\n'
                            'path = random.choice(["left", "right", "straight"])\n'
                            'has_torch = random.choice([True, False])\n'
                            'print(f"\\nYou go {path}. Torch: {has_torch}")\n'
                            '\n'
                            'if path == "left":\n'
                            '    print("You find a treasure chest!")\n'
                            '    if has_torch:\n'
                            '        print("Your torch reveals it is REAL gold! 💰")\n'
                            '        print("You win 100 coins!")\n'
                            '    else:\n'
                            '        print("It is too dark to see inside...")\n'
                            '        print("You take a handful and hope for the best.")\n'
                            '\n'
                            'elif path == "right":\n'
                            '    # TODO: A monster blocks the way!\n'
                            '    # If has_torch, you scare it away and find a secret door\n'
                            '    # If no torch, you must sneak past (50/50 chance with random)\n'
                            '    pass\n'
                            '\n'
                            'else:  # straight\n'
                            '    # TODO: You find a locked door with a riddle\n'
                            '    # Pick a random number 1-3 as the answer\n'
                            '    # If the number is 1, you solve it and escape\n'
                            '    # Otherwise, a trapdoor opens!\n'
                            '    # If has_torch, you see the trapdoor and dodge it\n'
                            '    # If no torch, you fall but survive\n'
                            '    pass\n'
                            '\n'
                            'print("\\n=== ADVENTURE COMPLETE ===")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Replace pass with your if/else blocks',
                            'Use random.choice([True, False]) for a 50/50 chance',
                            'Nest an if inside the else for the trapdoor scenario',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Logic Quiz',
                        'question': 'What does  not (True and False)  evaluate to?',
                        'voice': 'Quiz! What does not, open bracket, True and False, close bracket, evaluate to?',
                        'options': ['True', 'False', 'None', 'Error'],
                        'answer': 0,
                        'explanation': (
                            'True and False = False. '
                            'not False = True. '
                            'The not operator flips the result!'
                        ),
                        'explanation_voice': (
                            'True and False gives False. Then not False gives True. '
                            'The not operator flips the result!'
                        ),
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 3: Loops — Power of Repetition
    # ================================================================
    {
        'id': 't_m3',
        'title': 'Loops 🔁',
        'icon': '🔁',
        'description': 'Master for loops, while loops, and the art of iteration.',
        'badge': 'Loop Engineer',
        'badge_icon': '🔁',
        'color': '#6BCB77',
        'prerequisite_modules': ['t_m1', 't_m2'],
        'lessons': [
            {
                'id': 't_m3_l1',
                'title': 'for Loops & range()',
                'icon': '🔢',
                'xp': 125,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Mission: Loop Engineer 🔄',
                        'content': (
                            "Agent Toby — automate EVERYTHING.\n\n"
                            "Printing the 12 times table by hand? 12 lines.\n"
                            "Checking 1000 passwords? 1000 lines.\n"
                            "With a loop — just 3 lines. Every time. ⚡\n\n"
                            "Loops are one of the most powerful ideas in all of programming.\n"
                            "Games, AI, simulations — they all run on loops.\n\n"
                            "Let's master them! 🏆"
                        ),
                        'voice': (
                            "Agent Toby — automate everything. "
                            "Printing a times table by hand takes 12 lines. "
                            "With a loop — just 3 lines, every time. "
                            "Games, AI, simulations — they all run on loops. "
                            "Let's master them!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'for Loops in Python',
                        'content': (
                            "A for loop iterates over a sequence.\n\n"
                            "    for variable in sequence:\n"
                            "        # code runs for each item\n\n"
                            "range() creates a number sequence:\n"
                            "    range(5)        → 0, 1, 2, 3, 4\n"
                            "    range(1, 6)     → 1, 2, 3, 4, 5\n"
                            "    range(0, 10, 2) → 0, 2, 4, 6, 8 (step of 2)\n"
                            "    range(10, 0, -1)→ 10, 9, 8 ... 1 (count down)\n\n"
                            "Other useful patterns:\n"
                            "    for char in 'Python':   # iterate over a string\n"
                            "    for i, val in enumerate(my_list):  # index + value\n\n"
                            "break  → exit the loop early\n"
                            "continue → skip to the next iteration"
                        ),
                        'voice': (
                            "A for loop runs a block of code for each item in a sequence. "
                            "range creates number sequences. "
                            "range 5 gives zero to four. "
                            "range 1 comma 6 gives one to five. "
                            "You can also iterate over strings and use enumerate to get index and value together. "
                            "Break exits the loop early. Continue skips to the next iteration."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Loops in Practice',
                        'content': '',
                        'voice': 'Here are some practical for loop examples.',
                        'code': (
                            '# Times table\n'
                            'n = 7\n'
                            'print(f"--- {n} Times Table ---")\n'
                            'for i in range(1, 13):\n'
                            '    print(f"{n} x {i} = {n * i}")\n'
                            '\n'
                            '# Find first number divisible by both 3 and 7\n'
                            'for num in range(1, 100):\n'
                            '    if num % 3 == 0 and num % 7 == 0:\n'
                            '        print(f"First multiple of 3 AND 7: {num}")\n'
                            '        break'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Times Table Warm-up! 🔢',
                        'content': (
                            "Before FizzBuzz, let's warm up with a simpler loop challenge!\n\n"
                            "Print all multiples of 7 up to 70:\n"
                            "  7, 14, 21, 28 ... 70\n\n"
                            "Use range() with a step of 7, or use % inside the loop!"
                        ),
                        'voice': (
                            "Before FizzBuzz, let's warm up! "
                            "Print all multiples of 7 up to 70. "
                            "You can use range with a step, or check using percent inside the loop."
                        ),
                        'starter_code': (
                            'print("Multiples of 7:")\n'
                            'for num in range(7, 71, 7):\n'
                            '    # YOUR CODE: print the number\n'
                            '    pass'
                        ),
                        'expected_output': None,
                        'hints': [
                            'range(7, 71, 7) starts at 7, goes to 70, steps by 7',
                            'Just print(num) inside the loop!',
                        ],
                    },
                    {
                        'type': 'exercise',
                        'title': 'FizzBuzz — The Classic!',
                        'content': (
                            "FizzBuzz is a famous coding puzzle that trips up even adults!\n\n"
                            "Print numbers 1 to 30, but:\n"
                            "  • If divisible by 3 → print 'Fizz'\n"
                            "  • If divisible by 5 → print 'Buzz'\n"
                            "  • If divisible by BOTH → print 'FizzBuzz'\n"
                            "  • Otherwise → print the number\n\n"
                            "The loop is set up — YOU write the if/elif/else inside it!"
                        ),
                        'voice': (
                            "FizzBuzz is a famous coding puzzle that trips up even adults! "
                            "The loop is set up for you — your job is to write the if statements inside it. "
                            "Use percent to check if a number divides evenly. "
                            "Remember: check for FizzBuzz first — both conditions together!"
                        ),
                        'starter_code': (
                            'for num in range(1, 31):\n'
                            '    # YOUR CODE HERE\n'
                            '    # Check if num is divisible by both 3 AND 5 first!\n'
                            '    # Then check for just 3, then just 5, then else print num\n'
                            '    pass  # remove this line when you start writing'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Use % to check divisibility: num % 3 == 0 means divisible by 3',
                            'Check the FizzBuzz case FIRST (both 3 and 5): if num % 3 == 0 and num % 5 == 0',
                            'The structure is: if ... elif ... elif ... else print(num)',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Loops Quiz',
                        'question': 'What does  break  do inside a loop?',
                        'voice': 'Quiz! What does the break statement do inside a loop?',
                        'options': [
                            'Skips to the next iteration',
                            'Exits the loop immediately',
                            'Causes a syntax error',
                            'Pauses the loop for 1 second',
                        ],
                        'answer': 1,
                        'explanation': 'break exits the loop immediately. continue skips to the next iteration.',
                        'explanation_voice': 'Correct! Break exits the loop immediately. Continue just skips to the next one.',
                    },
                ],
            },
            {
                'id': 't_m3_l2',
                'title': 'while Loops',
                'icon': '⏳',
                'xp': 125,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'while Loops',
                        'content': (
                            "A while loop keeps running as long as a condition is True.\n\n"
                            "    while condition:\n"
                            "        # code to repeat\n\n"
                            "Use while when you do not know in advance how many times\n"
                            "the loop will run.\n\n"
                            "⚠️  ALWAYS make sure the condition will eventually become\n"
                            "False — otherwise you get an INFINITE LOOP! 😱\n\n"
                            "    count = 0\n"
                            "    while count < 5:\n"
                            "        print(count)\n"
                            "        count += 1    # count = count + 1\n\n"
                            "    # while True: ... break   ← useful for menus!"
                        ),
                        'voice': (
                            "A while loop keeps running as long as its condition is true. "
                            "Use while when you do not know in advance how many times to loop. "
                            "Always make sure the condition will eventually become false — "
                            "otherwise you get an infinite loop! "
                            "The pattern while True colon break is very useful for menus."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'while True + break Pattern',
                        'content': (
                            "The  while True: ... break  pattern keeps asking until\n"
                            "the user gives a valid answer. Watch it in action:"
                        ),
                        'voice': (
                            "The while True break pattern keeps asking until the user gives a valid answer. "
                            "Watch this example — it keeps prompting until a valid number is entered!"
                        ),
                        'code': (
                            '# Keep asking until user enters a number 1-10\n'
                            'while True:\n'
                            '    answer = input("Pick a number between 1 and 10: ")\n'
                            '    number = int(answer)\n'
                            '    if 1 <= number <= 10:\n'
                            '        print(f"Great choice! You picked {number}.")\n'
                            '        break  # valid input — exit the loop\n'
                            '    else:\n'
                            '        print("That is not between 1 and 10 — try again!")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Number Guessing Game (Pro Version)',
                        'content': (
                            "Build an improved guessing game using a while loop:\n\n"
                            "  • Computer picks a random number 1-100\n"
                            "  • Player keeps guessing until correct\n"
                            "  • Give 'too high' / 'too low' hints\n"
                            "  • Count the number of guesses\n"
                            "  • Rate the player at the end!"
                        ),
                        'voice': (
                            "Build a pro guessing game with a while loop. "
                            "The player guesses a number between 1 and 100, "
                            "gets hints, and the program counts how many guesses it took!"
                        ),
                        'starter_code': (
                            'import random\n'
                            '\n'
                            'secret = random.randint(1, 100)\n'
                            'guesses = 0\n'
                            '\n'
                            'print("🎲 Guess the number between 1 and 100!")\n'
                            '\n'
                            'while True:\n'
                            '    guess = int(input("Your guess: "))\n'
                            '    guesses += 1\n'
                            '    \n'
                            '    # YOUR CODE:\n'
                            '    # Check if guess is too low → print a hint\n'
                            '    # Check if guess is too high → print a hint\n'
                            '    # If correct → print guesses count and break\n'
                            '    pass  # remove this line when you start writing\n'
                        ),
                        'expected_output': None,
                        'hints': [
                            'guesses += 1 is a shortcut for guesses = guesses + 1',
                            'while True: loops forever until a break is hit',
                            'Inside the loop: if guess < secret → "Too low!", elif guess > secret → "Too high!", else → correct!',
                            'For the rating: if guesses <= 5: print("Amazing!") elif guesses <= 10: print("Good effort!") else: print("Keep practising!")',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'while Quiz',
                        'question': 'When should you use a while loop instead of a for loop?',
                        'voice': 'When should you use a while loop instead of a for loop?',
                        'options': [
                            'When you know exactly how many times to loop',
                            'When the number of iterations depends on a condition',
                            'while loops are always better than for loops',
                            'for loops cannot use break',
                        ],
                        'answer': 1,
                        'explanation': 'Use while when the number of iterations depends on a condition or user input. Use for when iterating over a known sequence.',
                        'explanation_voice': 'Correct! Use while when the number of loops depends on a condition. Great thinking!',
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULES 4-11: M4, M5, M6, M11 fully built; M7-M10 remain stubs
    # ================================================================

    # ================================================================
    # MODULE 4: Functions
    # ================================================================
    {
        'id': 't_m4',
        'title': 'Functions 🔧',
        'icon': '🔧',
        'description': 'Write reusable blocks of code with parameters and return values.',
        'badge': 'Function Builder',
        'badge_icon': '🔧',
        'color': '#E17055',
        'prerequisite_modules': ['t_m1', 't_m2', 't_m3'],
        'lessons': [
            # ---- Lesson 1: Defining Functions ----
            {
                'id': 't_m4_l1',
                'title': 'Defining Functions',
                'icon': '🔧',
                'xp': 125,
                'steps': [
                    {
                        'type': 'story',
                        'title': '🔧 Mission: Reusable Code',
                        'content': (
                            "Imagine you had to write the same 5 lines of code\n"
                            "every single time you wanted to greet someone.\n\n"
                            "That would be ridiculous! 😂\n\n"
                            "Functions let you write code ONCE and use it ANYWHERE.\n"
                            "They are one of the most important ideas in all of programming.\n\n"
                            "Master functions and you will level up massively as a developer! 🚀"
                        ),
                        'voice': (
                            "Imagine writing the same five lines of code every time you wanted to greet someone — "
                            "that would be crazy! Functions let you write code once and use it anywhere. "
                            "They are one of the most important ideas in all of programming. "
                            "Master functions and you will level up massively as a developer!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Defining and Calling Functions',
                        'content': (
                            "A function is a named, reusable block of code.\n\n"
                            "    def function_name(parameters):\n"
                            "        # code goes here (indented!)\n"
                            "        return result\n\n"
                            "Example:\n"
                            "    def greet(name):\n"
                            '        return f"Hello, {name}!"\n\n'
                            "    # Calling the function:\n"
                            '    message = greet("Toby")\n'
                            '    print(message)     # Hello, Toby!\n'
                            '    print(greet("world"))  # Hello, world!\n\n'
                            "Key terms:\n"
                            "  def  — keyword that starts a function definition\n"
                            "  name  — how you call it\n"
                            "  parameters — inputs the function receives\n"
                            "  return  — sends a result back to the caller"
                        ),
                        'voice': (
                            "A function is a named, reusable block of code. "
                            "You define it once with the def keyword, give it a name, "
                            "list any parameters in brackets, then write the code indented inside. "
                            "Use return to send a result back. "
                            "Call the function by writing its name with brackets."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Functions in Action',
                        'content': 'Watch how one function can be called many times:',
                        'voice': 'Watch how one function can be called many times with different inputs.',
                        'code': (
                            'def square(n):\n'
                            '    return n * n\n'
                            '\n'
                            'def cube(n):\n'
                            '    return n * n * n\n'
                            '\n'
                            'def is_even(n):\n'
                            '    return n % 2 == 0\n'
                            '\n'
                            'for i in range(1, 6):\n'
                            '    print(f"{i}: square={square(i)}, cube={cube(i)}, even={is_even(i)}")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Build a Temperature Converter',
                        'content': (
                            "Write TWO functions:\n\n"
                            "  1. celsius_to_fahrenheit(c)\n"
                            "     Formula: F = C × 9/5 + 32\n\n"
                            "  2. fahrenheit_to_celsius(f)\n"
                            "     Formula: C = (F − 32) × 5/9\n\n"
                            "Then print conversions for 0°C, 100°C, and 37°C (body temp)."
                        ),
                        'voice': (
                            "Write two functions to convert temperatures. "
                            "Celsius to Fahrenheit multiplies by nine fifths and adds 32. "
                            "Fahrenheit to Celsius subtracts 32 then multiplies by five ninths. "
                            "Then call both functions with a few temperatures."
                        ),
                        'starter_code': (
                            'def celsius_to_fahrenheit(c):\n'
                            '    # YOUR CODE: return the Fahrenheit value\n'
                            '    pass\n'
                            '\n'
                            'def fahrenheit_to_celsius(f):\n'
                            '    # YOUR CODE: return the Celsius value\n'
                            '    pass\n'
                            '\n'
                            '# Test your functions:\n'
                            'print(f"0°C = {celsius_to_fahrenheit(0)}°F")\n'
                            'print(f"100°C = {celsius_to_fahrenheit(100)}°F")\n'
                            'print(f"37°C = {celsius_to_fahrenheit(37)}°F")\n'
                            'print(f"98.6°F = {fahrenheit_to_celsius(98.6)}°C")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Replace "pass" with: return c * 9/5 + 32',
                            'For Fahrenheit to Celsius: return (f - 32) * 5/9',
                            'round(result, 1) rounds to 1 decimal place — optional but neat!',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Functions Quiz',
                        'question': 'What keyword is used to define a function in Python?',
                        'voice': 'Quiz! What keyword defines a function in Python?',
                        'options': ['func', 'define', 'def', 'function'],
                        'answer': 2,
                        'explanation': 'Python uses "def" to define a function — short for "define".',
                        'explanation_voice': 'Correct! Python uses def — short for define. Nice work!',
                    },
                ],
            },

            # ---- Lesson 2: Parameters and Return Values ----
            {
                'id': 't_m4_l2',
                'title': 'Parameters & Return Values',
                'icon': '↩️',
                'xp': 125,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Multiple Parameters & Default Values',
                        'content': (
                            "Functions can have multiple parameters:\n\n"
                            "    def add(a, b):\n"
                            "        return a + b\n\n"
                            "    print(add(3, 7))   # 10\n\n"
                            "Default parameter values — used when no argument is given:\n\n"
                            "    def greet(name, greeting='Hello'):\n"
                            '        return f"{greeting}, {name}!"\n\n'
                            '    print(greet("Toby"))           # Hello, Toby!\n'
                            '    print(greet("Toby", "Hey"))    # Hey, Toby!\n\n'
                            "A function CAN return multiple values:\n\n"
                            "    def min_max(numbers):\n"
                            "        return min(numbers), max(numbers)\n\n"
                            "    low, high = min_max([5, 2, 8, 1, 9])\n"
                            "    print(low, high)   # 1 9"
                        ),
                        'voice': (
                            "Functions can take multiple parameters separated by commas. "
                            "You can give parameters default values so they work even when not supplied. "
                            "A function can even return multiple values — Python packs them into a tuple "
                            "and you can unpack them with multiple variable names."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'A Real-World Example: Shopping Cart',
                        'content': 'Functions make complex programs much cleaner:',
                        'voice': 'Here is a shopping cart example using multiple functions.',
                        'code': (
                            'def calculate_total(price, quantity, discount=0):\n'
                            '    subtotal = price * quantity\n'
                            '    saving = subtotal * (discount / 100)\n'
                            '    return subtotal - saving\n'
                            '\n'
                            'def format_price(amount):\n'
                            '    return f"£{amount:.2f}"\n'
                            '\n'
                            '# Items in the cart\n'
                            'items = [\n'
                            '    ("Pizza", 8.99, 2, 0),\n'
                            '    ("Coke", 1.50, 4, 10),\n'
                            '    ("Chips", 2.00, 3, 0),\n'
                            ']\n'
                            '\n'
                            'total = 0\n'
                            'for name, price, qty, disc in items:\n'
                            '    cost = calculate_total(price, qty, disc)\n'
                            '    total += cost\n'
                            '    print(f"{name:10} x{qty}  {format_price(cost)}")\n'
                            '\n'
                            'print(f"\\nTOTAL: {format_price(total)}")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Password Strength Checker',
                        'content': (
                            "Write a function  check_password(password)  that:\n\n"
                            "  • Returns 'Weak'   — if less than 8 characters\n"
                            "  • Returns 'Medium' — if 8+ chars but no digits\n"
                            "  • Returns 'Strong' — if 8+ chars AND has a digit\n\n"
                            "Hint: Use  any(c.isdigit() for c in password)  to check for digits.\n"
                            "Then test it with a few different passwords!"
                        ),
                        'voice': (
                            "Write a password strength checker function. "
                            "Weak if under 8 characters. Medium if 8 or more but no digits. "
                            "Strong if 8 or more characters and contains at least one digit. "
                            "Use any with isdigit to check for numbers in the password."
                        ),
                        'starter_code': (
                            'def check_password(password):\n'
                            '    # Check length first\n'
                            '    if len(password) < 8:\n'
                            '        return "Weak"\n'
                            '    # YOUR CODE: check for digits\n'
                            '    # has_digit = any(c.isdigit() for c in password)\n'
                            '    # return "Strong" if has_digit else "Medium"\n'
                            '    pass\n'
                            '\n'
                            '# Test your function:\n'
                            'print(check_password("abc"))         # Weak\n'
                            'print(check_password("abcdefgh"))    # Medium\n'
                            'print(check_password("abc12345"))    # Strong'
                        ),
                        'expected_output': 'Weak\nMedium\nStrong',
                        'hints': [
                            'Uncomment the lines with has_digit and return',
                            'any(c.isdigit() for c in password) returns True if ANY character is a digit',
                            'Delete the "pass" line once you add your code',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Parameters Quiz',
                        'question': 'What is a "default parameter"?',
                        'voice': 'Quiz! What is a default parameter in a function?',
                        'options': [
                            'A parameter that is always required',
                            'A parameter with a preset value used when none is given',
                            'The first parameter of any function',
                            'A parameter that cannot be changed',
                        ],
                        'answer': 1,
                        'explanation': (
                            'A default parameter has a preset value. '
                            'If you call the function without that argument, the default is used.'
                        ),
                        'explanation_voice': (
                            'Correct! A default parameter has a preset value used when you do not supply one. '
                            'Great understanding!'
                        ),
                    },
                ],
            },

            # ---- Lesson 3: Functions Project ----
            {
                'id': 't_m4_l3',
                'title': 'Functions Project: Text RPG',
                'icon': '🎮',
                'xp': 150,
                'steps': [
                    {
                        'type': 'story',
                        'title': '🎮 Build a Text Adventure!',
                        'content': (
                            "Time to use your function skills to build something REAL!\n\n"
                            "You are going to create a mini text-based RPG game.\n\n"
                            "The player fights monsters using structured function code.\n"
                            "Functions are what make games manageable — every action\n"
                            "in a real game (attack, defend, heal) is a function.\n\n"
                            "Let's build it! ⚔️"
                        ),
                        'voice': (
                            "Time to use your function skills to build something real! "
                            "You are going to create a mini text-based RPG game. "
                            "Functions are what make games manageable — every action in a real game is a function. "
                            "Let's build it!"
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'The Building Blocks',
                        'content': 'Study these functions — they will form the basis of your game:',
                        'voice': 'Study these building blocks — they are the foundation of the RPG.',
                        'code': (
                            'import random\n'
                            '\n'
                            'def create_character(name, hp, attack):\n'
                            '    return {"name": name, "hp": hp, "attack": attack}\n'
                            '\n'
                            'def attack(attacker, defender):\n'
                            '    damage = random.randint(1, attacker["attack"])\n'
                            '    defender["hp"] -= damage\n'
                            '    return damage\n'
                            '\n'
                            'def is_alive(character):\n'
                            '    return character["hp"] > 0\n'
                            '\n'
                            'def show_status(char):\n'
                            '    print(f"{char[\'name\']:10} HP: {max(0, char[\'hp\'])}")\n'
                            '\n'
                            '# Create hero and monster\n'
                            'hero = create_character("Hero", 30, 8)\n'
                            'goblin = create_character("Goblin", 20, 5)\n'
                            '\n'
                            'print("=== BATTLE START ===")\n'
                            'round_num = 1\n'
                            'while is_alive(hero) and is_alive(goblin):\n'
                            '    dmg = attack(hero, goblin)\n'
                            '    print(f"Round {round_num}: Hero hits Goblin for {dmg} damage!")\n'
                            '    if is_alive(goblin):\n'
                            '        dmg2 = attack(goblin, hero)\n'
                            '        print(f"         Goblin hits Hero for {dmg2} damage!")\n'
                            '    show_status(hero)\n'
                            '    show_status(goblin)\n'
                            '    round_num += 1\n'
                            '\n'
                            'if is_alive(hero):\n'
                            '    print("\\n🏆 Hero wins!")\n'
                            'else:\n'
                            '    print("\\n💀 Game over!")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Upgrade the RPG!',
                        'content': (
                            "Extend the RPG by writing a  heal(character, amount)  function:\n\n"
                            "  • It should add 'amount' HP to the character\n"
                            "  • HP should NOT go above the character's starting max HP\n"
                            "  • Use it so the hero heals 5 HP every other round\n\n"
                            "BONUS: Add a second monster and make the hero fight them both!"
                        ),
                        'voice': (
                            "Extend the RPG by adding a heal function. "
                            "It should add hit points to a character but not above their maximum. "
                            "Then use it so the hero heals every other round. "
                            "Bonus: add a second monster!"
                        ),
                        'starter_code': (
                            'import random\n'
                            '\n'
                            'def create_character(name, hp, attack):\n'
                            '    return {"name": name, "hp": hp, "attack": attack, "max_hp": hp}\n'
                            '\n'
                            'def attack(attacker, defender):\n'
                            '    damage = random.randint(1, attacker["attack"])\n'
                            '    defender["hp"] -= damage\n'
                            '    return damage\n'
                            '\n'
                            'def is_alive(character):\n'
                            '    return character["hp"] > 0\n'
                            '\n'
                            'def heal(character, amount):\n'
                            '    # YOUR CODE: add amount to hp, but cap at max_hp\n'
                            '    pass\n'
                            '\n'
                            'hero = create_character("Hero", 30, 8)\n'
                            'goblin = create_character("Goblin", 20, 5)\n'
                            '\n'
                            'for round_num in range(1, 8):\n'
                            '    if not (is_alive(hero) and is_alive(goblin)):\n'
                            '        break\n'
                            '    attack(hero, goblin)\n'
                            '    attack(goblin, hero)\n'
                            '    if round_num % 2 == 0:\n'
                            '        heal(hero, 5)  # heal every other round\n'
                            '    print(f"Round {round_num}: Hero HP={hero[\'hp\']} Goblin HP={goblin[\'hp\']}")\n'
                            '\n'
                            'print("Hero wins!" if is_alive(hero) else "Game over!")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'In heal(): character["hp"] += amount',
                            'Cap at max: character["hp"] = min(character["hp"], character["max_hp"])',
                            'Delete the "pass" once you write your code',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Functions Final Quiz',
                        'question': 'What does the  return  statement do in a function?',
                        'voice': 'Final quiz! What does the return statement do in a function?',
                        'options': [
                            'Stops the program entirely',
                            'Sends a value back to whoever called the function',
                            'Prints a value to the screen',
                            'Goes back to the start of the function',
                        ],
                        'answer': 1,
                        'explanation': (
                            'return sends a value back to the code that called the function. '
                            'Without return, the function gives back None.'
                        ),
                        'explanation_voice': (
                            'Correct! Return sends a value back to the caller. '
                            'Without return, the function just gives back None. Excellent!'
                        ),
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 5: Data Structures
    # ================================================================
    {
        'id': 't_m5',
        'title': 'Data Structures 📚',
        'icon': '📚',
        'description': 'Store and organise data with lists, dicts, tuples and sets.',
        'badge': 'Data Architect',
        'badge_icon': '📚',
        'color': '#6C5CE7',
        'prerequisite_modules': ['t_m1', 't_m2', 't_m3', 't_m4'],
        'lessons': [
            # ---- Lesson 1: Lists ----
            {
                'id': 't_m5_l1',
                'title': 'Lists',
                'icon': '📋',
                'xp': 125,
                'steps': [
                    {
                        'type': 'story',
                        'title': '📚 Mission: Organise Your Data',
                        'content': (
                            "So far all your variables held ONE thing.\n\n"
                            "But what if you want to store a list of 10 scores?\n"
                            "Or the names of 100 players? Or a million quiz answers?\n\n"
                            "That is where DATA STRUCTURES come in.\n"
                            "They are the containers that hold collections of data.\n\n"
                            "First up: the humble but mighty LIST. 📋"
                        ),
                        'voice': (
                            "So far your variables held one thing at a time. "
                            "But what if you want to store ten scores, or a hundred names? "
                            "That is where data structures come in — containers for collections of data. "
                            "First up: the list!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Python Lists',
                        'content': (
                            "A list stores an ORDERED collection of items.\n\n"
                            "    scores = [95, 72, 88, 61, 100]\n"
                            "    names  = ['Alice', 'Bob', 'Charlie']\n"
                            "    mixed  = [1, 'hello', True, 3.14]\n\n"
                            "Accessing items (indexing starts at 0):\n"
                            "    scores[0]    → 95  (first item)\n"
                            "    scores[-1]   → 100 (last item)\n"
                            "    scores[1:3]  → [72, 88] (slice)\n\n"
                            "Useful list methods:\n"
                            "    scores.append(99)     # add to end\n"
                            "    scores.pop()          # remove last\n"
                            "    scores.sort()         # sort in place\n"
                            "    len(scores)           # number of items\n"
                            "    99 in scores          # check membership"
                        ),
                        'voice': (
                            "A list stores an ordered collection of items in square brackets. "
                            "Indexing starts at zero — the first item is index zero. "
                            "Negative indexes count from the end — minus one is the last item. "
                            "You can slice a list to get a portion. "
                            "Key methods: append adds to the end, pop removes the last, "
                            "sort sorts in place, and len gives the count."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Lists in Action',
                        'content': 'See how lists power real programs:',
                        'voice': 'Here is how lists power real programs.',
                        'code': (
                            'scores = [85, 92, 78, 95, 61, 88]\n'
                            '\n'
                            '# Statistics\n'
                            'print(f"Count:   {len(scores)}")\n'
                            'print(f"Total:   {sum(scores)}")\n'
                            'print(f"Average: {sum(scores)/len(scores):.1f}")\n'
                            'print(f"Highest: {max(scores)}")\n'
                            'print(f"Lowest:  {min(scores)}")\n'
                            '\n'
                            '# Filter: only scores above 80\n'
                            'good_scores = [s for s in scores if s > 80]\n'
                            'print(f"Above 80: {good_scores}")\n'
                            '\n'
                            '# Sort and rank\n'
                            'scores.sort(reverse=True)\n'
                            'print("Ranked:", scores)'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Class Gradebook',
                        'content': (
                            "Build a gradebook program:\n\n"
                            "  1. Start with the list of scores below\n"
                            "  2. Calculate and print the average\n"
                            "  3. Find and print the highest and lowest\n"
                            "  4. Print how many students scored above 70\n\n"
                            "Use the list methods and built-in functions from the lesson!"
                        ),
                        'voice': (
                            "Build a class gradebook! Calculate the average, "
                            "find the highest and lowest scores, "
                            "and count how many students passed with more than 70."
                        ),
                        'starter_code': (
                            'class_scores = [72, 88, 45, 91, 67, 83, 55, 79, 94, 61]\n'
                            '\n'
                            '# YOUR CODE:\n'
                            '# 1. Print the average (use sum() and len())\n'
                            '\n'
                            '# 2. Print the highest and lowest (use max() and min())\n'
                            '\n'
                            '# 3. Count scores above 70\n'
                            '#    Hint: above_70 = [s for s in class_scores if s > 70]\n'
                            '#    Then print len(above_70)\n'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Average = sum(class_scores) / len(class_scores)',
                            'Use max() and min() directly: max(class_scores)',
                            'Count with: len([s for s in class_scores if s > 70])',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Lists Quiz',
                        'question': 'What does  my_list[-1]  return?',
                        'voice': 'Quiz! What does my list minus one return?',
                        'options': [
                            'Raises an IndexError',
                            'The first item in the list',
                            'The last item in the list',
                            '-1',
                        ],
                        'answer': 2,
                        'explanation': (
                            'Negative indexes count from the end. '
                            'list[-1] is the last item, list[-2] is second-to-last, etc.'
                        ),
                        'explanation_voice': (
                            'Correct! Negative one gives the last item. '
                            'Negative indexes count backwards from the end. Nice!'
                        ),
                    },
                ],
            },

            # ---- Lesson 2: Dictionaries ----
            {
                'id': 't_m5_l2',
                'title': 'Dictionaries',
                'icon': '📖',
                'xp': 125,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Python Dictionaries',
                        'content': (
                            "A dictionary stores KEY-VALUE pairs — like a real dictionary\n"
                            "where each word (key) has a definition (value).\n\n"
                            '    player = {\n'
                            '        "name": "Toby",\n'
                            '        "score": 9500,\n'
                            '        "level": 7,\n'
                            '        "alive": True\n'
                            '    }\n\n'
                            "Accessing and modifying:\n"
                            '    player["score"]          # 9500\n'
                            '    player["score"] += 100   # add 100\n'
                            '    player["lives"] = 3      # add new key\n'
                            '    del player["alive"]      # remove key\n\n'
                            "Iteration:\n"
                            "    for key in player:\n"
                            "        print(key, ':', player[key])\n\n"
                            '    player.keys()    # all keys\n'
                            '    player.values()  # all values\n'
                            '    player.items()   # key-value pairs'
                        ),
                        'voice': (
                            "A dictionary stores key-value pairs. "
                            "Think of it like a real dictionary — the word is the key and the definition is the value. "
                            "Access values using square brackets with the key. "
                            "You can add new keys, update values, or delete keys. "
                            "Loop through all key-value pairs with items()."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Dictionaries in Action',
                        'content': 'A contacts list built with a dictionary:',
                        'voice': 'Here is a contacts list built with a dictionary.',
                        'code': (
                            'contacts = {\n'
                            '    "Mum":   "07700900123",\n'
                            '    "Dad":   "07700900456",\n'
                            '    "School":"01632960789",\n'
                            '}\n'
                            '\n'
                            '# Look up a contact\n'
                            'name = "Mum"\n'
                            'if name in contacts:\n'
                            '    print(f"{name}: {contacts[name]}")\n'
                            'else:\n'
                            '    print(f"{name} not found")\n'
                            '\n'
                            '# Add a new contact\n'
                            'contacts["Best Friend"] = "07700900999"\n'
                            '\n'
                            '# Print all contacts\n'
                            'print("--- All Contacts ---")\n'
                            'for name, number in contacts.items():\n'
                            '    print(f"  {name:15} {number}")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Word Frequency Counter',
                        'content': (
                            "Write a program that counts how many times\n"
                            "each word appears in a sentence.\n\n"
                            "Use a dictionary where:\n"
                            "  key = word\n"
                            "  value = how many times it appears\n\n"
                            "Then print the word that appears most often!"
                        ),
                        'voice': (
                            "Write a word frequency counter! "
                            "Count how many times each word appears in the sentence "
                            "using a dictionary, then find the most common word."
                        ),
                        'starter_code': (
                            'sentence = "the cat sat on the mat and the cat sat"\n'
                            'words = sentence.split()  # splits into a list of words\n'
                            '\n'
                            '# YOUR CODE: build a frequency dictionary\n'
                            'freq = {}\n'
                            'for word in words:\n'
                            '    # Hint: if word is in freq, add 1. If not, set to 1.\n'
                            '    pass  # replace with your code\n'
                            '\n'
                            'print("Word counts:", freq)\n'
                            '\n'
                            '# Find the most common word\n'
                            '# Hint: use max(freq, key=freq.get)\n'
                            'most_common = max(freq, key=freq.get)\n'
                            'print(f"Most common: {most_common} ({freq[most_common]} times)")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'If word already in freq: freq[word] += 1',
                            'If word NOT in freq: freq[word] = 1',
                            'Or use: freq[word] = freq.get(word, 0) + 1  (one line!)',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Dictionaries Quiz',
                        'question': 'How do you safely get a value from a dict that might not exist?',
                        'voice': 'How do you safely get a value from a dictionary that might not have the key?',
                        'options': [
                            'd[key]',
                            'd.get(key)',
                            'd.find(key)',
                            'd.fetch(key)',
                        ],
                        'answer': 1,
                        'explanation': (
                            'd.get(key) returns None if the key does not exist (no crash!). '
                            'd[key] raises a KeyError if the key is missing.'
                        ),
                        'explanation_voice': (
                            'Correct! .get() is the safe way — it returns None if the key is missing '
                            'instead of crashing with a KeyError. Great answer!'
                        ),
                    },
                ],
            },

            # ---- Lesson 3: Tuples & Sets ----
            {
                'id': 't_m5_l3',
                'title': 'Tuples & Sets',
                'icon': '🔒',
                'xp': 125,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Tuples — Immutable Sequences',
                        'content': (
                            "A tuple is like a list, but you CANNOT change it after creation.\n\n"
                            "    coordinates = (51.5, -0.1)   # London lat/long\n"
                            "    rgb_red     = (255, 0, 0)\n"
                            "    single      = (42,)          # note the trailing comma!\n\n"
                            "Accessing works just like lists:\n"
                            "    coordinates[0]   → 51.5\n"
                            "    coordinates[-1]  → -0.1\n\n"
                            "Unpacking — assign each element to a variable:\n"
                            "    lat, lon = coordinates\n"
                            "    r, g, b  = rgb_red\n\n"
                            "Why tuples?\n"
                            "  • Faster than lists\n"
                            "  • Safe — nobody can accidentally change them\n"
                            "  • Can be used as dictionary keys (lists cannot!)"
                        ),
                        'voice': (
                            "A tuple is like a list you cannot change. "
                            "Create them with round brackets. "
                            "You can unpack tuples into variables. "
                            "Tuples are faster, safer, and can be used as dictionary keys."
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Sets — Unique Elements',
                        'content': (
                            "A set stores UNIQUE items only — no duplicates!\n\n"
                            "    colours = {'red', 'blue', 'green', 'red'}\n"
                            "    print(colours)   → {'red', 'blue', 'green'}\n\n"
                            "Set operations — like a Venn diagram:\n"
                            "    a = {1, 2, 3, 4}\n"
                            "    b = {3, 4, 5, 6}\n\n"
                            "    a | b   → {1,2,3,4,5,6}  (union — everything)\n"
                            "    a & b   → {3, 4}          (intersection — in both)\n"
                            "    a - b   → {1, 2}          (difference — in a not b)\n\n"
                            "Useful methods:\n"
                            "    colours.add('purple')     # add one item\n"
                            "    colours.discard('red')    # remove (no error if missing)\n"
                            "    'blue' in colours         # membership check (very fast!)"
                        ),
                        'voice': (
                            "A set stores unique items only — no duplicates allowed. "
                            "Sets support powerful operations like union, intersection, and difference. "
                            "Think of them like Venn diagrams. "
                            "Membership checks with in are super fast on sets."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Set Operations in Action',
                        'content': 'Finding common and unique elements between two groups:',
                        'voice': 'Here is how set operations find common and unique elements.',
                        'code': (
                            'football = {"Alice", "Bob", "Charlie", "Diana", "Eve"}\n'
                            'chess    = {"Bob", "Diana", "Frank", "Grace"}\n'
                            '\n'
                            '# Who plays BOTH sports?\n'
                            'both = football & chess\n'
                            'print(f"Both clubs: {both}")\n'
                            '\n'
                            '# Who plays ANY sport?\n'
                            'any_sport = football | chess\n'
                            'print(f"All members: {any_sport}")\n'
                            '\n'
                            '# Football ONLY (not in chess)\n'
                            'football_only = football - chess\n'
                            'print(f"Football only: {football_only}")\n'
                            '\n'
                            '# Chess ONLY (not in football)\n'
                            'chess_only = chess - football\n'
                            'print(f"Chess only: {chess_only}")\n'
                            '\n'
                            'print(f"Total unique members: {len(any_sport)}")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Student Clubs Analyser 🏫',
                        'content': (
                            "The school has three clubs. Use sets to answer questions:\n\n"
                            "  1. Who is in ALL three clubs?\n"
                            "  2. Who is in coding but NOT art?\n"
                            "  3. How many UNIQUE students are there in total?\n"
                            "  4. Who is in exactly one club? (tricky!)"
                        ),
                        'voice': (
                            "Analyse three school clubs using set operations! "
                            "Find who is in all three, who is only in one, "
                            "and how many unique students there are in total."
                        ),
                        'starter_code': (
                            'coding_club = {"Alice", "Bob", "Charlie", "Diana", "Eve"}\n'
                            'art_club    = {"Bob", "Diana", "Frank", "Grace", "Eve"}\n'
                            'sport_club  = {"Charlie", "Diana", "Eve", "Henry", "Grace"}\n'
                            '\n'
                            '# TODO 1: Find students in ALL three clubs\n'
                            '# Hint: use & to intersect all three sets\n'
                            'all_three = coding_club  # fix this!\n'
                            'print(f"In all three clubs: {all_three}")\n'
                            '\n'
                            '# TODO 2: Find students in coding but NOT art\n'
                            'coding_not_art = coding_club  # fix this!\n'
                            'print(f"Coding but not art: {coding_not_art}")\n'
                            '\n'
                            '# TODO 3: Find total unique students across all clubs\n'
                            'all_students = coding_club  # fix this!\n'
                            'print(f"Total unique students: {len(all_students)}")\n'
                            '\n'
                            '# TODO 4 (CHALLENGE): Find students in exactly one club\n'
                            '# Hint: a student is in exactly one club if they are in\n'
                            '# the total set but NOT in any pair\'s intersection\n'
                            'in_multiple = (coding_club & art_club) | (coding_club & sport_club) | (art_club & sport_club)\n'
                            'exactly_one = all_students - in_multiple  # uses your answer from TODO 3\n'
                            'print(f"In exactly one club: {exactly_one}")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'All three: coding_club & art_club & sport_club',
                            'Coding not art: coding_club - art_club',
                            'All students: coding_club | art_club | sport_club',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Tuples Quiz',
                        'question': 'Can you change a value in a tuple after creating it?',
                        'voice': 'Quiz! Can you change a value in a tuple after creating it?',
                        'options': [
                            'Yes, with indexing like a list',
                            'No — tuples are immutable',
                            'Only if the tuple has one element',
                            'Yes, but only with .update()',
                        ],
                        'answer': 1,
                        'explanation': (
                            'Tuples are immutable — once created, their values cannot be changed. '
                            'This is what makes them safe and usable as dictionary keys.'
                        ),
                        'explanation_voice': (
                            'Correct! Tuples are immutable — you cannot change them after creation. '
                            'That is what makes them safe and perfect for dictionary keys!'
                        ),
                    },
                ],
            },
        ],
    },

    # ================================================================
    # MODULE 6: Object-Oriented Python
    # ================================================================
    {
        'id': 't_m6',
        'title': 'Object-Oriented Python 🏗️',
        'icon': '🏗️',
        'description': 'Model real-world things with classes, objects and inheritance.',
        'badge': 'OOP Master',
        'badge_icon': '🏗️',
        'color': '#00CEC9',
        'prerequisite_modules': ['t_m1', 't_m2', 't_m3', 't_m4', 't_m5'],
        'lessons': [
            # ---- Lesson 1: Classes & Objects ----
            {
                'id': 't_m6_l1',
                'title': 'Classes & Objects',
                'icon': '🏗️',
                'xp': 150,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Mission: Object Architect 🏗️',
                        'content': (
                            "Agent Toby — welcome to a MASSIVE level up.\n\n"
                            "Everything in the real world is an OBJECT:\n"
                            "  A car has properties (colour, speed) and actions (drive, brake).\n"
                            "  A player has stats (health, score) and abilities (attack, heal).\n\n"
                            "A CLASS is the blueprint. An OBJECT is the thing you build from it.\n"
                            "One blueprint → unlimited objects.\n\n"
                            "This is how professional developers build BIG software. 🚀"
                        ),
                        'voice': (
                            "Agent Toby — everything in the real world is an object. "
                            "A class is the blueprint, an object is what you build from it. "
                            "This is how professional developers build big software!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Class Syntax: __init__, self, Methods',
                        'content': (
                            "Define a class with the class keyword:\n\n"
                            "    class Player:\n"
                            "        def __init__(self, name, health):\n"
                            "            self.name = name\n"
                            "            self.health = health\n\n"
                            "        def take_damage(self, amount):\n"
                            "            self.health -= amount\n\n"
                            "        def is_alive(self):\n"
                            "            return self.health > 0\n\n"
                            "Key concepts:\n"
                            "  class     — defines the blueprint\n"
                            "  __init__  — runs when you create an object (constructor)\n"
                            "  self      — refers to THIS specific object\n"
                            "  attributes — variables on self (self.name, self.health)\n"
                            "  methods   — functions inside the class\n\n"
                            "Creating objects:\n"
                            "    p1 = Player('Toby', 100)\n"
                            "    p2 = Player('Bot', 80)\n"
                            "    p1.take_damage(25)\n"
                            "    print(p1.health)   # 75"
                        ),
                        'voice': (
                            "Define a class with the class keyword. "
                            "The init method runs when you create an object — it sets up the attributes. "
                            "Self refers to this specific object. "
                            "Methods are functions inside the class. "
                            "Create objects by calling the class like a function."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Player Class',
                        'content': 'A Player class with name, health and attack power:',
                        'voice': 'Here is a Player class with health and attack methods.',
                        'code': (
                            'class Player:\n'
                            '    def __init__(self, name, health, attack_power):\n'
                            '        self.name = name\n'
                            '        self.health = health\n'
                            '        self.attack_power = attack_power\n'
                            '        self.score = 0\n'
                            '\n'
                            '    def attack(self, target):\n'
                            '        target.health -= self.attack_power\n'
                            '        print(f"{self.name} hits {target.name} for {self.attack_power} damage!")\n'
                            '\n'
                            '    def is_alive(self):\n'
                            '        return self.health > 0\n'
                            '\n'
                            '    def status(self):\n'
                            '        state = "ALIVE" if self.is_alive() else "DEFEATED"\n'
                            '        print(f"{self.name}: {self.health} HP [{state}]")\n'
                            '\n'
                            '# Create two players\n'
                            'hero = Player("Toby", 100, 25)\n'
                            'enemy = Player("Goblin", 60, 15)\n'
                            '\n'
                            '# Battle!\n'
                            'hero.attack(enemy)\n'
                            'enemy.attack(hero)\n'
                            'hero.attack(enemy)\n'
                            'hero.attack(enemy)\n'
                            '\n'
                            'hero.status()\n'
                            'enemy.status()'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Build a BankAccount Class 🏦',
                        'content': (
                            "Create a BankAccount class with:\n\n"
                            "  • __init__: owner name and starting balance\n"
                            "  • deposit(amount): add money, print new balance\n"
                            "  • withdraw(amount): remove money (if enough!)\n"
                            "  • summary(): print owner and balance\n\n"
                            "Complete the methods marked with TODO."
                        ),
                        'voice': (
                            "Build a BankAccount class with deposit and withdraw methods! "
                            "Make sure you cannot withdraw more than the balance."
                        ),
                        'starter_code': (
                            'class BankAccount:\n'
                            '    def __init__(self, owner, balance=0):\n'
                            '        self.owner = owner\n'
                            '        self.balance = balance\n'
                            '\n'
                            '    def deposit(self, amount):\n'
                            '        # TODO: Add amount to self.balance\n'
                            '        # Print f"{owner} deposited £{amount}. Balance: £{balance}"\n'
                            '        pass\n'
                            '\n'
                            '    def withdraw(self, amount):\n'
                            '        # TODO: If amount > balance, print "Insufficient funds!"\n'
                            '        # Otherwise subtract amount and print the new balance\n'
                            '        pass\n'
                            '\n'
                            '    def summary(self):\n'
                            '        # TODO: Print f"Account: {owner} | Balance: £{balance}"\n'
                            '        pass\n'
                            '\n'
                            '# Test your class:\n'
                            'acc = BankAccount("Toby", 100)\n'
                            'acc.summary()\n'
                            'acc.deposit(50)\n'
                            'acc.withdraw(30)\n'
                            'acc.withdraw(200)\n'
                            'acc.summary()'
                        ),
                        'expected_output': None,
                        'hints': [
                            'self.balance += amount for deposit',
                            'Check if amount > self.balance before withdrawing',
                            'Use f-strings with self.owner and self.balance',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'OOP Quiz',
                        'question': 'What is "self" in a Python class?',
                        'voice': 'Quiz! What is self in a Python class?',
                        'options': [
                            'A built-in function',
                            'A reference to the current object instance',
                            'The name of the class',
                            'A keyword that creates a new object',
                        ],
                        'answer': 1,
                        'explanation': (
                            'self refers to the specific object that called the method. '
                            'It lets each object access its own attributes and methods.'
                        ),
                        'explanation_voice': (
                            'Correct! Self refers to the specific object that called the method. '
                            'That is how each object keeps track of its own data!'
                        ),
                    },
                ],
            },

            # ---- Lesson 2: Inheritance & Polymorphism ----
            {
                'id': 't_m6_l2',
                'title': 'Inheritance & Polymorphism',
                'icon': '🧬',
                'xp': 150,
                'steps': [
                    {
                        'type': 'teach',
                        'title': 'Inheritance: Parent & Child Classes',
                        'content': (
                            "Inheritance lets a class REUSE code from another class.\n\n"
                            "    class Animal:              # parent class\n"
                            "        def __init__(self, name):\n"
                            "            self.name = name\n"
                            "        def speak(self):\n"
                            "            return '...'\n\n"
                            "    class Dog(Animal):         # child — inherits from Animal\n"
                            "        def speak(self):       # override the parent method\n"
                            '            return f"{self.name} says: Woof!"\n\n'
                            "Key ideas:\n"
                            "  • Child class inherits ALL attributes and methods from parent\n"
                            "  • Child can OVERRIDE methods to change behaviour\n"
                            "  • super() calls the parent's version of a method\n"
                            "  • Polymorphism = different classes, same method name,\n"
                            "    different behaviour"
                        ),
                        'voice': (
                            "Inheritance lets a child class reuse code from a parent class. "
                            "The child inherits all attributes and methods, "
                            "and can override them to change behaviour. "
                            "Super calls the parent version. "
                            "Polymorphism means same method name, different behaviour."
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Animal Hierarchy',
                        'content': 'An Animal parent class with Dog and Cat subclasses:',
                        'voice': 'Here is an Animal class with Dog and Cat subclasses that override speak.',
                        'code': (
                            'class Animal:\n'
                            '    def __init__(self, name, species):\n'
                            '        self.name = name\n'
                            '        self.species = species\n'
                            '\n'
                            '    def speak(self):\n'
                            '        return f"{self.name} says: ..."\n'
                            '\n'
                            '    def info(self):\n'
                            '        return f"{self.name} is a {self.species}"\n'
                            '\n'
                            'class Dog(Animal):\n'
                            '    def __init__(self, name, breed):\n'
                            '        super().__init__(name, "Dog")\n'
                            '        self.breed = breed\n'
                            '\n'
                            '    def speak(self):\n'
                            '        return f"{self.name} says: Woof! 🐕"\n'
                            '\n'
                            'class Cat(Animal):\n'
                            '    def __init__(self, name, indoor=True):\n'
                            '        super().__init__(name, "Cat")\n'
                            '        self.indoor = indoor\n'
                            '\n'
                            '    def speak(self):\n'
                            '        return f"{self.name} says: Meow! 🐱"\n'
                            '\n'
                            '# Polymorphism in action\n'
                            'pets = [Dog("Rex", "Labrador"), Cat("Whiskers"), Dog("Max", "Poodle")]\n'
                            'for pet in pets:\n'
                            '    print(pet.info())\n'
                            '    print(pet.speak())\n'
                            '    print()'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'Shape Hierarchy 📐',
                        'content': (
                            "Build a shape class hierarchy:\n\n"
                            "  Shape (parent) — has a name, an area() method returning 0\n"
                            "  Circle(Shape)  — radius, area = π × r²\n"
                            "  Rectangle(Shape) — width & height, area = w × h\n\n"
                            "Complete the child classes and test them!"
                        ),
                        'voice': (
                            "Build a Shape hierarchy! Create Circle and Rectangle "
                            "subclasses that override the area method."
                        ),
                        'starter_code': (
                            'import math\n'
                            '\n'
                            'class Shape:\n'
                            '    def __init__(self, name):\n'
                            '        self.name = name\n'
                            '\n'
                            '    def area(self):\n'
                            '        return 0\n'
                            '\n'
                            '    def describe(self):\n'
                            '        print(f"{self.name}: area = {self.area():.2f}")\n'
                            '\n'
                            'class Circle(Shape):\n'
                            '    def __init__(self, radius):\n'
                            '        super().__init__("Circle")\n'
                            '        # TODO: store the radius\n'
                            '\n'
                            '    def area(self):\n'
                            '        # TODO: return math.pi * self.radius ** 2\n'
                            '        return 0\n'
                            '\n'
                            'class Rectangle(Shape):\n'
                            '    def __init__(self, width, height):\n'
                            '        super().__init__("Rectangle")\n'
                            '        # TODO: store width and height\n'
                            '\n'
                            '    def area(self):\n'
                            '        # TODO: return self.width * self.height\n'
                            '        return 0\n'
                            '\n'
                            '# Test your shapes\n'
                            'shapes = [Circle(5), Rectangle(4, 7), Circle(10)]\n'
                            'for shape in shapes:\n'
                            '    shape.describe()'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Store radius: self.radius = radius',
                            'Circle area: math.pi * self.radius ** 2',
                            'Rectangle area: self.width * self.height',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Inheritance Quiz',
                        'question': 'What keyword in the class definition makes one class inherit from another?',
                        'voice': 'Quiz! What keyword makes a class inherit from another?',
                        'options': [
                            'extends',
                            'inherits',
                            'Parentheses after the class name — e.g. class Dog(Animal)',
                            'the super keyword',
                        ],
                        'answer': 2,
                        'explanation': (
                            'In Python, you put the parent class in parentheses: class Dog(Animal). '
                            'There is no extends or inherits keyword. '
                            'super() is used inside methods to call the parent version.'
                        ),
                        'explanation_voice': (
                            'Correct! In Python, you put the parent class in brackets — '
                            'class Dog bracket Animal. Super is used inside methods to call the parent version.'
                        ),
                    },
                ],
            },

            # ---- Lesson 3: OOP Project — Text RPG ----
            {
                'id': 't_m6_l3',
                'title': 'OOP Project: Text RPG',
                'icon': '⚔️',
                'xp': 200,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Final Mission: Build an RPG ⚔️',
                        'content': (
                            "Agent Toby — this is the BIG one.\n\n"
                            "You are going to build a TEXT-BASED RPG using everything\n"
                            "you have learned about classes, inheritance, and methods.\n\n"
                            "Your game will have:\n"
                            "  ⚔️  Characters with health and attack\n"
                            "  👹  Monsters to fight\n"
                            "  🎒  Items to collect and use\n\n"
                            "This is how real game developers work —\n"
                            "every object in a game is a class! 🎮"
                        ),
                        'voice': (
                            "Agent Toby, this is the big one! "
                            "Build a text RPG with characters, monsters, and items. "
                            "Every object in a game is a class — this is how real developers work!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Composing Objects & Game Loops',
                        'content': (
                            "In a real game, objects CONTAIN other objects:\n\n"
                            "    class Character:\n"
                            "        def __init__(self, name):\n"
                            "            self.inventory = []    # list of Item objects!\n\n"
                            "    class Item:\n"
                            "        def __init__(self, name, power):\n"
                            "            self.name = name\n"
                            "            self.power = power\n\n"
                            "The game loop pattern:\n"
                            "    1. Show the current state (player HP, location)\n"
                            "    2. Get player input (what do they want to do?)\n"
                            "    3. Update the game state (fight, move, use item)\n"
                            "    4. Check for win/lose conditions\n"
                            "    5. Repeat!\n\n"
                            "This loop runs until the game ends."
                        ),
                        'voice': (
                            "In a real game, objects contain other objects — a character has an inventory of items. "
                            "The game loop shows state, gets input, updates the game, and checks for win or lose. "
                            "This loop repeats until the game ends."
                        ),
                    },
                    {
                        'type': 'exercise',
                        'title': 'Build Your Text RPG ⚔️',
                        'content': (
                            "Complete this text RPG! The starter code gives you:\n"
                            "  • An Item class\n"
                            "  • A Character class with inventory\n"
                            "  • A Monster class\n\n"
                            "Your job:\n"
                            "  1. Add the attack() method to Character\n"
                            "  2. Add the use_item() method to Character\n"
                            "  3. Complete the battle sequence\n\n"
                            "Make it epic! 🏆"
                        ),
                        'voice': (
                            "Complete this text RPG! Add the attack and use item methods, "
                            "then finish the battle sequence. Make it epic!"
                        ),
                        'starter_code': (
                            'import random\n'
                            '\n'
                            'class Item:\n'
                            '    def __init__(self, name, item_type, power):\n'
                            '        self.name = name\n'
                            '        self.item_type = item_type  # "weapon" or "heal"\n'
                            '        self.power = power\n'
                            '\n'
                            '    def __repr__(self):\n'
                            '        return f"{self.name} ({self.item_type}: +{self.power})"\n'
                            '\n'
                            'class Character:\n'
                            '    def __init__(self, name, health, base_attack):\n'
                            '        self.name = name\n'
                            '        self.health = health\n'
                            '        self.max_health = health\n'
                            '        self.base_attack = base_attack\n'
                            '        self.inventory = []\n'
                            '\n'
                            '    def is_alive(self):\n'
                            '        return self.health > 0\n'
                            '\n'
                            '    def pick_up(self, item):\n'
                            '        self.inventory.append(item)\n'
                            '        print(f"{self.name} picked up {item.name}!")\n'
                            '\n'
                            '    def attack(self, target):\n'
                            '        # TODO: Calculate damage = base_attack + random.randint(0, 10)\n'
                            '        # Subtract damage from target.health\n'
                            '        # Print who attacked whom and for how much damage\n'
                            '        pass\n'
                            '\n'
                            '    def use_item(self, item_name):\n'
                            '        # TODO: Find the item in self.inventory by name\n'
                            '        # If item_type is "heal": add power to health (max = max_health)\n'
                            '        # If item_type is "weapon": add power to base_attack\n'
                            '        # Remove the item from inventory after use\n'
                            '        # Print what happened\n'
                            '        pass\n'
                            '\n'
                            '    def status(self):\n'
                            '        print(f"  {self.name}: {self.health}/{self.max_health} HP | ATK: {self.base_attack}")\n'
                            '\n'
                            'class Monster(Character):\n'
                            '    def __init__(self, name, health, base_attack, xp_reward):\n'
                            '        super().__init__(name, health, base_attack)\n'
                            '        self.xp_reward = xp_reward\n'
                            '\n'
                            '# === SET UP THE GAME ===\n'
                            'hero = Character("Toby", 100, 15)\n'
                            'hero.pick_up(Item("Health Potion", "heal", 30))\n'
                            'hero.pick_up(Item("Magic Sword", "weapon", 10))\n'
                            '\n'
                            'monsters = [\n'
                            '    Monster("Goblin", 40, 8, 20),\n'
                            '    Monster("Skeleton", 60, 12, 35),\n'
                            '    Monster("Dragon", 100, 20, 100),\n'
                            ']\n'
                            '\n'
                            'print("=== TOBY\'S TEXT RPG ===")\n'
                            'print(f"Inventory: {hero.inventory}")\n'
                            'hero.use_item("Magic Sword")\n'
                            '\n'
                            'total_xp = 0\n'
                            'for monster in monsters:\n'
                            '    print(f"\\n--- A wild {monster.name} appears! ---")\n'
                            '    while hero.is_alive() and monster.is_alive():\n'
                            '        hero.attack(monster)\n'
                            '        if monster.is_alive():\n'
                            '            monster.attack(hero)\n'
                            '    if hero.is_alive():\n'
                            '        total_xp += monster.xp_reward\n'
                            '        print(f"Victory! +{monster.xp_reward} XP")\n'
                            '        if hero.health < 50 and hero.inventory:\n'
                            '            hero.use_item("Health Potion")\n'
                            '    else:\n'
                            '        print("Game Over! 💀")\n'
                            '        break\n'
                            '\n'
                            'print(f"\\n=== FINAL STATUS ===")\n'
                            'hero.status()\n'
                            'print(f"Total XP earned: {total_xp}")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'attack: damage = self.base_attack + random.randint(0, 10)',
                            'use_item: loop through self.inventory to find the item by name',
                            'Heal: self.health = min(self.health + item.power, self.max_health)',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'OOP in Games Quiz',
                        'question': 'Why is OOP useful for game development?',
                        'voice': 'Quiz! Why is OOP useful for game development?',
                        'options': [
                            'It makes games run faster',
                            'It organises code into reusable objects that model game entities',
                            'It is required by all game engines',
                            'It automatically creates graphics',
                        ],
                        'answer': 1,
                        'explanation': (
                            'OOP organises code into classes that model game entities — '
                            'players, enemies, items, weapons. '
                            'Each object manages its own state and behaviour, '
                            'making complex games much easier to build and maintain.'
                        ),
                        'explanation_voice': (
                            'Correct! OOP organises code into reusable objects that model game things — '
                            'players, enemies, items. It makes complex games much easier to build!'
                        ),
                    },
                ],
            },
        ],
    },

    _stub_module(
        't_m7', 'Files & Exceptions 📁', '📁',
        'Read and write files, handle errors gracefully.',
        'File Handler', '📁', '#FDCB6E',
        ['t_m1', 't_m2', 't_m3', 't_m4', 't_m5'],
        (
            "Reading and writing files lets your programs REMEMBER things!\n\n"
            "    with open('scores.txt', 'w') as f:\n"
            '        f.write("Toby: 100\\n")\n\n'
            "    with open('scores.txt', 'r') as f:\n"
            "        data = f.read()\n\n"
            "Exception handling catches errors gracefully:\n\n"
            "    try:\n"
            "        result = 10 / 0\n"
            "    except ZeroDivisionError:\n"
            '        print("Cannot divide by zero!")'
        ),
        (
            "Reading and writing files lets your programs save and load data. "
            "Exception handling catches errors gracefully so programs do not crash. "
            "This module is coming soon!"
        ),
        ['Reading text files', 'Writing and appending', 'Working with CSV',
         'JSON data', 'try/except/finally', 'Custom exceptions']
    ),

    _stub_module(
        't_m8', 'Networking Basics 🌐', '🌐',
        'Understand how the internet works and make Python talk to web services.',
        'Network Explorer', '🌐', '#74B9FF',
        ['t_m1', 't_m2', 't_m3', 't_m4', 't_m5', 't_m6', 't_m7'],
        (
            "The internet connects millions of computers together!\n\n"
            "Key concepts:\n"
            "  🌍  IP addresses — unique addresses for each device\n"
            "  🚪  Ports — specific 'doors' for different services\n"
            "  📨  HTTP/HTTPS — the language of the web\n"
            "  🔗  APIs — ways programs talk to each other\n\n"
            "In Python, the requests library makes HTTP calls easy.\n"
            "For example, to get data from a weather API:\n\n"
            "    response = requests.get(url)\n"
            "    data = response.json()    # returns a dict!\n\n"
            "⚠️  This module requires internet access for some exercises."
        ),
        (
            "The internet connects millions of computers together! "
            "You will learn about IP addresses, ports, HTTP, and APIs. "
            "Python's requests library makes it easy to talk to web services. "
            "This module is coming soon!"
        ),
        ['How the internet works (conceptual)',
         'IP addresses, DNS, and ports',
         'HTTP/HTTPS — GET, POST, status codes',
         'Working with JSON APIs',
         'Building a weather checker with a free API',
         'Introduction to web scraping (ethical)']
    ),

    _stub_module(
        't_m9', 'Azure & The Cloud ☁️', '☁️',
        'Discover cloud computing and how Azure powers the modern internet.',
        'Cloud Pioneer', '☁️', '#A29BFE',
        ['t_m1', 't_m2', 't_m3', 't_m4', 't_m5', 't_m6', 't_m7', 't_m8'],
        (
            "The Cloud means using computers over the internet instead of your own!\n\n"
            "Microsoft Azure is one of the world's largest clouds:\n"
            "  ☁️   Azure Virtual Machines — rent a computer in a data centre\n"
            "  💾  Azure Storage — store files, blobs, and databases\n"
            "  ⚡  Azure Functions — run code without managing servers\n"
            "  🤖  Azure AI Services — ready-made AI for your apps\n"
            "  🐳  Azure Container Apps — run Docker containers\n\n"
            "Millions of companies use Azure — including the ones that built\n"
            "Xbox, LinkedIn, and GitHub!"
        ),
        (
            "The cloud means using computers over the internet. "
            "Microsoft Azure is one of the world's largest cloud platforms. "
            "You will learn about virtual machines, storage, serverless functions, "
            "containers, and Azure AI services. This module is coming soon!"
        ),
        ['What is cloud computing?',
         'Azure services overview (VMs, Storage, Functions, AI)',
         'Azure Storage — blobs and queues',
         'Azure Functions — serverless Python',
         'Deploying a Python web app to Azure',
         'Azure AI — vision, speech, language APIs']
    ),

    _stub_module(
        't_m10', 'Introduction to AI & ML 🤖', '🤖',
        'Discover artificial intelligence and build your first machine learning model.',
        'AI Explorer', '🤖', '#FF7675',
        ['t_m1', 't_m2', 't_m3', 't_m4', 't_m5', 't_m6', 't_m7'],
        (
            "Artificial Intelligence is all around us!\n\n"
            "  🎵  Spotify recommending songs\n"
            "  🎬  Netflix suggesting films\n"
            "  📸  Your phone recognising faces\n"
            "  🗣️  Siri and Alexa understanding speech\n\n"
            "Machine Learning is how computers LEARN from data:\n"
            "  1. Collect data (examples)\n"
            "  2. Train a model (find patterns)\n"
            "  3. Use the model (make predictions)\n\n"
            "You will build real ML models with scikit-learn!\n\n"
            "⚠️  AI Ethics: with great power comes great responsibility.\n"
            "    We will always use AI responsibly and fairly."
        ),
        (
            "Artificial intelligence is all around us — in music apps, streaming services, "
            "and voice assistants. Machine learning is how computers learn from data. "
            "You will build real models with scikit-learn. "
            "We will also cover AI ethics — using AI responsibly. "
            "This module is coming soon!"
        ),
        ['What is AI? History and concepts',
         'Machine learning vs traditional programming',
         'Types of ML: supervised, unsupervised, reinforcement',
         'Your first classifier with scikit-learn',
         'Neural networks — how they work',
         'Using Azure AI APIs (vision, language)',
         'AI ethics and responsible use']
    ),

    # ================================================================
    # MODULE 11: Game Development (text-based)
    # ================================================================
    {
        'id': 't_m11',
        'title': 'Game Development 🎮',
        'icon': '🎮',
        'description': 'Build text-based games — dice duels, slot machines, and a dungeon crawler!',
        'badge': 'Game Developer',
        'badge_icon': '🎮',
        'color': '#55EFC4',
        'prerequisite_modules': ['t_m1', 't_m2', 't_m3', 't_m4', 't_m5', 't_m6'],
        'lessons': [
            # ---- Lesson 1: Game Design & ASCII Art ----
            {
                'id': 't_m11_l1',
                'title': 'Game Design & ASCII Art',
                'icon': '🎲',
                'xp': 150,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Mission: Game Developer 🎮',
                        'content': (
                            "Agent Toby — you are about to become a GAME DEVELOPER.\n\n"
                            "Every game ever made — from Minecraft to FIFA — runs on\n"
                            "the same three ideas:\n\n"
                            "  1. GAME LOOP  — update, check, repeat\n"
                            "  2. GAME STATE — variables tracking everything\n"
                            "  3. INPUT/OUTPUT — player actions and display\n\n"
                            "We will build text-based games using Python and random.\n"
                            "No graphics libraries needed — just pure code! 💻"
                        ),
                        'voice': (
                            "Agent Toby, you are about to become a game developer! "
                            "Every game runs on three ideas: the game loop, game state, and input output. "
                            "We will build text-based games using pure Python!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': 'Game Loop, State & ASCII Art',
                        'content': (
                            "The GAME LOOP — the heartbeat of every game:\n"
                            "    while game_running:\n"
                            "        show_state()    # display the game\n"
                            "        get_input()     # what does the player do?\n"
                            "        update_state()  # process the action\n"
                            "        check_win()     # has anyone won?\n\n"
                            "GAME STATE — track everything with variables/dicts:\n"
                            "    game = {\n"
                            '        "coins": 100,\n'
                            '        "round": 1,\n'
                            '        "playing": True\n'
                            "    }\n\n"
                            "ASCII ART — draw with text characters:\n"
                            '    print("╔══════════╗")\n'
                            '    print("║  🎰 SLOT ║")\n'
                            '    print("╚══════════╝")\n\n'
                            "Use random for dice, cards, enemy behaviour, and loot!"
                        ),
                        'voice': (
                            "The game loop has four steps: show state, get input, update state, check win. "
                            "Track everything with dictionaries and variables. "
                            "Use ASCII art to draw displays. "
                            "Use random for dice rolls, enemy behaviour, and loot!"
                        ),
                    },
                    {
                        'type': 'example',
                        'title': 'Dice Duel Game',
                        'content': 'A simple dice duel — player vs computer:',
                        'voice': 'Here is a dice duel game — player versus computer.',
                        'code': (
                            'import random\n'
                            '\n'
                            'print("=== ⚔️ DICE DUEL ⚔️ ===")\n'
                            'print("Best of 5 rounds!\\n")\n'
                            '\n'
                            'player_wins = 0\n'
                            'computer_wins = 0\n'
                            '\n'
                            'for round_num in range(1, 6):\n'
                            '    player_roll = random.randint(1, 6)\n'
                            '    computer_roll = random.randint(1, 6)\n'
                            '\n'
                            '    print(f"Round {round_num}: You rolled {player_roll} 🎲 | Computer rolled {computer_roll} 🎲")\n'
                            '\n'
                            '    if player_roll > computer_roll:\n'
                            '        print("  → You win this round! ✅")\n'
                            '        player_wins += 1\n'
                            '    elif computer_roll > player_roll:\n'
                            '        print("  → Computer wins this round! ❌")\n'
                            '        computer_wins += 1\n'
                            '    else:\n'
                            '        print("  → Draw! 🤝")\n'
                            '\n'
                            'print(f"\\n=== FINAL SCORE ===")\n'
                            'print(f"You: {player_wins} | Computer: {computer_wins}")\n'
                            'if player_wins > computer_wins:\n'
                            '    print("🏆 YOU WIN THE DUEL!")\n'
                            'elif computer_wins > player_wins:\n'
                            '    print("💻 Computer wins... try again!")\n'
                            'else:\n'
                            '    print("🤝 It is a draw!")'
                        ),
                        'expected_output': None,
                    },
                    {
                        'type': 'exercise',
                        'title': 'ASCII Slot Machine 🎰',
                        'content': (
                            "Build a slot machine game!\n\n"
                            "  1. Player starts with 100 coins\n"
                            "  2. Each spin costs 10 coins\n"
                            "  3. Spin 3 random symbols from: 🍒 🍋 🔔 ⭐ 💎\n"
                            "  4. Match 2 = win 20 coins, match 3 = win 50 coins\n"
                            "  5. Run for 5 spins and show final balance\n\n"
                            "Complete the TODO sections!"
                        ),
                        'voice': (
                            "Build a slot machine! Each spin costs 10 coins. "
                            "Match two symbols to win 20 coins, three to win 50. "
                            "Run five spins and show the final balance!"
                        ),
                        'starter_code': (
                            'import random\n'
                            '\n'
                            'symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]\n'
                            'coins = 100\n'
                            '\n'
                            'print("╔═══════════════════╗")\n'
                            'print("║   🎰 SLOT MACHINE ║")\n'
                            'print("╚═══════════════════╝")\n'
                            'print(f"Starting coins: {coins}\\n")\n'
                            '\n'
                            'for spin in range(1, 6):\n'
                            '    coins -= 10  # cost per spin\n'
                            '\n'
                            '    # TODO: Pick 3 random symbols\n'
                            '    s1 = random.choice(symbols)\n'
                            '    s2 = random.choice(symbols)\n'
                            '    s3 = random.choice(symbols)\n'
                            '\n'
                            '    print(f"Spin {spin}: | {s1} | {s2} | {s3} |", end=" ")\n'
                            '\n'
                            '    # TODO: Check for matches\n'
                            '    # If all 3 match: win 50 coins, print "JACKPOT! 🎉"\n'
                            '    # If any 2 match: win 20 coins, print "Nice! Two match!"\n'
                            '    # Otherwise: print "No luck..."\n'
                            '    # Hint: check s1==s2==s3 first, then check pairs\n'
                            '    pass\n'
                            '\n'
                            '    print(f"  Coins: {coins}")\n'
                            '\n'
                            'print(f"\\n=== GAME OVER ===")\n'
                            'print(f"Final coins: {coins}")\n'
                            'profit = coins - 100\n'
                            'if profit > 0:\n'
                            '    print(f"You made a profit of {profit} coins! 🎉")\n'
                            'elif profit < 0:\n'
                            '    print(f"You lost {abs(profit)} coins. Better luck next time!")\n'
                            'else:\n'
                            '    print("You broke even! 🤷")'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Three match: if s1 == s2 == s3',
                            'Two match: if s1==s2 or s2==s3 or s1==s3',
                            'Remember to add coins for wins: coins += 50 or coins += 20',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Game Loop Quiz',
                        'question': 'What are the 3 parts of a game loop?',
                        'voice': 'Quiz! What are the three parts of a game loop?',
                        'options': [
                            'Start, Middle, End',
                            'Input, Update, Render (display)',
                            'Load, Save, Quit',
                            'Create, Destroy, Repeat',
                        ],
                        'answer': 1,
                        'explanation': (
                            'The game loop has three core parts: '
                            'Input (get player actions), Update (process the game logic), '
                            'and Render (display the current state). This repeats every frame!'
                        ),
                        'explanation_voice': (
                            'Correct! Input, Update, Render — get actions, process logic, display state. '
                            'This repeats every frame in every game ever made!'
                        ),
                    },
                ],
            },

            # ---- Lesson 2: Dungeon Crawler Project ----
            {
                'id': 't_m11_l2',
                'title': 'Project: Dungeon Crawler',
                'icon': '🏰',
                'xp': 200,
                'steps': [
                    {
                        'type': 'story',
                        'title': 'Build a Real Dungeon Crawler! 🏰',
                        'content': (
                            "Agent Toby — final project time.\n\n"
                            "You will build a DUNGEON CRAWLER:\n"
                            "  🗺️  A map made of rooms (2D list)\n"
                            "  🏃  A player who moves through the dungeon\n"
                            "  💎  Items to collect\n"
                            "  👹  A monster to fight\n\n"
                            "This combines EVERYTHING: classes, lists, loops,\n"
                            "conditionals, random, and functions.\n\n"
                            "Let's build it! 🚀"
                        ),
                        'voice': (
                            "Final project! Build a dungeon crawler with a map, a player, "
                            "items to collect, and a monster to fight. "
                            "This uses everything you have learned. Let's build it!"
                        ),
                    },
                    {
                        'type': 'teach',
                        'title': '2D Lists as Game Maps',
                        'content': (
                            "A 2D list is a list of lists — perfect for a grid map:\n\n"
                            "    dungeon = [\n"
                            '        ["🚪", "  ", "💎"],\n'
                            '        ["  ", "##", "  "],\n'
                            '        ["👹", "  ", "🏆"],\n'
                            "    ]\n\n"
                            "Access cells with [row][col]:\n"
                            '    dungeon[0][0]  → "🚪"  (top-left)\n'
                            '    dungeon[2][2]  → "🏆"  (bottom-right)\n\n'
                            "Player position is just (row, col):\n"
                            "    player_row = 0\n"
                            "    player_col = 0\n\n"
                            "Movement:\n"
                            "    Up    → row - 1\n"
                            "    Down  → row + 1\n"
                            "    Left  → col - 1\n"
                            "    Right → col + 1\n\n"
                            "Check boundaries before moving!"
                        ),
                        'voice': (
                            "A 2D list is a list of lists — perfect for a grid map. "
                            "Access cells with row and column indexes. "
                            "Player position is just a row and column number. "
                            "Move by changing the row or column, but check boundaries first!"
                        ),
                    },
                    {
                        'type': 'exercise',
                        'title': 'Dungeon Crawler 🏰',
                        'content': (
                            "Complete this dungeon crawler! You need to:\n\n"
                            "  1. Add two more rooms to the dungeon map\n"
                            "  2. Complete the combat logic when meeting a monster\n"
                            "  3. Add item collection\n\n"
                            "The game auto-plays a random path through the dungeon."
                        ),
                        'voice': (
                            "Complete the dungeon crawler! Add rooms, combat, and item collection. "
                            "The game will auto-play a random path."
                        ),
                        'starter_code': (
                            'import random\n'
                            '\n'
                            '# === DUNGEON MAP ===\n'
                            '# Each room: (description, content_type, content_value)\n'
                            '# content_type: "empty", "item", "monster", "exit"\n'
                            'rooms = {\n'
                            '    (0, 0): ("Entrance Hall", "empty", None),\n'
                            '    (0, 1): ("Dusty Corridor", "item", "Health Potion"),\n'
                            '    (0, 2): ("Armoury", "item", "Iron Sword"),\n'
                            '    (1, 0): ("Dark Pit", "monster", {"name": "Goblin", "hp": 30, "atk": 5}),\n'
                            '    (1, 1): ("Treasure Room", "item", "Gold Coins"),\n'
                            '    (1, 2): ("Library", "empty", None),\n'
                            '    # TODO: Add room (2, 0) — a "Throne Room" with a strong monster\n'
                            '    # Example: ("Throne Room", "monster", {"name": "Dragon", "hp": 50, "atk": 10})\n'
                            '    # TODO: Add room (2, 1) — an "Ancient Vault" with a special item\n'
                            '    (2, 2): ("Exit Portal", "exit", None),\n'
                            '}\n'
                            '\n'
                            '# === PLAYER STATE ===\n'
                            'player = {"hp": 100, "atk": 10, "items": [], "pos": (0, 0)}\n'
                            '\n'
                            'def show_status():\n'
                            '    print(f"  HP: {player[\'hp\']} | ATK: {player[\'atk\']} | Items: {player[\'items\']}")\n'
                            '\n'
                            'def fight_monster(monster):\n'
                            '    """Fight a monster! Returns True if player wins."""\n'
                            '    m_hp = monster["hp"]\n'
                            '    m_atk = monster["atk"]\n'
                            '    print(f"  ⚔️ A {monster[\'name\']} attacks! (HP:{m_hp} ATK:{m_atk})")\n'
                            '    while player["hp"] > 0 and m_hp > 0:\n'
                            '        # TODO: Player attacks monster\n'
                            '        # damage = player["atk"] + random.randint(0, 5)\n'
                            '        # Subtract from m_hp, print the hit\n'
                            '        # Then monster attacks player if still alive\n'
                            '        # m_damage = m_atk + random.randint(0, 3)\n'
                            '        # Subtract from player["hp"]\n'
                            '        pass  # Replace this!\n'
                            '        break  # Remove this after adding combat!\n'
                            '    if m_hp <= 0:\n'
                            '        print(f"  ✅ You defeated the {monster[\'name\']}!")\n'
                            '        return True\n'
                            '    return False\n'
                            '\n'
                            '# === GAME LOOP ===\n'
                            'print("=== 🏰 DUNGEON CRAWLER ===")\n'
                            'visited = set()\n'
                            '\n'
                            'for turn in range(1, 15):\n'
                            '    pos = player["pos"]\n'
                            '    if pos not in rooms:\n'
                            '        print("You hit a wall! Turning back.")\n'
                            '        player["pos"] = (0, 0)\n'
                            '        continue\n'
                            '\n'
                            '    room_name, content_type, content_val = rooms[pos]\n'
                            '    print(f"\\nTurn {turn}: You enter the {room_name} {pos}")\n'
                            '\n'
                            '    if pos not in visited:\n'
                            '        visited.add(pos)\n'
                            '        if content_type == "item":\n'
                            '            player["items"].append(content_val)\n'
                            '            print(f"  💎 Found: {content_val}!")\n'
                            '        elif content_type == "monster":\n'
                            '            fight_monster(content_val)\n'
                            '        elif content_type == "exit":\n'
                            '            print("  🏆 You found the exit! YOU WIN!")\n'
                            '            show_status()\n'
                            '            break\n'
                            '    else:\n'
                            '        print("  (already explored)")\n'
                            '\n'
                            '    show_status()\n'
                            '\n'
                            '    if player["hp"] <= 0:\n'
                            '        print("💀 Game Over!")\n'
                            '        break\n'
                            '\n'
                            '    # Auto-move to a random adjacent room\n'
                            '    moves = [(0,1),(0,-1),(1,0),(-1,0)]\n'
                            '    dr, dc = random.choice(moves)\n'
                            '    new_pos = (pos[0]+dr, pos[1]+dc)\n'
                            '    if new_pos in rooms:\n'
                            '        player["pos"] = new_pos\n'
                            '    else:\n'
                            '        player["pos"] = random.choice(list(rooms.keys()))\n'
                            '\n'
                            'print(f"\\n=== ADVENTURE COMPLETE ===")\n'
                            'print(f"Rooms explored: {len(visited)}/{len(rooms)}")\n'
                            'show_status()'
                        ),
                        'expected_output': None,
                        'hints': [
                            'Add rooms: (2,0): ("Throne Room", "monster", {"name":"Dragon","hp":50,"atk":10})',
                            'Combat: damage = player["atk"] + random.randint(0, 5); m_hp -= damage',
                            'Monster turn: m_damage = m_atk + random.randint(0, 3); player["hp"] -= m_damage',
                        ],
                    },
                    {
                        'type': 'quiz',
                        'title': 'Game Map Quiz',
                        'question': 'How do 2D lists represent a game map?',
                        'voice': 'Quiz! How do 2D lists represent a game map?',
                        'options': [
                            'Each list element is a pixel on screen',
                            'Rows and columns form a grid — each cell is a map tile',
                            'They store the game soundtrack',
                            'They only work with graphics libraries',
                        ],
                        'answer': 1,
                        'explanation': (
                            'A 2D list forms a grid where rows and columns map to positions. '
                            'Each cell holds what is at that position — a wall, item, enemy, or empty space. '
                            'Access with grid[row][col].'
                        ),
                        'explanation_voice': (
                            'Correct! Rows and columns form a grid. Each cell is a map tile — '
                            'it could be a wall, an item, or an enemy. Access it with row and column indexes!'
                        ),
                    },
                ],
            },
        ],
    },
]
