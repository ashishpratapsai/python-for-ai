def analyze_videos(videos:list[dict])-> dict:
    if not videos:
        return{}

    # find best video by views
    best_video = max(videos, key=lambda v: v["views"])

    #Calculate average
    total_views =sum(v["views"] for v in videos)
    total_likes =sum(v["likes"] for v in videos)
    avg_views = total_views/len(videos)
    avg_likes = total_likes/len(videos)

    return {
        "total_videos": len(videos),
        "total_views": total_views,
        "total_likes": total_likes,
        "avg_views": round(avg_views,2),
        "avg_likes": round(avg_likes,2),
        "best_video_title": best_video["title"],
        "best_video_views": best_video["views"],
        "best_video_id": best_video["video_id"]
        

    }

if __name__ == "__main__":
    from fetcher import get_video_stats, get_latest_videos
    videos = get_latest_videos()
    video_ids =[v["video_id"] for v in videos]
    stats = get_video_stats(video_ids)
    analysis = analyze_videos(stats)
    print(analysis)
   