videos = ["Claude Code", "n8n Tutorial", "Python Basics"]

videos.append("LangChain Guide")  # add to end
videos.remove("Python Basics")    # remove by value
videos.pop()                      # remove last item
videos.sort()                     # sort alphabetically
len(videos)                       # count items
videos[0]                         # first item
videos[-1]                        # last item
videos[1:3]                       # slice — items 1 and 2

# Practice

videos = [
    "Claude Code Tutorial",
    "n8n",
    "Python for AI Automation Beginners Guide",
    "LangChain",
    "How to Build AI Agents with Python",
    "Loops"
]

def filter_video(videos):
    filtered = [video for video in videos if len(video.split())>3]
    filtered.sort()
    return filtered



print(filter_video(videos))

#--------------------------
#Now practicing cleaning the data 

# extention-1 using strip to cleaning the data

videos = [
    "  Claude Code Tutorial  ",
    "n8n  ",
    "  Python for AI Automation Beginners Guide",
]

def filter_video(videos):
    filtered = [video for video in videos if len(video.split())>3]
    filtered = [ video.strip() for video in filtered ]
    filtered.sort()
    return filtered

print(filter_video(videos))


#--------------------------

videos = [
    "Claude Code Tutorial",
    "n8n",
    "Python for AI Automation Beginners Guide",
    "LangChain",
    "How to Build AI Agents with Python",
    "Loops"
]

def video_stata(videos):
    longest_count = 0
    smallest_count = 1000
    for video in videos:
        word_count = len(video.split())
        if word_count>longest_count:
            longest_count = word_count
            longest = video
        if word_count<smallest_count:
            smallest_count = word_count
            smallest = video

    return {
        "total" : len(videos),
        "longest_video": longest,
        "smallest_video": smallest
    }

print(video_stata(videos))