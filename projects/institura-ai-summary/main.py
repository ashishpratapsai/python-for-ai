# Imports needed:
from data import load_students
from generator import generate_summaries,get_results
from reporter import save_report
import time
import logging
import anthropic

# Setup logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    # Load student
   students =load_students("students.csv")
   if not students:
      logger.error("No student loaded. Check student.csv")
      return
   logger.info(f"Loaded {len(students)} students")

   # Generate Batch
   try:
        print("\nSubmitting batch to Anthropic...")
        batch_id = generate_summaries(students)
        logger.info(f"Batch created: {batch_id}")
        print("Save this Id - you ca check results later")

   except anthropic.AuthenticationError:
            logger.error("Invalid API key. check .env file.")
            return
   except anthropic.APIConnectionError:
        logger.error("Cannot connect to Anthropic API.")
        return
   except Exception as e:
        logger.error(f"Batch creation failed: {e}")
        return
        
   
    # Save batch_id to file for later
   with open("batch_id.txt", "w") as f:
        f.write(batch_id)

   print(f"\nBatch submitted successfully.")
   print(f"Wait 5 minutes then run:")
   print(f"  python3 main.py --check")


def check_batch():
   # Read saved batch_id
   from pathlib import Path

   if not Path("batch_id.txt").exists():
        print("No batch found, Run 'python3 main.py' first.")
        return

   with open("batch_id.txt","r") as f:
        batch_id = f.read().strip()

   print(f"Checking batch: {batch_id}")
   results = get_results(batch_id)

   if results is None:
        print("still processing.Try again in few minutes")
        return

    # save report
    
   save_report(results)
   #summary
   print(f"\n=== DONE ===")
   print(f"Students processed: {len(results)}")
   print(f"Report saved to: summaries.md")


if __name__ == "__main__":
    import sys
    if len(sys.argv)>1 and sys.argv[1] == "--check":
         check_batch()
    else:
        main()

        