import re
import os

def patch_view(filename, model_val, combo_num):
    path = f"clone truyen app/src/components/{filename}"
    with open(path, "r") as f:
        content = f.read()

    # Pass model parameter into agentConceptGenerator and agentConceptScorer
    pattern1 = r"(agentConceptGenerator\('[^']+', [^,]+, )(criteria\))"
    content = re.sub(pattern1, rf"\1'{model_val}', \2", content)

    pattern2 = r"(agentConceptScorer\('[^']+', [^,]+, )(concepts\))"
    content = re.sub(pattern2, rf"\1'{model_val}', \2", content)
    
    # Add comboType explicitly when pushing QueueItem
    # Find "isAdvancedPipeline: true," and append comboType
    if "comboType:" not in content:
        content = content.replace("isAdvancedPipeline: true,", f"isAdvancedPipeline: true, comboType: {combo_num},")

    with open(path, "w") as f:
        f.write(content)

patch_view("ComboEconomicView.tsx", "gemini-1.5-flash", 5)
patch_view("ComboRoyalView.tsx", "gpt-4o-mini", 6)
