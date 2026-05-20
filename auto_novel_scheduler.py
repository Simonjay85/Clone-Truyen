import time
import subprocess
import os
import sys

print("=" * 60)
print("🤖 AUTOMATED NOVEL PUBLISHER DAEMON IS RUNNING...")
print("📍 This daemon will automatically trigger a new full novel generation")
print("📍 every 4 hours (14400 seconds) in the background.")
print("=" * 60)

# Define interval (4 hours)
INTERVAL = 4 * 60 * 60 

def trigger_generation():
    print(f"\n⏰ [{time.strftime('%Y-%m-%d %H:%M:%S')}] Triggering new novel generation...")
    try:
        # Run auto_novel_generator.py and redirect output to a log file
        log_file = f"scheduler_run_{time.strftime('%Y%m%d_%H%M%S')}.log"
        with open(log_file, "w") as f:
            subprocess.run([sys.executable, "auto_novel_generator.py"], stdout=f, stderr=subprocess.STDOUT, check=True)
        print(f"✓ Novel generation completed successfully! Logs saved to {log_file}")
    except Exception as e:
        print(f"❌ Error during novel generation: {e}")

# Run immediately on start
trigger_generation()

# Loop forever
while True:
    print(f"\n💤 Sleeping for 4 hours... Next generation at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + INTERVAL))}")
    time.sleep(INTERVAL)
    trigger_generation()
