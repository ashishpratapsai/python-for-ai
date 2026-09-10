# Python for AI Automation — Learning Log

GOAL: n8n (have it) + Python (learning) → high-paid AI automation.
Build agents n8n can't, expose via webhook, charge for outcomes.

ROADMAP: 28 weeks, 6 shipped products.
- Phase 1: Read Python under 200 lines (weeks 1-4)
- Phase 5: n8n + Python automation product ← my home turf

## Day 1 — Functions
Concept: def, parameters, return.
Built: greet(name), add(a,b), multiply(a,b)
What broke: missing return → None
            missing colon → SyntaxError
            one argument instead of two → TypeError
What surprised me: If I am not placing the colon at the end, then the function is not working.

## Day 2 — if/elif/else
Concept: control flow, decisions inside functions.
Built: check_number(n), calculate(a, b, operation)
What broke: Basically, what I was not able to do was place the quotes  when I was equating them to the operations. That was the mistake. 
What surprised me:So vnu2 is the system. If you're passing something or if you're creating some good voice, don't forget to place the quotes --- Quotes are very important

## Day 3 — for loops
Concept: loops, iterating over lists, enumerate()
Built: calculate() automated over a list,
       numbered video list with enumerate
What broke: f-string syntax broke when index was outside quotes
What surprised me: enumerate() can start from any number, 
                   not just 0


## Day 4 — Dictionaries
Concept: key-value pairs, accessing values by key
Built: analyze_video() — returns title, word_count, 
       char_count, is_title_long for a list of videos
What broke: at first, I was not able to identify that we have to define the function only once. I was defining the function inside the for loop, I think, which was wrong. 
What surprised me: so, in a list, when we are defining the list within the strings, if I am not providing the comma, then whenever we are calling that from the list, it is going to merge them both.  

## Day 5 — Nested Dictionaries
Concept: dictionaries inside dictionaries, 
         accessing nested values with chained brackets
Built: get_video_stats() — extracts title, likes, 
       subscribers from a nested video dictionary
What broke: Got some what confused that how the function will take the dictionary.
What surprised me:we can pass any this in the function , like any thing whether it is a list, dictionary or a string it doen,t matter

## Revision Day — Days 1-5 Review
Built: check_views(), enumerate channels, 
       channel_summary() with nested access
What broke: and <10000 syntax, f-string without 
            curly braces, wrong division syntax
What surprised me:when accesing from dictionary and if have to the the value again for division and so then i have have to acces it from the start.

## Day 7 — While Loops
Concept: while True, break, return to escape, input inside loop
Built: ask_until_valid(), password checker, get_valid_operation()
What broke: didn't know where to put the loop — inside function
What surprised me: input() must be inside loop, break vs return


## Day 8 — Data Types
Concept: str, int, float, bool, NoneType, 
         type conversion, try/except
Built: describe_value() — type, value, can_do_math
       safe_to_number() — graceful type conversion
What broke: Nothing broke today.
What surprised me: If you don't store a result with =, 
                   Python throws it away immediately. 
                   int(value) and number = int(value) 
                   look similar but are completely different.


## Day 9 — Lists and List Methods
Concept: list methods, list comprehension, 
         slicing, negative indexing, strip()
Built: filter_videos() — comprehension, sort, strip
       video_stats() — total, longest, shortest
What broke: Forgot to initialize longest_count and 
            smallest_count before the loop. Variables 
            must be set before the loop runs.
What surprised me: len(videos) counts list items. 
                   len(video.split()) counts words. 
                   Same function, completely different 
                   result based on what you pass in.



## Day 10 — String Methods
Concept: strip, title, upper, lower, replace,
         split, startswith, endswith, in, len
Built: format_student() — cleans messy Institura student data
       analyze_batch() — parses IIT-JEE batch codes
What broke: Wrapped split() in [] making list inside list.
            Used parts[2] without defining parts first.
What surprised me: split() already returns a list. 
                   Never wrap it in [] again.



## Day 11 — Error Handling
Concept: try/except, ValueError, KeyError, 
         AttributeError, .get(), or for None defaults
Built: safe_parse_student() — handles missing fields,
       wrong types, None values, messy strings
What broke: Put two conversions in one try block —
            first failure killed second silently
What surprised me: One try block = one risky operation.
                   Never combine. Each failure must be
                   caught independently.




## Day 12 — File I/O
Concept: open(), read/write/append modes,
         with statement, readlines(), strip(), split()
Built: save_students() — writes student list to file
       read_students() — reads file back to list of dicts
What broke: Called .split().split() — chained two splits
            instead of .strip().split(). Lists don't have
            .split() method, only strings do.
What surprised me: open() and the loop are separate steps.
                   First open the file, then loop inside it.
                   readlines() gives a list — each line is
                   a string with \n at the end.
                   strip() then split() — always in that order.

## Day 13 — *args and **kwargs
Concept: *args collects positional args as tuple,
         **kwargs collects keyword args as dictionary
Built: calculate_total(*args) — total and average of any marks
       create_student(**kwargs) — flexible student dictionary  
       create_report(*args, **kwargs) — combined both
What broke: Tried to use length variable outside function —
            variables defined inside function don't exist outside.
            Stored kwargs in unnecessary variable — 
            kwargs is already a dictionary, access directly.
What surprised me: kwargs is already a dictionary — no need to 
                   store in another variable. Access with kwargs["key"]
                   or kwargs.get("key", default) directly.
                   Compute first, store in variables, then map to 
                   dictionary — that's clean professional Python.




## Day 14 — Lambda Functions
Concept: lambda syntax, key=lambda in sorted(),
         filter(), map(), dictionary unpacking {**s}
Built: classify, format_name, sorted by marks/name,
       filter IIT-JEE students, map grades to students
What broke: Nothing broke today.
What surprised me: Instead of defining a separate function
                   just to pass to sorted() or filter(),
                   lambda lets you write it inline in one line.
                   filter removes items. map transforms items.
                   Same size list vs smaller list — key difference.



## Day 15 — Basic OOP (Classes and Objects)
Concept: class, __init__, self, methods, objects,
         class dependency, objects inside objects
Built: Student class — get_grade(), get_status(),
       is_pass(), to_dict(), summary()
       Batch class — add_student(), get_topper(),
       get_average(), get_summary()
What broke: Removed Student class — NameError proved
            Batch depends on Student. Order matters.
What surprised me: Classes can depend on each other —
                   Batch uses Student objects inside it.
                   self is passed automatically by Python
                   when calling a method — you write it
                   in definition but never in the call.
                   Position of arguments determines which
                   value goes to which parameter.

## Day 17 — Project: Institura Student Processor
Built: read_students(filepath) — reads CSV into 
       list of student dictionaries
What broke: Hardcoded filename instead of using 
            filepath parameter. Used read() instead 
            of readlines().
What surprised me: lines[1:] — one slice skips the 
                   entire header row. Clean and simple.


## Day 18 — Project: Institura Student Processor (Day 2)
Built: clean_student() — strips, titles, converts marks
       load_students() — combines read + clean in one call
       get_student_summary() — adds grade and status
What broke: Semicolon instead of colon in load_students.
            Used 'students' instead of 'student' parameter.
            Incomplete if/else chain — last condition needs else.
What surprised me: Python reads all function definitions first
                   then executes from the first non-function line.
                   Functions are preparation. The call is the trigger.



## Day 19 — Project: Institura Student Processor (Day 3)
Built: analyze_batch() — topper, average, pass/fail, fee counts
       filter_by_batch() — filter students by batch name
What broke: Typo pendind_count instead of pending_count —
            Python created a new variable silently.
            paid_count: pass_count — wrong variable name
            in return dictionary.
What surprised me: Same function analyze_batch() works on
                   all students, IIT-JEE only, or NEET only
                   — just change what you pass in.


## Day 20 — Project: Institura Student Processor (Day 4)
Built: generate_report() — writes full analysis to text file
What broke: Two with open() blocks — second overwrote first.
            NERET typo — filter returned empty list silently.
What surprised me: One with open() block handles everything.
                   f-strings with :.2f format decimals cleanly.
                   A real report generated from messy CSV data
                   in under 100 lines of Python.


## Day 21 — Project: Institura Student Processor (Day 5)
Built: main.py — terminal menu with while True loop
What broke: processor.py running code on import —
            fixed with if __name__ == "__main__"
            python vs python3 on Mac
What surprised me: if __name__ == "__main__" — 
                   code only runs when file is run directly,
                   not when imported. Every Python file needs this.

## Day 22 — Project: Institura Student Processor (SHIPPED)
Concept: README writing, final polish, shipping to GitHub
Built: README.md — project description, how to run, what I learned
       Final cleanup of processor.py — removed commented code
       Fixed typo in main.py — IIt-JEE → IIT-JEE
What broke: Nothing today — clean session.
What surprised me: Writing the README in my own words made me 
                   realise how much I actually built. Explaining 
                   it to someone else is harder than building it.

## Day 23 — Project 2: Transcript Extractor (Day 1)
Built: read_transcript(), extract_keywords(), save_summary()
What broke: return inside loop — returned first match only.
            keywords.lower() on a list — should be keyword.lower()
            results.count() — should be len(results)
What surprised me: any() with generator expression — 
                   checks all keywords in one line.
                   join() converts list to clean string.


## Day 25 — Modules and Packages
Concept: modules vs packages, __init__.py,
         relative imports with dot notation,
         separating concerns into different files
Built: institura_pkg — reader.py, cleaner.py, analyzer.py
What broke: readline() vs readlines() — one letter difference.
            roll_numbber typo — KeyError.
            Wrong import path — fixed with relative import .reader
What surprised me: __init__.py empty file makes a folder 
                   a package. The dot in .reader means 
                   "same package I'm in."

## Day 26 — Type Hints
Concept: parameter types, return types, list[dict],
         Optional, self-documenting code
Built: Added type hints to all institura_pkg functions
       get_batch_names() — returns unique batch names
What broke: Calling code in analyzer.py outside 
            if __name__ == "__main__" — NameError
What surprised me: Type hints don't change how code runs.
                   They document intent and help Claude Code
                   write better suggestions.

## Day 27 — Pydantic
Concept: BaseModel, field_validator, coercion,
         validation errors, self-cleaning models
Built: Student model (basic) and StudentV2 (with validators)
       marks validation — no negative, no > 100
       clean_name validator — auto strip and title case
What broke: marks validator used v > 0 instead of v > 100
What surprised me: Pydantic coerces "85" string to 85 int
                   automatically. And validators can clean
                   data — not just validate it.

## Day 28 — Environment Variables
Concept: .env files, python-dotenv, os.getenv(),
         .gitignore for secrets, .env.example pattern
Built: Institute config loader — name, API key, debug, max students
What broke: DEBUG = True with spaces — .env requires no spaces around =
            Jupyter caches env vars — always use terminal for .env
What surprised me: .env.example is what you push to GitHub —
                   shows what variables exist without real values.
                   os.getenv() safer than os.environ[] — 
                   returns None instead of crashing.


## Day 29 — Logging
Concept: logging levels, basicConfig, getLogger(__name__),
         replacing print() with professional logging
Built: Added logging to reader.py and cleaner.py
       INFO for successful operations
       WARNING for corrupted lines and invalid marks
What broke: %(levrlname)s typo — one letter breaks the format
What surprised me: level=logging.WARNING hides debug and info
                   automatically — one line controls all verbosity.
                   %(name)s shows which module logged — 
                   institura_pkg.reader tells you exactly where.

## Day 30 — pytest
Concept: test files, test functions, assert statements,
         running pytest -v, reading failure output
Built: test_cleaner.py — 4 tests for clean_student()
       test strips name, handles absent marks,
       converts string marks to int, lowercases email
What broke: Relative import in cleaner.py — fixed by
            changing from .reader to from reader for
            standalone testing. assert 85 == 99 — 
            intentional fail to see failure output.
What surprised me: pytest failure output is incredibly clear —
                   shows exactly which line, what you got,
                   what you expected. AI writes code but YOU
                   decide what to test and whether tests
                   prove the right things.

## Day 31 — httpx
Concept: HTTP requests, GET/POST, status codes,
         response.json(), error handling, connection errors
Built: get_user(user_id) — fetch one user with error handling
       get_all_users() — fetch all users, clean list
What broke: "user" instead of "users" in URL — 404
            Missing f-string — {user_id} not replaced
What surprised me: response.json() converts API response
                   to Python dictionary automatically.
                   Same nested dict access as Day 5.
                   Two types of errors: status code errors
                   and connection errors — handle both.


## Day 32 — JSON Deeply
Concept: json.dumps, json.loads, json.dump, json.load,
         s = string, no s = file
Built: save_students_json(), load_students_json(),
       extract_response() — Anthropic API preview
What broke: json.loads() on dict that was already parsed.
            content is a list — content[0]["text"] not content["text"].
            load result not stored — result fell on the floor.
What surprised me: Anthropic API response uses same nested
                   dict access as Day 5. Phase 3 is closer
                   than it feels.

## Day 33 — Async/Await
Concept: async def, await, asyncio.gather(),
         asyncio.run(), AsyncClient
Built: fetch_user() async, fetch_multiple_users(),
       sync vs async speed comparison
What broke: user_id vs user_ids variable name mismatch
What surprised me: Async 0.58s vs Sync 2.05s — 3.5x faster.
                   fetch_user(1) creates coroutine but doesn't run it.
                   await actually runs it.

## Day 34 — Context Managers
Concept: with statement, setup/yield/teardown,
         @contextmanager decorator, yield connection
Built: timer() — measures execution time
       database_connection() — simulates DB open/close
What broke: _IncompleteInputError in Jupyter — Jupyter issue, not code
What surprised me: yield is the dividing line.
                   Before yield = setup.
                   After yield = teardown.
                   Whatever you yield becomes the "as" variable.