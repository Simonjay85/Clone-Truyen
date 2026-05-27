import os
import signal
import re

current_pid = os.getpid()
print(f"My PID is {current_pid}")

# Get all running python processes
try:
    ps_output = os.popen("ps aux | grep batch_v13_publisher").read()
    print("Found processes:")
    print(ps_output)
    
    for line in ps_output.split("\n"):
        if "batch_v13_publisher.py" in line and "grep" not in line:
            # Extract PID (second column)
            parts = re.split(r'\s+', line.strip())
            if len(parts) > 1:
                pid = int(parts[1])
                # Cautiously avoid killing ourselves or any process that might be important
                if pid != current_pid:
                    # Double check process arguments to make sure it's an orphan
                    # We want to kill indices 14, 24, 34, 54 etc.
                    print(f"Killing orphaned publisher process with PID: {pid}")
                    try:
                        os.kill(pid, signal.SIGKILL)
                        print(f"Successfully killed PID {pid}")
                    except Exception as e:
                        print(f"Failed to kill PID {pid}: {e}")
except Exception as ex:
    print("Error parsing processes:", ex)
