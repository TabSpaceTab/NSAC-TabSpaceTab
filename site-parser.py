import json     

contaminated_list = []
req_counter = 0

with open('Json/contaminated-data.json') as f:
    for jsonObj in f:
        cont_dict = json.loads(jsonObj)
        contaminated_list.append(cont_dict)


user = string(input("Enter the site:"))

for cont in contaminated_list:
    req_counter += 1
    if cont["site"] == user:
        return(list[count - 1])
        #print(list[count - 1])
        