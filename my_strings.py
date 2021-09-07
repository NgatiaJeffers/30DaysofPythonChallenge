# STRING CHALLENGES
# concatenate
string = "Thirty"
string1 = "Days"
string2 = "Of"
string3 = "Python"
space = " "
sentence = string + space + string1 + space + string2 + space + string3

print(sentence)

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

first_word = company[:6]
print(first_word)
# index()
sub_string = "Coding"
print(company.index(sub_string))
# replace()
print(company.replace("Coding", "Python"))
print(company.replace("All", "Everyone"))
# split()
print(company.split(" "))
companies = "Faceblook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))
# character index
first_letter = company[0]
print(first_letter)
last_letter = company[-1]
print(last_letter)
tenth_letter = company[10]
print(tenth_letter)

# find()
para = "You cannot end a sentence with because because because is a conjuction"
sub_string = "because"
print(para.find(sub_string))


