#CS2705
#pinging assignment
#Jared Anderson

import subprocess

print("Begin DNS Search Processes\n")
#1
print("nslookup for weber.edu")
subprocess.call(["nslookup", "www.weber.edu"])
print("")

print("dig for weber.edu using different DNS server")
subprocess.call(["dig", "@1.1.1.1", "www.weber.edu"])
print("")

print("NS server using host for weber.edu")
subprocess.call(["host", "-t", "NS", "www.weber.edu"])
print("")

#2
print("nslookup for deseretnews.com")
subprocess.call(["nslookup", "www.deseretnews.com"])
print("")

print("dig for deseretnews.com using different DNS server")
subprocess.call(["dig", "@1.1.1.1", "www.deseretnews.com"])
print("")

print("NS server using host for deseretnews.com")
subprocess.call(["host", "-t", "NS", "www.deseretnews.com"])
print("")

#3
print("MX server using nslookup for www.weber.edu")
subprocess.call(["nslookup", "-query=mx", "www.weber.edu"])
print("")

print("MX server using nslookup for www.gmail.com")
subprocess.call(["nslookup", "-query=mx", "www.gmail.com"])
print("")

#4
print("nslookup for yahoo.com")
subprocess.call(["nslookup", "www.yahoo.com"])
print("")

print("nslookup for microsoft.com")
subprocess.call(["nslookup", "www.microsoft.com"])
print("")

#5
print("dig for google.com using different DNS server using 8.8.8.8 server")
subprocess.call(["dig", "@8.8.8.8", "www.google.com"])
print("")

print("dig for dell.com using different DNS server using 8.8.8.8 server")
subprocess.call(["dig", "@8.8.8.8", "www.dell.com"])
print("")

print("dig for hp.com using different DNS server using 8.8.8.8 server")
subprocess.call(["dig", "@8.8.8.8", "www.hp.com"])
print("")
