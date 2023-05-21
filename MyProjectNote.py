
# Replacing text link with ading html tag
text = 'The link is gran.com. The price issol.com'
# Must have to wrapped with () round bracket.. here  " [\w]+ " a word "\." then adding Dot " [\w]+ " again a word
pattern = r'([\w]+\.[\w]+)'
# Here "\1" will replace the pattern
replacement = r'<a href="\1">\1</a>'
result = re.sub(pattern, replacement, text)
# Output: The link is <a href="gran.com">gran.com</a>. The price <a href="issol.com">issol.com</a>


text = "Additionally, there are.several job postings.available for Charge Solar in Canada on Indeed.com, indicating that they are an active and growing.company"
converted_text = re.sub(r'(\b(?:are|several))\.(\w+\b)(?!\.com)', r'\1. \2', text)
print(converted_text)
# Output: Additionally, there are. several job postings.available for Charge Solar in Canada on Indeed.com, indicating that they are an active and growing.company 

"""
(\b(?:are|several))\.(\w+\b)(?!\.com).
(\b(?:are|several)) captures the words "are" or "several" as a group using a non-capturing group (?: ).
The word boundary \b ensures that it matches the whole word and not a partial word.
\. matches the dot character.
(\w+\b) captures one or more word characters (letters, digits, or underscores) followed by a word boundary. This captures the word immediately after the dot.
(?!\.com) is a negative lookahead assertion that ensures the pattern doesn't match if the dot is followed by ".com".
The (?!\ ) construct is used to specify that the pattern inside the lookahead should not be present at that point.
In the replacement pattern r'\1. \2', the \1 represents the first captured group, which is "are" or "several".
The dot and space are added between \1 and \2, which is the second captured group, representing the word immediately after the dot.
"""
