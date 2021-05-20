import random
import subprocess

wordlist = list()
with open('keimport zipfile
from tqdm import tqdm

wordlist = "keywords.txt"
zip_file = "username.zip"

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
ywords.txt') as f:
    for line in f:
        wordlist.append(line.rstrip('\n'))
        password = line.rstrip('\n')
        subprocess.call(["7z", "x", "-y", "-p "+password, "username.zip"])
