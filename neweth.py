from time import sleep
import bit
import requests
from bitcoin import *
import colorama
from colorama import Fore, Back, Style
colorama.init()
import eth_keys
from eth_keys import keys
import requests
import json
import atexit
from time import time
from datetime import timedelta, datetime


def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + Fore.BLUE + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' )
    if elapsed:
        print("\n " + Fore.RED + " [TIMING]> Elapsed time ==> " + elapsed + "\n" )


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")


print(Fore.GREEN + "Start search... Pick Range 128 Above you starting range or it will not work")
x=int(input(Fore.YELLOW +"'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")

query = []
F = []
P = x
count=0
total=0
pagenumber=0
while P<y:
    P+=1
    ran = P
    myhex = "%064x" % ran
    private_key = myhex[:64]
    private_key_bytes = bytes.fromhex(private_key)
    public_key_hex = keys.PrivateKey(private_key_bytes).public_key
    public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
    ethadd = keys.PublicKey(public_key_bytes).to_address()	
    count+=1
    total+=128 
    seed=str(ran)
    pagenumber= int(seed)//128
    if len(query) == 128:
        
        try:
            blocs = requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd + "?apiKey=EK-gT2va-7M2tojY-Lsydy") #Ethereum API Must create account to be better API
            ress = blocs.json()
            balances = dict(ress)["countTxs"]
            print(Fore.RED + '\nPrivateKey (hex) Last One in Scan : ' + Fore.YELLOW + key.to_hex() + Fore.RED + ' : PrivateKey (hex) Last One in Scan' + Style.RESET_ALL)
            print(Fore.RED + '\nPrivateKey (dec) Last One in Scan : ' + Fore.YELLOW + seed + Fore.RED + ' : PrivateKey (dec) Last One in Scan' + Style.RESET_ALL)
            print(Fore.RED + '\n WARNING !!!!  Any Winners found will be Within 128 Private Key range of this Scan !!!! WARNING !!!!'+ Style.RESET_ALL)
            print ('\n-- keys.py -- ' + Fore.GREEN +  'Running Scan : ' + str (count) + '  :  ' + Fore.BLUE + 'Total Ethereum Addresses : ' + str (total) + ' : ' + Fore.YELLOW + seconds_to_str() + '] ----> '   + Style.RESET_ALL)

            #Parse results
            for row in request["addresses"]:
                print(row)
                print(Fore.GREEN +  '<--------------------------------Page Number ' , Fore.YELLOW , pagenumber , Fore.GREEN , ' on Keys--------------------------------> '+ Style.RESET_ALL)
                if row(balances) > 0:
                    print(Fore.GREEN + "\nMatching Key ==== Found!!!\n PrivateKey: " + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
                    print(Fore.GREEN + "\nMatching Key ==== Found!!!\n Page Number: " + Fore.YELLOW , pagenumber , Style.RESET_ALL)
                    f=open(u"winner.txt","a")
                    f.write('\nPrivateKey (hex): ' + myhex)
                    f.write('\n Eth Address: ' + ethadd)
                    f.write('\n==================================')
                    f.close()
                    print('\a')
                    break
        except:
            pass

        # Reset counter
        query = []
        sleep(1) 
