from parsing import *
import hashlib,json


def hashing( info ):
	i = 0
	hashedUserInfo = [None]*3
	for x in info:
		str = hashlib.sha256(x.encode('utf-8'))
		hashedUserInfo[i] = str.hexdigest()
		++i
		return 'done'
