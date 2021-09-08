tech_stack = ["Python", "Django", "Javascript", "Angular", "Vue"]
print(len(tech_stack))
# First item
print(tech_stack[0])
print(tech_stack[1])
print(tech_stack[3])

mixed_data_types = ["Jefferson", 23, 5.2, "single", 2535]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
first_company = it_companies[0]
print(first_company)
middle_company = it_companies[3]
print(middle_company)
last_index = len(it_companies) -1
last_company = it_companies[last_index]
print(last_company)

# Adding an Item
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("Twitter")
print(it_companies)

# Inserting an Item
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(4, "Twitter")
print(it_companies)

# upper case to one of the companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
uppercase = it_companies[3].upper()
print(uppercase)

# join function
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
result = "#".join(it_companies)
print(result)

# in function
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exists = "Apple" in it_companies
print(does_exists)

# Sort() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

# reverse() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse=True)
print(it_companies)

# Slice() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_three = it_companies[3:]
print(first_three)
# The last three 
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_three = it_companies[:3]
print(last_three)
# The middle company
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_name = it_companies[::3]
print(middle_company)

# remove() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(0)
print(it_companies)
it_companies.pop(3)
print(it_companies)
del it_companies[::1]
print(it_companies)


# Join() method
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Python", "Django", "Flask"]
full_stack = front_end + back_end
print(full_stack)
full_stack.append("SQl")
print(full_stack)

# Exercise: Level2 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
# Add min and Max
