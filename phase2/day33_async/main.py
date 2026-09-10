import asyncio
import httpx
import time

async def fetch_user(user_id:int)-> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"

        )

    data = response.json()
    return{
        "id": user_id,
        "name": data["name"],
        "email": data["email"]
    }

async def main():
    user = await fetch_user(1)
    print(user)

asyncio.run(main())

#------

async def fetch_multiple_user(user_ids:list[int])-> list[dict]:
    tasks =[fetch_user(user_id) for user_id in user_ids]
    results = await asyncio.gather(*tasks)
    return list(results)

async def main():
    #time the async version
    start =time.time()
    users = await fetch_multiple_user([1,2,3,4,5])
    end = time.time()

    print(f"Async:{end-start:.2f} seconds")
    for user in users:
        print(user)

asyncio.run(main())

#------------------
# LAYER 3 — Speed comparison sync vs async
#---------------------


def fetch_user_sync(user_id: int)-> dict:
    response = httpx.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    data = response.json()
    return {"id": user_id, "name": data["name"], "email": data["email"]}


# Time the sync version
start = time.time()
users_sync = [fetch_user_sync(i) for i in [1, 2, 3, 4, 5]]
end = time.time()
print(f"Sync: {end - start:.2f} seconds")