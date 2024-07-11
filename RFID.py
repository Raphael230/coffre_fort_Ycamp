import mfrc522
from os import uname
def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring

def do_read():

	rdr = mfrc522.MFRC522(sck=18, mosi=23, miso=19, rst=3, cs=21)

	print("")
	print("Place card before reader to read from address 0x08")
	print("")

	try:
		while True:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.SelectTagSN()

				if stat == rdr.OK:
					print("New card detected")
					print(uidToString(raw_uid))


	except KeyboardInterrupt:
		print("Bye")

do_read()