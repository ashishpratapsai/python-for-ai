from models import Tutorial, TutorialSection
from extractor import extract_structure


def generate_tutorial(tutorial: Tutorial, output_file: str = "tutorial.md")-> None:
    with open(output_file,"w") as f:
        # write title
        f.write(f"# {tutorial.title}\n\n")

        # write introduction
        f.write(f"{tutorial.introduction}\n\n")

        #loop throug sections 
        for section in tutorial.sections:
            f.write(f"## {section.heading}\n\n")
            f.write(f"{section.content}\n\n")
            if section.code_example:
                f.write(f"```python\n{section.code_example}\n```\n")

        #key takeaways
        f.write("## Key Takeaways\n\n")
        for point in tutorial.key_takeaways:
            f.write(f"- {point}\n")

        #thumbnail prompt
        f.write(f"\n---\n**Thumbnail Prompt:** {tutorial.thumbnail_prompt}\n")