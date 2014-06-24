#Basic function to check for updates.
from urllib2 import urlopen

version = '2.1.0.2'
url = 'https://dl.dropboxusercontent.com/u/9528427/update.txt'

def update_check(version,url):
    print 'Checking for update...'
    for line in urlopen(url):
        line = line.split(',')
        if line[0] != version:
            print 'Update', line[0], 'available at:', line[1]
            print 'Current version:', version
        else:
            print 'No update available.'