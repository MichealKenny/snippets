#Program to perform a series of tasks related to computer networking.
#Tested on Linux Mint 17 and Windows 7
from subprocess import check_output, CalledProcessError
from re import findall
from os import name

def ping():
    if name == 'posix':
        try:
            output = check_output('ping -c 1 ' + ip_addr, shell=True)

            #Obtain latency from the output, Regex find third last float.
            latency = (findall('\d+.\d+', output))[-3]

            print 'The latency of the connection is:', latency, 'ms'

        except CalledProcessError:
            print 'Could not ping:', ip_addr

    elif name == 'nt':
        try:
            output = check_output('ping -n 2 ' + ip_addr)

            #Obtain latency from the output, Regex find last int.
            latency = (findall('\d+', output))[-1]

            print 'The latency of the connection is:', latency, 'ms'

        except CalledProcessError:
            print 'Could not ping:', ip_addr

def multi_ping():
    if name == 'posix':
        try:
            output = check_output('ping -c 1 ' + ip_addr, shell=True)

            #Obtain latency from the output, Regex find third last float.
            latency = (findall('\d+.\d+', output))[-3]

            #Add latency to list.
            latency_list.append(float(latency))

        except CalledProcessError:
            print 'Could not ping:', ip_addr
            latency_list.append(9999)

    elif name == 'nt':
        try:
            output = check_output('ping -n 1 -l 128 ' + ip_addr)

            #Obtain latency from the output, Regex find last int.
            latency = (findall('\d+', output))[-1]

            #Add latency to list.
            latency_list.append(int(latency))

        except CalledProcessError:
            print 'Could not ping:', ip_addr
            latency_list.append(9999)

#Choice
print 'Network Utils performs a series of tasks related to computer networking.'
print '[0]Ping an IP, [1]Fastest route finder, [2]Network address finder'
choice = input('Please choose from 0/1/2: ')

#Main If statment.
if choice == 0: #Ping an IP address.

    #Input and ping the IP address.
    ip_addr = raw_input('Please enter an IP address: ')

    #Ping IP address.
    ping()

elif choice == 1: #Fastest route finder.

    #Local Variables.
    ip_list = []
    latency_list = []
    finished = 'N'

    #Choose which way to input addresses.
    print 'Would you like to enter the addresses [0]one-by-one or [1]import them from a text file?'
    choice = input('Please choose from 0/1: ')

    if choice == 0:
        #Enter IP address until user is finished.
        while finished != 'Y':
            #Input IP address.
            ip_addr = raw_input('Please enter an IP address: ')
            ip_list.append(ip_addr)

            #Continue/Cancel.
            print 'Are you finished entering IPs?'
            finished = raw_input('Y/N?: ')

    elif choice == 1:

        #Type file location.
        print 'Location of file relative to .py, eg: data/file.txt'
        ip_file = raw_input('File location: ')

        #Add each line of the text file to the IP list.
        for line in open(ip_file):
            ip_list.append(line.strip())


    #Ping each IP address.
    for ip_addr in ip_list:
        #Ping each IP in list.
        multi_ping()

    #Match up lowest latency value with the corresponding IP address.
    index = latency_list.index(min(latency_list))

    #Display the fastest route and it's latency.
    print 'The fastest route is:', ip_list[index], 'with a latency of:', str(latency_list[index]), 'ms.'

elif choice == 2: #Find the network address given the IP and subnet.

    #Variables.
    count = 0
    net_octet_list = []

    #Inputs.
    ip_addr = raw_input('Please enter the IP address(192.168.1.56): ')
    subnet_mask = raw_input('Please enter the subnet mask(255.255.255.240): ')

    #Split inputs.
    ip_octet_list = ip_addr.split('.')
    subnet_octet_list = subnet_mask.split('.')

    #And each octet in the IP and Subnet together.
    for ip_octet in ip_octet_list:
        net_octet = int(ip_octet) & int(subnet_octet_list[count])
        net_octet_list.append(net_octet)
        count += 1

    #Output.
    print 'The network address is:', str(net_octet_list[0]) + '.' + str(net_octet_list[1]) + '.' + str(net_octet_list[2]) + '.' + str(net_octet_list[3])
