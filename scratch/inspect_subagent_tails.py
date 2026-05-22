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

for idx, conv_id in subagents.items():
    transcript_path = os.path.join(brain_dir, conv_id, ".system_generated", "logs", "transcript.jsonl")
    print(f"\n==========================================")
    print(f"Index {idx} ({conv_id})")
    print(f"==========================================")
    if not os.path.exists(transcript_path):
        print("Transcript path does not exist!")
        continue
    
    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("Transcript is empty.")
            continue
        
        print(f"Total steps: {len(lines)}")
        # Let's print the last 3-4 steps' summary or tool_calls
        for i in range(max(0, len(lines)-5), len(lines)):
            step = json.loads(lines[i].strip())
            step_idx = step.get("step_index")
            step_type = step.get("type")
            status = step.get("status")
            print(f"  Step {step_idx}: Type={step_type}, Status={status}")
            if "tool_calls" in step and step["tool_calls"]:
                for tc in step["tool_calls"]:
                    tc_name = tc.get("name")
                    print(f"    Tool: {tc_name}")
            # If it's model output, show a snippet
            if step_type == "MODEL" or step_type == "PLANNER_RESPONSE":
                content = step.get("content", "")
                if content:
                    excerpt = content[:200].replace('\n', ' ')
                    print(f"    Content: {excerpt}...")
    except Exception as e:
        print(f"Error reading transcript: {e}")
