"""
=========================================================
ASSERT AND PASS IN PYTHON
=========================================================

---------------------------------------------------------
1️⃣ WHAT IS assert?
---------------------------------------------------------

assert is used for debugging purposes.

It checks whether a condition is True.

If the condition is False:
→ Python raises AssertionError.
→ Program stops (unless handled).

Simple meaning:
assert = "This condition must be True."

---------------------------------------------------------
SYNTAX
---------------------------------------------------------

assert condition, "Optional error message"

---------------------------------------------------------
WHEN TO USE assert?
---------------------------------------------------------

✔ During development
✔ To verify assumptions
✔ For internal testing
✔ To catch programming mistakes early

NOT recommended for:
❌ User input validation
❌ Production error handling

---------------------------------------------------------
WHY NOT USE assert FOR USER VALIDATION?
---------------------------------------------------------

Because assert statements can be disabled.

When Python is run in optimization mode:

    python -O script.py

Python removes all assert statements.

That means:
→ Assertions will NOT execute.
→ Validation will be skipped.

So assert should NOT be used for critical validation.
Use raise instead for production validation.

---------------------------------------------------------
EXAMPLE 1- Normal assert behavior
---------------------------------------------------------
"""

x = -1
assert x > 0, "x must be positive"
print("Program continues")


"""
Since x > 0 is False:
→ Python raises AssertionError
→ Program stops
→ "Program continues" does NOT print
"""

"""
---------------------------------------------------------
EXAMPLE 2- assert in optimization mode
---------------------------------------------------------

If you run:

    python -O script.py

Python removes assert statements internally.

So the code behaves like this:
"""

x = -1
# assert x > 0, "x must be positive"   (Removed in -O mode)
print("Program continues")

"""
Output:
Program continues

Because assert was ignored.
"""

"""
---------------------------------------------------------
Difference Between raise and assert
---------------------------------------------------------

raise  → Used in production to enforce rules.
assert → Used in development for debugging checks.

raise will ALWAYS execute.
assert may be ignored in optimized mode.

---------------------------------------------------------
IMPORTANT DIFFERENCE
---------------------------------------------------------

assert → Stops program if condition fails.
pass   → Does nothing, program continues.

---------------------------------------------------------
FINAL SUMMARY
---------------------------------------------------------

assert:
- Used for debugging.
- Checks if condition is True.
- Raises AssertionError if False.
- Can be ignored in optimized mode.

pass:
- Does nothing.
- Used as placeholder.
- Required when Python expects a block.

=========================================================
"""
