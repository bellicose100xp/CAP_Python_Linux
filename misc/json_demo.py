from pprint import pprint
import json
import yaml

spidey = {
    "name": "Spiderman",
    "money": None,
    "powers": ["web slinging", "wall crawling"],
    "alive": True,
}

json_string = json.dumps(spidey)
pprint(json_string)

with open("marvel.yaml", "w", encoding="utf-8") as file:
    yaml.dump(spidey, file)
