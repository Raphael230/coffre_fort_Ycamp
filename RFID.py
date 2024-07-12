import mfrc522
from os import uname

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring

def do_read():

	rdr = mfrc522.MFRC522(sck=18, mosi=23, miso=19, rst=3, cs=21)

	while True:
		(stat, tag_type) = rdr.request(rdr.REQIDL)

		if stat == rdr.OK:

			(stat, raw_uid) = rdr.SelectTagSN()

			if stat == rdr.OK:
				return "902A3D03" == uidToString(raw_uid)

# print(do_read())