from extractor import read_transcript, key_moments, save_summary

def main():
    transcript = read_transcript("sample_transcript.txt")
    keywords = ["Claude Code", "AI agents", "n8n", "automation", "MCP", "Python"]
    results = []

    while True:
        print("\n===================================\n")
        print("      TRANSCRIPT EXTRACTOR   ")
        print("\n===================================\n")
        print("1. Find Key Moments")
        print("2. view key Moments")
        print("3. Save Summary to Markdown")
        print("4. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            results = key_moments(transcript, keywords)
            print(f"\n{len(results)} key moments found.")

        elif choice == "2":
            if not results:
                print("No moments yet. Run Option 1 first")
            else:
                for i, moment in enumerate(results, 1):
                    print(f"{i}.{moment}")
           

        elif choice == "3":
            choice = save_summary(results,keywords,"transcript_summary.md")
            print("Summary saved to transcript_summary.md")
        elif choice =="4":
            print("Good bye")
            break
        else:
            print("Invalid Code. Pleaseenter 1-4")

main()



    

