import paramiko

s = paramiko.SSHClient()
key = paramiko.AutoAddPolicy()
s.set_missing_host_key_policy(key)
s.connect('192.168.3.9', 22, 'root', '2023Possible@' ,timeout=5)


stdin, stdout, stderr = s.exec_command('cd /volume1/git/hexo-blog-config && git pull')

for i in stdout.readlines():
	print(i)

for i in stderr.readlines():
	print(i)

stdin, stdout, stderr = s.exec_command('cd /volume1/git/hexo-blog-config && git push -f Github')

for i in stdout.readlines():
	print(i)

for i in stderr.readlines():
	print(i)

stdin, stdout, stderr = s.exec_command('cd /volume1/git/hexo-blog && git pull')

for i in stdout.readlines():
	print(i)

for i in stderr.readlines():
	print(i)