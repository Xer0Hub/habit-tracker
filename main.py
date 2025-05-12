from http.client import responses

import requests
import datetime

#CONSTANTS
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
GRAPH_ID = "YOUR GRAPH"

#VARIABLES
today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%Y%m%d")
change_date = "MODIFIED DATE"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "EXAMPLE",
    "unit": "Hours",
    "type": "int",
    "color": "shibafu"
}

pixel_data = {
    "date": formatted_date,
    "quantity": "1"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#------------------POST METHOD
# pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# post_pixel = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
# print(post_pixel.text)


#------------------PUT METHOD
# new_pixel_data = {
#     "quantity": "1",
# }
#
# update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{change_date}"
#
# response = requests.put(url=update_pixel, json= new_pixel_data, headers=headers)
# print(response.text)

#------------------DEL METHOD
# delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
# response = requests.delete(url=delete_pixel, headers=headers)
# print(response.text)

"""Look here for further documentation to customize the tracker for you https://pixe.la/"""