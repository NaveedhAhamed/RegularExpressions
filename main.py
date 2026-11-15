
import re

# ==========================================================
# 1. BASIC SEARCHING - re.search()
# ==========================================================

text = "My name is Naveedh and I am learning Python."

pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Found:", result.group())
    print("Starting position:", result.start())
    print("Ending position:", result.end())
else:
    print("Not found!")


# ==========================================================
# 2. re.match() - MATCH ONLY AT THE BEGINNING
# ==========================================================

text = "Python is an amazing language."

result = re.match("Python", text)

if result:
    print("\nMatch:", result.group())
else:
    print("\nNo match at the beginning!")


# ==========================================================
# 3. re.findall() - FIND ALL MATCHES
# ==========================================================

text = "I have 10 apples, 20 oranges and 30 bananas."

numbers = re.findall(r"\d+", text)

print("\nAll numbers:", numbers)


# ==========================================================
# 4. re.finditer() - FIND MATCHES WITH POSITIONS
# ==========================================================

text = "Python 100 Java 200 C++ 300"

matches = re.finditer(r"\d+", text)

print("\nFinding numbers with positions:")

for match in matches:
    print("Value:", match.group())
    print("Start:", match.start())
    print("End:", match.end())


# ==========================================================
# 5. re.sub() - REPLACE MATCHING TEXT
# ==========================================================

text = "I love Java. Java is powerful."

new_text = re.sub(r"Java", "Python", text)

print("\nReplaced text:", new_text)


# ==========================================================
# 6. re.split() - SPLIT TEXT USING A PATTERN
# ==========================================================

text = "Python,Java;C++;JavaScript"

languages = re.split(r"[,;]", text)

print("\nLanguages:", languages)


# ==========================================================
# 7. REGULAR EXPRESSION SPECIAL CHARACTERS
# ==========================================================

text = "cat cot cut c9t"

# . = Any character except newline
print("\nDot:", re.findall(r"c.t", text))

# ^ = Beginning of a string
print("Beginning:", re.findall(r"^cat", text))

# $ = End of a string
print("Ending:", re.findall(r"c9t$", text))

# [] = Match characters inside brackets
print("Character set:", re.findall(r"c[ao]t", text))

# [^] = Characters NOT inside brackets
print("Negation:", re.findall(r"c[^ao]t", text))


# ==========================================================
# 8. QUANTIFIERS - HOW MANY TIMES?
# ==========================================================

text = "a aa aaa aaaa aaaaa"

# * = Zero or more
print("\nStar:", re.findall(r"a*", text))

# + = One or more
print("Plus:", re.findall(r"a+", text))

# ? = Zero or one
print("Question:", re.findall(r"ab?", "a ab abb"))

# {n} = Exactly n times
print("Exactly 3:", re.findall(r"a{3}", text))

# {n,m} = Between n and m times
print("Between 2 and 4:", re.findall(r"a{2,4}", text))


# ==========================================================
# 9. SPECIAL SEQUENCES
# ==========================================================

text = "Python 123 is easy 456!"

# \d = Any digit (0-9)
print("\nDigits:", re.findall(r"\d", text))

# \D = Anything except digits
print("Non-digits:", re.findall(r"\D", text))

# \w = Letters, digits and underscore
print("Word characters:", re.findall(r"\w+", text))

# \W = Anything except word characters
print("Non-word characters:", re.findall(r"\W", text))

# \s = Whitespace
print("Whitespace:", re.findall(r"\s", text))

# \S = Anything except whitespace
print("Non-whitespace:", re.findall(r"\S+", text))


# ==========================================================
# 10. GROUPS - CAPTURING SPECIFIC INFORMATION
# ==========================================================

text = "Name: Naveedh, Age: 20"

pattern = r"Name: (\w+), Age: (\d+)"

result = re.search(pattern, text)

if result:
    print("\nFull match:", result.group(0))
    print("Name:", result.group(1))
    print("Age:", result.group(2))
    print("All groups:", result.groups())


# ==========================================================
# 11. NAMED GROUPS
# ==========================================================

text = "Email: naveedh@gmail.com"

pattern = r"Email: (?P<email>[\w.]+@[\w.]+\.\w+)"

result = re.search(pattern, text)

if result:
    print("\nEmail:", result.group("email"))


# ==========================================================
# 12. ALTERNATION - OR OPERATOR
# ==========================================================

text = "I like Python and Java."

pattern = r"Python|Java"

print("\nLanguages found:", re.findall(pattern, text))


# ==========================================================
# 13. FLAGS - IGNORE CASE
# ==========================================================

text = "PYTHON python Python PyThOn"

matches = re.findall(r"python", text, re.IGNORECASE)

print("\nIgnore case:", matches)


# ==========================================================
# 14. VALIDATING EMAIL ADDRESSES
# ==========================================================

emails = [
    "naveedh@gmail.com",
    "hello@yahoo.com",
    "invalid-email",
    "test123@outlook.com"
]

email_pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"

print("\nEmail validation:")

for email in emails:
    if re.fullmatch(email_pattern, email):
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")


# ==========================================================
# 15. EXTRACTING PHONE NUMBERS
# ==========================================================

text = """
Call me at 0771234567.
Office: 0112345678.
Another number: 0719876543.
"""

phone_pattern = r"\b0\d{9}\b"

phones = re.findall(phone_pattern, text)

print("\nPhone numbers:", phones)


# ==========================================================
# 16. GREEDY VS NON-GREEDY MATCHING
# ==========================================================

text = "<h1>Hello</h1><h2>Python</h2>"

# Greedy - matches as much as possible
print("\nGreedy:", re.findall(r"<.*>", text))

# Non-greedy - matches as little as possible
print("Non-greedy:", re.findall(r"<.*?>", text))


# ==========================================================
# 17. LOOKAHEAD - FIND WITHOUT INCLUDING THE NEXT PART
# ==========================================================

text = "100USD 200LKR 300USD"

# Find numbers followed by USD
result = re.findall(r"\d+(?=USD)", text)

print("\nUSD amounts:", result)


# ==========================================================
# 18. LOOKBEHIND - FIND WITHOUT INCLUDING PREVIOUS PART
# ==========================================================

text = "$100 $200 LKR300"

# Find numbers preceded by $
result = re.findall(r"(?<=\$)\d+", text)

print("\nDollar amounts:", result)


# ==========================================================
# 19. COMPILED REGULAR EXPRESSIONS
# ==========================================================

text = "Python 123 Java 456 C++ 789"

pattern = re.compile(r"\d+")

print("\nCompiled pattern:", pattern.findall(text))


# ==========================================================
# 20. PRACTICAL PROJECT - EXTRACT INFORMATION
# ==========================================================

text = """
Name: Ahmed
Email: ahmed@gmail.com
Phone: 0771234567

Name: John
Email: john@yahoo.com
Phone: 0712345678
"""

pattern = r"""
Name:\s*(?P<name>\w+)
\s*Email:\s*(?P<email>[\w.+-]+@[\w-]+\.[a-zA-Z]{2,})
\s*Phone:\s*(?P<phone>0\d{9})
"""

people = re.finditer(pattern, text, re.VERBOSE)

print("\nExtracted people:")

for person in people:
    print("Name:", person.group("name"))
    print("Email:", person.group("email"))
    print("Phone:", person.group("phone"))
    print("----------------------")


print("\nREGULAR EXPRESSIONS LESSON COMPLETED!")
