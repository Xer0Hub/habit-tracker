import requests

#CONSTANTS
USERNAME = "xer0"
TOKEN = "djaskflj2r32fjsdklf3"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graph"
graph_config = {
    "id": "id1",
    "name": "my_first_graph",
    "unit": "hours",
    "type": 
    "color":

}

requests.post()

