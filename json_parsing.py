import json

class JsonParser:

    def __init__(self):
        pass
    
    def parse_json_string(self, json_str):
        return json.loads(json_str)

    def parse_json_file(self, file_path):
        json_file = open(file_path)
        file_content = json_file.read()
        return self.parse_json_string(file_content)


# parse values into dictionary
parser = JsonParser()
value_dict = parser.parse_json_file('data.json')

# iterate over the dictionary
for key in value_dict:
    print value_dict[key]
