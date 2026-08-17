

def add_number(a,b):
    return a+b

print(add_number(2,4))


def check_views(views):
    if views <1000:
        return "starting"
    elif views >1000 and views<10000:
        return "growing"
    elif views > 10000:
        return "viral"

print(check_views(50000))
print(check_views(5000))
print(check_views(500))


#----------------

channels = ["AWA Channel", "MrBeast", "Fireship", "NetworkChuck"]


for index, item in enumerate(channels, 1):
    print(f"{index}.{item}")

#----------

channel = {
    "name": "AWA Channel",
    "subscribers": 5000,
    "stats": {
        "total_videos": 45,
        "total_views": 120000
    }
}

def channel_summary(channel):
    return {
        "name": channel["name"],
        "subscribers": channel["subscribers"],
        "total_videos": channel["stats"]["total_videos"],
        "average_views": channel["stats"]["total_views"]/channel["stats"]["total_videos"]
    }

print(channel_summary(channel))