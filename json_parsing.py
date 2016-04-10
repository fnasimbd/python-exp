import json

# read file
json_file = open('data.json')
file_content = json_file.read()

# parse values into dictionary
value_dict = json.loads(file_content)

# iterate over the dictionary
for key in value_dict:
    print value_dict[key]
