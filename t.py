import re

pattern = r'({U, B}*?\.)(a*?\()'  # Your regular expression pattern
test_string = "UBBBBBBB.ser.all()"  # Your test string

# Use re.search() to search for the pattern in the test string
match = re.search(pattern, test_string)

if match:
    print("Match found:", match.group())  # Prints the matched string
else:
    print("No match found.")

