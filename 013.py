import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.0.254.158", port=22, username="root", password="Eaj2018!@#$%^")
stdin,stdout,stderr = ssh.exec_command("df")
result = stdout.read().decode()
err = stderr.read()
ssh.close()
print(stdin, result, err)