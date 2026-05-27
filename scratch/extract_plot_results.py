import json

def main():
    with open("plot_analysis_results.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    print("Setting Distribution:")
    for k, v in data["setting_distribution"].items():
        print(f"  {k}: {v}")
        
    print("\nTheme Distribution:")
    for k, v in data["theme_distribution"].items():
        print(f"  {k}: {v}")
        
    print("\nSample Stories and Extracted Capitalized Name Sequences:")
    for idx, story in enumerate(data["stories"][:15]):
        print(f"\n{idx+1}. [{story['theme']}] {story['title']}")
        print(f"   Setting: {story['setting']}")
        print(f"   Names detected: {', '.join(story['extracted_names'])}")

if __name__ == "__main__":
    main()
