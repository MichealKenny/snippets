#Micheal Kenny
from urllib import urlopen, urlretrieve

print 'Checking for updates...'

#Variables
cb_url = 'http://dl.bukkit.org/api/1.0/downloads/projects/craftbukkit/artifacts/'
cb_xml = urlopen(cb_url).read()
cb_list = cb_xml.split(',')
cb_version = (cb_list[12].split('"'))[3]
cb_size = round(float(((cb_list[15].split('"'))[2])[2:10]) / 1024000, 2)
cbdev = (cb_list[13].split('"'))[5]
cb_build = (cb_list[1].split(': '))[1]

if cb_build != ((open('build.txt').readlines())[0]).strip():
    print 'Downloading:', cb_version, cb_build + ',', str(cb_size) + 'MB'

    #Download file
    urlretrieve(cbdev, filename='craftbukkit.jar')
    
    open('build.txt', 'w').write(cb_build)
    print 'Saved as: craftbukkit.jar'

else:
    print 'Bukkit is up to date.'