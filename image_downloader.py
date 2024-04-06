import sys

fpath = sys.argv[1]
range_start = int(sys.argv[2])
range_end = int(sys.argv[3])
fout = sys.argv[4]

with open(fpath, "r") as f:
    lines = f.readlines()
    urls = [line.replace("\n", "") for line in lines]

import urllib.request
idx = range_start
for url in urls[range_start: range_end]:
    urllib.request.urlretrieve(url, fout + "_{}.png".format(idx))
    idx += 1