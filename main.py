import requests, os
from datetime import datetime

USERNAME = os.environ.get("USERNAME") #create username for user
TOKEN=os.environ.get("TOKEN") # create identification token
GRAPH_ID= "graph1" # name of graph

pixela_endpoint="https://pixe.la/v1/users"

# user parameters
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# POST
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# graph endpoint
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
update_graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
graph_config={
    "id":GRAPH_ID,
    "name":"Running Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu",
}

# Identification Token, serves as password
headers = {
    "X-USER-TOKEN":TOKEN,
}

# create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


add_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

add_pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many km did you run today?"),
}

# create pixel
response=requests.post(url=add_pixel_endpoint,json=add_pixel_config,headers=headers)
print(response.text)

#update pixel
update_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_pixel_data={
    "quantity":"21.1",
}

# response=requests.put(url=update_pixel_endpoint,json=update_pixel_data,headers=headers)
# print(response.text)

#delete a pixel
delete_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response=requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)