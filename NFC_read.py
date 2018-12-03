
import binascii
import sys
import time
import PN532
import subprocess

global CardState
global CardID
global cardNum
global tagListe

def debug_print(message):
    #print(message)
    pass

#Create an instance of the PN532 class
pn532 = PN532.PN532("/dev/ttyAMA0", 115200)

#Initialize communiction with PN532
pn532.begin()

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

# Get the firmware version from the chip and print(it out.)
ic, ver, rev, support = pn532.get_firmware_version()
debug_print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
#print('Waiting for MiFare card...')

CardState = "none"
cardNum = 0
tagListe = [0, 0, 0, 0]

taglistFile = open("input_badge.txt", "w")
taglistFile.write("")
taglistFile.close()


while cardNum < 4:
    global CardState
    # Check if a card is available to read.
#    uid = pn532.read_passive_target()
    # Try again if no card is available.
#    if uid is "no_card":
#        CardState = "none"
#        continue

    if CardState == "init":
        debug_print("Waiting for card...")
        CardState = "read"

    elif CardState == "read":
        #Wait to read a card
        uid = pn532.read_passive_target()

        if uid == "no_card":
#	    print("waiting for card...{}".format(uid))
            CardState = "read"
        else:
#	    print("waiting for card...{}".format(format(binascii.hexlify(uid))))
            CardState = "card_detected"

    elif CardState == "card_detected":
        debug_print("card detected: {}".format(format(binascii.hexlify(uid))))
        subprocess.call("./bip.sh", shell=True)
        CardID = int(binascii.hexlify(uid), 16)
        #Wait to remove card
        debug_print("waiting card is removed") 
        CardState = "waiting_remove"

    elif CardState == "waiting_remove":
        uid = pn532.read_passive_target()
 
        if uid == "no_card":
#            print("card removed.")
            CardState = "init"
            #Alternative: exit script and return tag ID
            if CardID == int("0xd3615d59", 16):
                debug_print("Master key detected {}".format(CardID))
                debug_print("Unlock")
                subprocess.call("./bip.sh", shell=True)
                subprocess.call("./bip.sh", shell=True)
                subprocess.call("./unlock.sh", shell=True)
            else:
                #record tag ID
                debug_print("write tag id")
                taglistFile = open("input_badge.txt", "a")
                taglistFile.write("badge-{}\n".format(hex(CardID)))
                taglistFile.close()
#                print("cardnum: {}".format(cardNum))
#                print("card number {}".format(CardID))   
#                sys.exit(CardID)
                
    else:
        CardState = "init"

