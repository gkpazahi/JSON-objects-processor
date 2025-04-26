"""Docstrings: """
# Modules necessaire
import json

# sources of the json object within this main file.
# json string
player_json_string = """
{
        "playerId": 1,
        "name": "Roger Federer",
        "age": 42,
        "skillLevel": "Professional",
        "contact": {
          "email": "roger.federer@example.com",
          "phone": "+1234567890"
        },
        "registeredOn": "2023-10-01"
      }
"""
person_dict = {
    "name": "Bob",
    "languages": ["English", "French"],
    "married": True,
    "age": 32
}

# son objects external to this file.
# json filename as global variables
filename = "states.json"
filename2 = "players.json"
filename3 = "tennis_players.json"

# Functions to work with this internal json objects and json file.
# parsing internal json string with loads() function
def parsing_json_string(json_str: str) -> dict:
    data = json.loads(json_str)
    return data

# parsing internal json string with loads() function
def get_json_from_file(json_file) -> list:
    with open(json_file, mode="r", encoding="UTF-8") as srcFile:
        data = json.load(srcFile)
        return data
        
# serializing a python dictionary as a json string using dumps()
def transform_in_jsonString(dictionary: dict):
    return json.dumps(dictionary, indent = 4, sort_keys=True)

# saving or storing json objrct in a json file using json dump() function
def save_json_to_file(data, filename) -> bool:
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent = 4, sort_keys=True)
        return True
         

# Driver or main function
def main():
    # Player data from internal file json string
    data = parsing_json_string(player_json_string)    
    print(f"player data: {data}")    
    
    # Retrieving data from filename
    state_data = get_json_from_file(filename)
    for state in state_data:
        print(f'state: {state["state"]} with Capital: {state["capital"]}')
        
    # Retrieving data from filename
    tournament_data = get_json_from_file(filename3)
    print(tournament_data["tournament"]) # tournament's name
    print(tournament_data["players"][2]) # third player's data
    
    # parsing data dictionary as a json strings
    parsed_data = transform_in_jsonString(data)
    print(parsed_data)
    
    # Saving person dictionary to a file
    data_saved = save_json_to_file(person_dict, "./output/person_data.json")
    print(f"data is saved in 'person.json' file: {data_saved}")    

# Running the Driver function
if __name__ == "__main__":
    main()