import re


pattern = r'\("?(.*?)"?,\s"?(.*?)"?,\s"?(.*?)"?\)'
test_string = 'User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")'


match = re.search(pattern, test_string)

if match:
    num = 1
    for ma in match.group():
        print("Match found:", match.group(num))
        num += 1
else:
    print("No match found.")

