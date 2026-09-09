import httpx

# import json

# response = httpx.get("https://jsonplaceholder.typicode.com/users/1")
# data = response.json()
# print(json.dumps(data, indent=2))



response = httpx.get("https://jsonplaceholder.typicode.com/users/1")



print(f"Status: {response.status_code}")
print(f"Data: {response.json()}")


data =response.json()
print(data["name"])
print(data["email"])
print(data["address"]["city"])
print(data["company"]["name"])

#-----------



def get_user(user_id: int) -> dict:

    response = httpx.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
   
    if response.status_code != 200:
        return {"error": f"Failed with status {response.status_code}"}

    data = response.json()
    return {
        "name": data["name"],
        "email": data["email"],
        "city" : data["address"]["city"],
        "company": data["company"]["name"]
    }

print(get_user(1))
print(get_user(999))

#---------
#now getting 10 users data

def get_all_user() ->list[dict]:
    users=[]
   

   
    response = httpx.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    user_count  = len(data)

    if response.status_code != 200:
            return []
    

    for item in data:
        users.append({
                "name": item["name"],
                "email": item["email"],
                "city" : item["address"]["city"],
                "company": item["company"]["name"]
        })

    return users



print(get_all_user())
print(len(get_all_user()))
#-----------

# for better error handling

def get_user(user_id: int) -> dict:

    try:
        response = httpx.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    except httpx.connectError:
         return{"error : could not connect to API"}
    
    
    
    
   
    if response.status_code != 200:
        return {"error": f"Failed with status {response.status_code}"}

    data = response.json()
    return {
        "name": data["name"],
        "email": data["email"],
        "city" : data["address"]["city"],
        "company": data["company"]["name"]
    }

print(get_user(1))
print(get_user(999))



    
