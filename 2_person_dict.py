person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}
 
#print(person)

# print out the name of the second child
#children = person['children']
#print(children[1])

# print out the name of the cat
#animal=person["pets"]['cat']
#print(animal)

# use a loop to print out the names of each child
list_of_children=person["children"]
print(list_of_children)

for item in list_of_children:
    print(item)



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

pets_dictionary = person['pets']
for k,v in pets_dictionary.items():
    print(f'the type of pet is: {k} and the name of hte pet is: {v}')