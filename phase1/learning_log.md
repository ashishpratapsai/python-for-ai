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