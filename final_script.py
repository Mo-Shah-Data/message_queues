import json
import re

pattern = re.compile(r'(\{.*?\})')

messages = {}

with open('MOCK_DATA_same.json', 'r') as file:
    for line in file:
        # Find all matches in the current line
        matches = pattern.findall(line)

        for match in matches:
            match = match.strip()
            #print(match)

            match_formatted = json.loads(match)

            if match_formatted['id'] in messages:
                # get id number from new_message
                match_id = match_formatted['id']
                #print("id in messages dict")
                # check all other key value pairs currently in dict item in messages
                for k, v in messages[match_id].items():
                    # print(k,v)
                    if match_formatted[k] == messages[match_id][k]:
                        if k == 'id': # convert to list of keys to look at
                            continue
                        match_formatted[k] = 'null'
            #else:
                # print("not in dict")

            messages[match_formatted['id']] = match_formatted

# Create output which is a list - output each line to list
# if an intial value, omit it as it can't be evaluated
