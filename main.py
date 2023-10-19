import re


def validate_url(url):
    # Regular expression pattern for URL validation
    pattern = re.compile(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

    # Check if the URL matches the pattern
    if re.match(pattern, url):
        return True
    else:
        return False


# Sample usage
url = input("Enter a URL: ")

if validate_url(url):
    print("The URL is valid.")
else:
    print("The URL is not valid.")
