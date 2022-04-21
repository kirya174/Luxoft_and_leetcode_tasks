import re

match = re.search(r"\d{3}-\d{3}-\d{3}","Phone 123-123-123")
print(match[0] if match else"Not found")
match = re.search(r"\d{3}-\d{3}-\d{3}","Phone 123")
print(match[0] if match else"Not found")

print(re.split(r"[1-9]\w","1One2Two3Three4Four3a"))