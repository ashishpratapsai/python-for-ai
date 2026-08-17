videos = [{
    "title" : "let's learn n8n together",
    "views" : 3000,
    "likes" : 5000,
    "meta" :{
        "word_count": 50,
        "duration_min": 5
    }
    },
    {
        "title" : "I want to create videos ",
    "views" : 4000,
    "likes" : 6000,
    "meta" :{
        "word_count": 60,
        "duration_min": 10
    }

    },
    {
        "title" : "claude code is best place to code",
    "views" : 5000,
    "likes" : 7000,
    "meta" :{
        "word_count": 70,
        "duration_min": 20
    }   
    }

]


def analyse_channel(videos):
    total_views = 0
    total_likes = 0
    longest_title =""
    longest_count = 0
    for video in videos:
        total_views = total_views + video["views"]
        total_likes = total_likes + video["likes"]
        title = video["title"]
        word_count = len(title.split())
        if word_count>longest_count:
            longest_count = word_count
            longest_title = title
    return {
        "longest_title" : longest_title,
        "longest_count": longest_count,
        "total_views": total_views,
        "total_likes": total_likes,
        "video_count": len(videos)  

    }

print(analyse_channel(videos))