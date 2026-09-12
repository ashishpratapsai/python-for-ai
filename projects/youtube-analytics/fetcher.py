import os
import httpx
import json
import html
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")
BASE_URL = "https://www.googleapis.com/youtube/v3"



def get_channel_stats()-> dict:
    response = httpx.get(
        f"{BASE_URL}/channels",
        params={
            "part": "snippet,statistics",
            "id": CHANNEL_ID,
            "key": API_KEY
        }
    )

    #print(json.dumps(response.json(), indent=2))

    if response.status_code != 200:
        return {"error": f"Failed : {response.status_code}"}

    
    data =response.json()
    channel =data["items"][0]
    stats = channel["statistics"]
    snippet = channel["snippet"]

    return{
        "name": snippet["title"],
        "description": snippet["description"][:100],
        "subscribers": int(stats.get("subscriberCount", 0)),
        "total_views": int(stats.get("viewCount", 0)),
        "video_count": int(stats.get("videoCount", 0))
    }

def get_latest_videos(max_results: int =10)-> list[dict]:
    response = httpx.get(
        f"{BASE_URL}/search",
        params={
            "part": "snippet",
            "channelId": CHANNEL_ID,
            "maxResults": 10,
            "order": "date",
            "type": "video",
            "key": API_KEY
        }
    )
    videos =[]
    data =response.json()
    for item in data["items"]:
        videos.append({
            "video_id": item["id"]["videoId"],
            "title": html.unescape(item["snippet"]["title"]),
            "published_at": item["snippet"]["publishedAt"][:10]

        })
        # print(f"Status: {response.status_code}")
        # print(json.dumps(response.json(), indent=2))
    return videos


# if __name__ == "__main__":
#     stats = get_channel_stats()
#     print(stats)

#     videos = get_latest_videos()
#     print(videos)



#------------

# getting videos data

def get_video_stats(video_ids: list[str])->list[dict]:
    ids_string = ",".join(video_ids) #join list into comma- seprated string

    response = httpx.get(
        f"{BASE_URL}/videos",
        params={
            "part":"snippet,statistics",
            "id": ids_string,
            "key": API_KEY

        }
    )

    if response.status_code !=200:
        return[]

    data = response.json()
    video =[]
    for item in data['items']:
        snippet = item.get("snippet",{})
        stats = item.get("statistics",{})
        video.append({
            "video_id": item["id"],
            "title": html.unescape(snippet.get("title","Unknown")),
            "views": int(stats.get("viewCount",0)),
            "likes": int(stats.get("likeCount",0)),
            "comments": int(stats.get("commentCount",0))

        })
    return video


#-----------
if __name__ == "__main__":
    videos = get_latest_videos()
    video_ids =[v["video_id"] for v in videos]
    stats = get_video_stats(video_ids)
    for s in stats:
        print(s)



