#! /usr/bin/python

import ftplib

def anonloginftp(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login("anonymos", "anonymos")
		print("[+] %s FTP anonymous logon successfully" % hostname)
		ftp.quit()
		return
	except Exception as e:
		print("[-] %s FTP logon falied " % hostname)
def main():
	host = input("Enter the IP address: ")
	anonloginftp(host)

if __name__ == "__main__":
	main()
