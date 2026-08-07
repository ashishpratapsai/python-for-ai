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