# Content Overview
1. Python Regular Expression
# Python Regular Expression
1. Lesson content:
  - What is regular expression
  - How to use re.search() to match a pattern against a string
  - Regular expression metacharacters
2. What i learned
  - A regular expression is a special sequence of characters that defines a pattern for complex string-matching functionality.
  - Python has built-in module `re` for regular expression.
  - `re.search(x, y)`: Scan `y` looking for the first location where the pattern `x` matches. If a match is found, then return the match object. Otherwise, it returns `None`.
  - Regex contains special characters called *metacharacters*
    - A set of characters specified or ranges in square brackets `[]` makes up a character class that counts as matches.
      - `-` : matches in a range from `x` to `y`
    - dot `.`: matches any single character except a newline.
    - `|`: mean OR, `x|y` mean either  `x` or `y` is matches
    - lowercase W `\w` : Match if character is a word character as letters,digits, and underscore `_` , equivalent to `[a-zA-Z0-9_]`.
    - uppercase w `\W` : Opposite of `\w`, match any none word characters `%^&*()`..ect...
    - `\d`: matches any numerical character.
    - `\D`: matches any character that isn’t a numerical character.
    - `\s`: matches any white space and newline `\n` character
    - `\S`: matches any character that it's white space or newline `\n` character
    - An anchor dictates a particular location in the search string where a match must occur.
    - `^` or `\A`: an anchor dictates the match must occur at start of the string.
    - `$` or `\Z`: an anchor dictates the match must occur at end of the string.
    - `\b`: Anchors a match to a word boundary.
    - `\B`: Anchors a match to a location that isn’t a word boundary, the opposite of `\b`.
    - A quantifier metacharacter immediately follows a portion of a `regex` and indicates how many times that portion must occur for the match to succeed.
    - `*`: Matches zero or more repetitions of the preceding regex.
    - `+`: Matches one or more repetitions of the preceding regex.
    - `?`: Matches only zero or one repetitions of the preceding regex.