import os
import json

subagents = {
    "4": "840df1a5-2c8b-491a-858f-864820fa61da",
    "5": "53a695f6-b485-472e-9886-33259686869e",
    "6": "87445270-8434-4c44-b968-59270a3ce668",
    "7": "0bd25f45-5ddf-41a8-bab7-17e537e76ef5",
    "8": "a357dfae-8802-4094-a697-24e4c9db214c",
    "9": "9089e309-0a44-46c2-a9a9-d716e34aa810",
    "10": "fd405405-f402-4981-94db-2fcc041c8920",
    "11": "ccc3d010-6828-4c7f-a2aa-091c8d4aaed1",
    "12": "94a1187c-a8ad-41cd-aaac-470cefaade22",
    "13": "c0a02bc3-b974-40e1-887e-555970cacdbe"
}

brain_dir = "/Users/aaronnguyen/.gemini/antigravity/brain"

print("Checking subagents progress:")
print("----------------------------")
for idx, conv_id in subagents.items():
    transcript_path = os.path.join(brain_dir, conv_id, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(transcript_path):
        print(f"Index {idx} ({conv_id}): Transcript path does not exist!")
        continue
    
    # Read the last few lines of the transcript to see the latest step/message
    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print(f"Index {idx} ({conv_id}): Transcript is empty.")
            continue
        
        # Look for the last non-empty line
        last_line = lines[-1].strip()
        last_step = json.loads(last_line)
        
        # Let's also look for messages sent or tools executed
        step_type = last_step.get("type", "unknown")
        status = last_step.get("status", "unknown")
        print(f"Index {idx} ({conv_id}): Step {last_step.get('step_index')}, Type: {step_type}, Status: {status}")
        # Print a small excerpt if it has text content
        if "content" in last_step and last_step["content"]:
            content = last_step["content"]
            excerpt = content[:150].replace('\n', ' ')
            print(f"  -> Excerpt: {excerpt}...")
    except Exception as e:
        print(f"Index {idx} ({conv_id}): Error reading transcript: {e}")
