
# Replacing text link with ading html tag
text = 'The link is gran.com. The price issol.com'
# Must have to wrapped with () round bracket.. here  " [\w]+ " a word "\." then adding Dot " [\w]+ " again a word
pattern = r'([\w]+\.[\w]+)'
# Here "\1" will replace the pattern
replacement = r'<a href="\1">\1</a>'
result = re.sub(pattern, replacement, text)
# Output: The link is <a href="gran.com">gran.com</a>. The price <a href="issol.com">issol.com</a>


text = "Additionally, there are.several job postings.available for Charge Solar in Canada on Indeed.com, indicating that they are an active and growing.company"
converted_text = re.sub(r'\.([\w]+)(?!\.com)', r'. \1', linked_text)
print(converted_text)
# Output: Additionally, there are. several job postings.available for Charge Solar in Canada on Indeed.com, indicating that they are an active and growing.company 
""" (?!\.com) is for excluding all .com """
