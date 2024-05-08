import re

pep7 = "I try to follow PEP7"
pep8 = "I try to follow PEP8"
peep8 = "I try to follow PEEP8"

print(re.findall('[A-Z]+[0-9]', pep7))
print(re.findall('[A-Z]+[0-9]', pep8))
print(re.findall('[A-Z]+[0-9]', peep8))

# replace
print(re.sub('[A-Z]+[0-9]','PEP8 Python Style Guide', pep7))
