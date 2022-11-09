import requests
import datetime
import os

TOKEN = os.environ.get("TOKEN")
USERNAME = "jamjam1990"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphs_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "days",
    "type": "int",
    "color": "sora",
}

# headers = {
#     "X-USER-TOKEN": TOKEN,
# }

# graph_response = requests.post(url=graph_endpoint, json=graphs_params, headers=headers)
# print(graph_response.text)

# Posting a value to the graph

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
current = datetime.datetime.now()

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_post_params = {
    "date": current.strftime("%Y%m%d"),
    "quantity": "1",

}

print(current)
print(current.strftime("%Y%m%d"))

# pixel_post_response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)
# print(pixel_post_response.text)
