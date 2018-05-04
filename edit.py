import urllib2
import re

url = "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts"

hosts = urllib2.urlopen(url)
with open('hosts.txt', "wb") as outfile:
    for line in hosts:
        if not re.search(r"#.*\n", line):
                line = re.sub(r"[0-255]+.[0-255]+.[0-255]+.[0-255]+", "127.0.0.1", line)
                outfile.write(line)
