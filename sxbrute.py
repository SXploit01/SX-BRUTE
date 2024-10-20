#!/usr/bin/env python3

Tool_Name = "SX-BRUTE"
Version = "1.0"
"""
Author: SXploit
GitHub: https://github.com/SXploit01
"""

from zipfile import ZipFile
import sys
import time
import argparse
import os

os.system("clear")

parser = argparse.ArgumentParser(description="A tool for cracking passwords of encrypted ZIP files using a provided wordlist.")
parser.add_argument("-z", "--zipfile", type=str, help="Specify the ZIP file.")
parser.add_argument("-w", "--wordlist", type=str, help="Specify the password list.")
parser.add_argument("-o", "--output", default="Extract", help="Directory to extract the contents of the ZIP file if the password is found (default: Extract).")
parser.add_argument("--version", action="version", version="{} {}".format(Tool_Name, Version))

args = parser.parse_args()

def banner():
    
    print("""\033[0;91m
_____________________________________________________ 
   ______  __      ____  ____  __  ______________   |
  / ___/ |/ /     / __ )/ __ \/ / / /_  __/ ____/   |
  \__ \|   /_____/ __  / /_/ / / / / / / / __/      |
 ___/ /   /_____/ /_/ / _, _/ /_/ / / / / /___      |
/____/_/|_|    /_____/_/ |_|\____/ /_/ /_____/      |
       Created by SXploit x Kallinux                |
                  DCT37 TEAM.                       |
    Fungsi: Crack Brute PW (Gk semua bisa)          |                                 
____________________________________________________|             
\033[0m""")



if (bool(args.zipfile) == True):
	action = args.zipfile
	try:
		zip = ZipFile(action, "r")
	except Exception as error:
		print("\n\033[0;91m[ERROR] {}\033[0;0m\n".format(error))


elif (bool(args.zipfile) == False):
	banner()
	while(True):
		action=input("Masukkan File Zip (Contoh : /sdcard/file.zip) : ")
		if(action=="quit" or action=="exit"):
			sys.exit()
		else:
			pass
		try:
			zip = ZipFile(action,"r")
			break

		except:
			if(action==""):
				pass
			else:
				print("\n\033[0;91m[ERROR FILE] Tidak dapat menemukan file zip.\033[0;0m\n")

else:
	pass


if(bool(args.wordlist) == True):
	list = args.wordlist
	try:
		wordlist = open(list, "r", encoding="utf-8", errors="replace")

	except Exception as error:
		print("\n\033[0;91m[ERROR] {}\033[0;0m\n".format(error))

elif(bool(args.wordlist) == False):
	while(True):
		list=input("Masukkan File Text/Word List(Contoh : /sdcard/sxpass.txt) : ")
		if(list=="quit" or list=="exit"):
			sys.exit()
		try:
			wordlist = open(list,"r")
			break
		except:
			if(list == ""):
				pass
			else:
				print("\n\033[0;91m[ERROR FILE] Tidak dapat menemukan File Password.\033[0;0m\n")

else:
	pass
	

	
print("\n")

condition=0
attempts = 0
start = time.time()
for password in wordlist:
	password = password.strip()
	sys.stdout.write("\r\033[K")
	sys.stdout.write("\r[!] Sedang Mencoba Password : {}".format(password))
	sys.stdout.flush()
	try:
		zip.extractall(path=args.output,pwd=password.encode("utf-8"))
		print("\n\n\033[1;92m[✓] Password Ditemukan !: {}\033[0;0m".format(password))
		timestamp = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
		file_name = "{}.txt".format(timestamp)
		with open(file_name,"w") as pass_file:
			pass_file.write(password)
			print("\nPassword disimpan di {}.".format(file_name))
			
		condition+=1
		break
	except:
		pass
	attempts +=1

zip.close()
wordlist.close()

if(condition==0):
	print("\n[?] Tidak ditemukan Password yang Valid.")
else:
	pass

elapsed = time.time() - start
elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))

print("Waktu yang dibutuhkan: {}".format(elapsed_time))
print("Mencoba Total {} Password.".format(attempts))
