import os
import urllib2

def download_file(url, file_name):
	print url
	u = urllib2.urlopen(url)

	dir = os.path.dirname(file_name)
	if not os.path.exists(dir):
		os.makedirs(dir)
	else: # if the file is already downloaded
		print "!-Already downloaded-!"
		return

	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	f.close()
