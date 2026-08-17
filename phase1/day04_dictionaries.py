

video = {

    "title" : "How to use Claude Code",
    "views" : 1500,
    "published" : True
}

print(video["title"])
print(video["views"])

#---------

def analyze_video(title):
    return {
        "title" :title,
        "word_count": len(title.split()),
        "char_count" : len(title)

    }

output = analyze_video("Learn n8n on AWA Chammel")
print(output)


#------------

def analyze_video(title):
    return {
        "title" :title,
        "word_count": len(title.split()),
        "char_count" : len(title),
        "is_title_long":  len(title.split())>4,
    }

output = analyze_video("Learn n8n on AWA Chammel")
print(output)

#-------------------

#loop

def analyze_video(video):
        return {
        "title" :video,
        "word_count": len(video.split()),
        "char_count" : len(video),
        "is_title_long":  len(video.split())>4,
    }

video = [
    "Learn n8n on AWA Channel",
    "Python for Ai Automation Guide for Biginners",
    "Claude Code Tuitorial"
]

for item in video:
     output = analyze_video(item)
     print(output)
   

