import re
from collections import Counter

def is_strong_password(password: str) -> bool:
    # בדיקה של אורך מינימלי
    if len(password) < 8:
        return False

    # בדיקה של lowercase, uppercase, digit, special char
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False

    # בדיקה שתו לא מופיע יותר מפעמיים
    counts = Counter(password)
    if any(v > 2 for v in counts.values()):
        return False

    # בדיקה שאין רצפים של 3 תווים עוקבים
    for i in range(len(password) - 2):
        c1, c2, c3 = password[i], password[i+1], password[i+2]
        # המרת תווים למספרים לפי ASCII
        if ord(c2) == ord(c1) + 1 and ord(c3) == ord(c2) + 1:
            return False

    return True

# דוגמאות בדיקה
test_passwords = [
    "Abc!1234",    # False (יש רצף abc)
    "A!b2C#d4",    # True
    "aaaBBB11!",   # False (a מופיעה 3 פעמים)
    "Ab1!xyZ9",    # True
]

for pwd in test_passwords:
    print(pwd, is_strong_password(pwd))
