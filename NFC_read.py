
import binascii
import sys
import time
import PN532
import subprocess

global CardState
global CardID
global cardNum
global tagListe

#Create an instance of the PN532 class
pn532 = PN532.PN532("/dev/ttyAMA0", 115200)

#Initialize communiction with PN532
pn532.begin()

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

# Get the firmware version from the chip and print(it out.)
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
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
        print("Waiting for card...")
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
        print("card detected: {}".format(format(binascii.hexlify(uid))))
        subprocess.call("./bip.sh", shell=True)
        CardID = int(binascii.hexlify(uid), 16)
        #Wait to remove card
        print("waiting card is removed") 
        CardState = "waiting_remove"

    elif CardState == "waiting_remove":
        uid = pn532.read_passive_target()
 
        if uid == "no_card":
#            print("card removed.")
            CardState = "init"
            #Alternative: exit script and return tag ID
            if CardID == int("0xd3615d59", 16):
                print("Master key detected {}".format(CardID))
                print("Unlock")
                subprocess.call("./bip.sh", shell=True)
                subprocess.call("./bip.sh", shell=True)
                subprocess.call("./unlock.sh", shell=True)
            else:
                #record tag ID
                print("write tag id")
                taglistFile = open("input_badge.txt", "a")
                taglistFile.write("badge-{}\n".format(hex(CardID)))
                taglistFile.close()
#                print("cardnum: {}".format(cardNum))
#                print("card number {}".format(CardID))   
#                sys.exit(CardID)
                
    else:
        CardState = "init"

    #Card is found
#    print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
    # Authenticate block 4 for reading with default key (0xFFFFFFFFFFFF).
#    for i in range(0,16):
 #       if not pn532.mifare_classic_authenticate_block(uid, i, PN532.MIFARE_CMD_AUTH_B,
#                                                       [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]):
  #          print('Failed to authenticate block ')+str(i)
   #         break
        # Read block 4 data.
    #    data = pn532.mifare_classic_read_block(i)
     #   if data is None:
      #      print('Failed to read block ')+str(i)
       #     continue
        # Note that 16 bytes are returned, so only show the first 4 bytes for the block.

     #   print "Read block "+str(i)+" - "+(': 0x{0}'.format(binascii.hexlify(data[:16]))) + " - "+''.join(map(chr,data))

        # Example of writing data to block 4.  This is commented by default to
        # prevent accidentally writing a card.
        # Set first 4 bytes of block to 0xFEEDBEEF.
        # data[0:4] = [0xFE, 0xED, 0xBE, 0xEF]
        # # Write entire 16 byte block.
        # pn532.mifare_classic_write_block(4, data)
        # print('Wrote to block 4, exiting program!')
        # # Exit the program to prevent continually writing to card.
# sys.exit(0)


