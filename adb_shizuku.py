import subprocess
import time


def run_command(command):
  result = subprocess.run(command, shell=True, capture_output=True, text=True)
  return result.returncode, result.stdout, result.stderr


print("Checking connected devices...")
time.sleep(1)
command = 'adb devices'
return_code, stdout, stderr = run_command(command)
print(stdout)
print(stderr)

if return_code != 0:
  print(
      f"ADB command failed. Please check device connection and ADB installation. Command '{command}' Error level: {return_code}")
else:
  print("Device check complete, allow USB debugging on your device...")
  time.sleep(1)
  print("Starting shell command...")

  process = subprocess.run(['adb', 'shell', 'sh', '/storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh'],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
  return_code = process.returncode
  print(process.stdout)

  if return_code != 0:
    print(
        f"Shell command execution failed, error level: {return_code}. Check the info! ")
  else:
    print("Shell command executed successfully.")

input("Press Enter to continue...")
