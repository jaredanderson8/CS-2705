#CS2705
#pinging assignment
#Jared Anderson

import subprocess

print("Begin pinging\n")
print("Pinging www.microsoft.com with the Mac and Linux...")
subprocess.call(["ping", "-c 4", "www.microsoft.com"])
print("")

print("Pinging www.weber.edu with the Mac and Linux...")
subprocess.call(["ping", "-c 4", "www.weber.edu"])
print("")

print("Pinging www.yahoo.com with the Mac and Linux...")
subprocess.call(["ping", "-c 4", "www.yahoo.com"])
print("")

print("Pinging www.nhl.com with the Mac and Linux...")
subprocess.call(["ping", "-c 4", "www.nhl.com"])
print("")

print("Pinging www.ksl.com with the Mac and Linux...")
subprocess.call(["ping", "-c 4", "www.ksl.com"])