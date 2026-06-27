

video = {
    "title": "how to use claude Code",
    "stats" : {
        "views": 1500,
        "likes" : 230,
        "comments": 45
    },
    "channel" : {
        "name":"Automate With Ashish",
        "subscribers": 5000
    }
}

status = print(video["stats"]["likes"])

#--------------

def get_video_stats(video):
    return {
        "title": video["title"],
        "likes": video["stats"]["likes"],
        "subscribers": video["channel"]["subscribers"]


    }

video = {
    "title": "how to use claude Code",
    "stats" : {
        "views": 1500200,
        "likes" : 23022,
        "comments": 452
    },
    "channel" : {
        "name":"Automate With Ashish",
        "subscribers": 5000
    }
}

output = get_video_stats(video)
print(output)



