def read_transcript(filepath):
    with open(filepath,"r")  as  file:
        lines = file.readlines()
        
    return [line.strip() for line in lines if line.strip()]


# transcript = read_transcript("sample_transcript.txt")


# print(read_transcript("sample_transcript.txt"))

# keywords = ["agent", "tool calling", "MCP", "Claude Code"]

# function to extract sentences which contain the keywords

def key_moments(transcript, keywords):
    results = []
    for sentense in transcript:
        if any(keyword.lower() in sentense.lower() for keyword in keywords):
            results.append(sentense)
    return results

# results = key_moments(transcript, keywords)
# for result in results:
#     print(result)


#writing the summary file

def save_summary(results, keywords, output_file):
    with open(output_file ,"w") as file:
      file.write("# Transcript Summary\n")
      file.write(f"## keywords: {', '.join(keywords)} \n")
      file.write(f"## key Moments: ({len(results)} found ) \n")
      for sentence in results:
          file.write(f"- {sentence}\n")
                
# save =save_summary(results,keywords,"transcript_summary.md")



if __name__ == "__main__":
    transcript = read_transcript("sample_transcript.txt")
    keywords = ["Claude Code", "AI agents", "n8n", "automation", "MCP", "Python"]
    results = key_moments(transcript, keywords)
    for result in results:
        print(result)
    save_summary(results, keywords, "transcript_summary.md")  



