import json 

# Define the dictionary of Indian states and capitals
indian_states_capitals = {
    "Telangana": "Hydrabad",
    "Andhra Pradesh": "Amaravati",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bangaluru",
    "Kerala": "Thiruvananthapuram",
    "Gujarat": "Gandhinagar",
    "Maharashtra": "Mumbai"
}

# Write the dictionary into a JSON file
with open("indian_states_capitals.json", "w") as json_file:
    json.dump(indian_states_capitals,json_file)
print("Indian states and capitals written to indian_states_capitals.json")
print(type(indian_states_capitals))

# output
# Indian states and capitals written to indian_states_capitals.json
# <class 'dict'>