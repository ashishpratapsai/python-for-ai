from fetcher import get_channel_stats, get_latest_videos,get_video_stats
from analyzer import analyze_videos
from reporter import generate_report

def main():
    print("Fetching channel stats...")
    channel_stats = get_channel_stats()

    print("Fetching latest video...")
    videos = get_latest_videos()
    video_ids = [v["video_id"] for v in videos]

    print("Fetching video stats...")
    video_stats = get_video_stats(video_ids)

    print("Analyzing...")
    analysis = analyze_videos(video_stats)

    print("Generating Report...")
    generate_report(channel_stats,video_stats,analysis)

    print("\n=== SUMMARY ===")
    print(f"Channel : {channel_stats["name"]}")
    print(f"Subscribers : {channel_stats["subscribers"]}")
    print(f"Best Video : {analysis["best_video_title"]}")
    print(f"Best Video Views : {analysis["best_video_views"]}")


if __name__ =="__main__":
    main()
