import requests

TOKEN = "fluent98765"
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

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_response = requests.post(url=graph_endpoint, json=graphs_params, headers=headers)
print(graph_response.text)
