from extractor import extract_structure
from generator import generate_tutorial
import anthropic

def main():
    # Read transcript
    with open("sample_transcript.txt","r") as f:
        transcript = f.read()

    print("Extracting Structure...")
    try:
        tutorial = extract_structure(transcript)
    except anthropic.APIConnectionError:
        print("Cannot connect to Anthropic API. Check your internet")
        return
    except anthropic.AuthenticationError:
        print("Invalid APi key. Check your .env file")
        return
    except Exception as e:
        print("Exreaction Failed: {e}")
        return

    print(f"Title: {tutorial.title}")
    print(f"Section: {len(tutorial.sections)}")

    print("\nGenerating Tutorial..")
    generate_tutorial(tutorial)
    print("Done! Check tutorial.md")

if __name__ =="__main__":
    main()