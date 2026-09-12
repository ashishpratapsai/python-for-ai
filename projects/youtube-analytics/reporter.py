from datetime import datetime

def generate_report(channel_stats: dict, video_stats: list[dict], analysis: dict, filename : str ="youtube_report.md")-> None:
    today = datetime.now().strftime("%Y-%m-%d")

    with open(filename, "w") as f:
        #Header
        f.write(f"# Youtube Analytics Report\n")
        f.write(f"**Channel:** {channel_stats["name"]}\n")
        f.write(f"**Generated:** {today}\n")

        # Channel Overview
        f.write(f"## Channel Overview\n")
        f.write(f"- Subscribers: {channel_stats['subscribers']}\n")
        f.write(f"- Total Views: {channel_stats['total_views']}\n")
        f.write(f"- Total Videos: {channel_stats['video_count']}\n")

        #Analysis
        f.write("## Latest 10 Video Analysis\n")
        f.write(f"- Average views: {analysis['avg_views']}\n")
        f.write(f"- Average Likes: {analysis['avg_likes']}\n")
        f.write(f"- Best video: {analysis['best_video_title']}\n")
        f.write(f"- Best video Views: {analysis['best_video_views']}\n")


        #Video Details
        f.write("## video Detail\n")
        f.write("| Title |  Views |  Likes |  Comments |\n")
        f.write("| ----- |  ----- |  ----- |  -------- |\n")

        for video in video_stats:
            f.write(f"| {video["title"][:40]} | {video["views"]} | {video["likes"]} | {video["comments"]} |\n")

    print(f"Report saved to {filename}")
    