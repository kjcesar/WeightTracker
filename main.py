import requests
import json
from datetime import datetime


"""
A(Start) --> |User inputs weight| B{weight entered?}
B --> |Yes| C[Update weight table]
C --> D{Goal achieved?}
D --> |Yes| E[Display success message]
D --> |No| F[Display encouragement message]
F --> B
B --> |No| A
somesecretpasswordthatnobodyknows
"""
user_input = input("Enter Weight: ")
date = datetime.now().date()  # YYYY-MM-DD
sheet_name = "sheet1"
endpoint = "https://api.sheety.co/8cb79d9904cf6af742bab39893fa4d99/myWeight/sheet1"
headers = {
    "Authorization": "Bearer somesecretpasswordthatnobodyknows",
    "Content-Type": "application/json",
}

print(date)

if user_input:
    pass
    # Code to update weight
    payload = {sheet_name: {"weight": int(user_input), "date": str(date)}}
    json_payload = json.dumps(payload)
    response = requests.post(endpoint, data=json_payload, headers=headers)
    response.raise_for_status()
    print(response.status_code)
    # Code if goal is archieved
    # Code if goal is not archieved
else:
    pass
