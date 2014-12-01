#PYTHON CONVENTION

##Indentation
Use 4 spaces per indentation level.

##Binary operators
Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).
If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.

```python
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)
```
Don't use spaces around the = sign when used to indicate a keyword argument or a default parameter value.
```python
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
```
##Comments
Write English only

###Blocks comments
Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. 
Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).
Paragraphs inside a block comment are separated by a line containing a single #.

###Inline Comments
Use inline comments sparingly.

##Naming conventions
###Names to Avoid
Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.

###Package and Module Names
Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.

###Class Names and Exception Names
Should normally use the CapWords convention.

###Function Names
Function names should be lowercase, with words separated by underscores as necessary to improve readability.

###Function and method arguments
Always use `self` for the first argument to instance methods.

Always use `cls` for the first argument to class methods.

If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. 
Thus `class_` is better than `clss`. (Perhaps better is to avoid such clashes by using a synonym.)

###Constants
Constants are usually defined on a module level and written in all capital letters with underscores separating words. 
Examples include `MAX_OVERFLOW` and `TOTAL`.

