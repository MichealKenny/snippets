#Program to perform a series of tasks related to computer networking.
#Tested on Linux Mint 16 and Windows 7
from easygui import *
from subprocess import check_output, CalledProcessError
from re import findall
from os import name

def ping():
    if name == 'posix':
        try:
            output = check_output('ping -c 1 ' + ip_addr, shell=True)
        
            #Obtain latency from the output, Regex find third last float.
            latency = (findall('\d+.\d+', output))[-3]
    
            msgbox('The latency of the connection is: ' + latency + 'ms', gui_title)
        
        except CalledProcessError:
            msgbox('Could not ping: ' + ip_addr)
    
    elif name == 'nt':
        try:
            output = check_output('ping -n 2 ' + ip_addr)
            
            #Obtain latency from the output, Regex find last int.
            latency = (findall('\d+', output))[-1]
        
            msgbox('The latency of the connection is: ' + latency + 'ms', gui_title)
            
        except CalledProcessError:
            msgbox('Could not ping: ' + ip_addr)

def multi_ping():
    if name == 'posix':
        try:
            output = check_output('ping -c 1 ' + ip_addr, shell=True)
        
            #Obtain latency from the output, Regex find third last float.
            latency = (findall('\d+.\d+', output))[-3]
            
            #Add latency to list.
            latency_list.append(float(latency))
            
        except CalledProcessError:
            msgbox('Could not ping: ' + ip_addr)
            latency_list.append(9999)
    
    elif name == 'nt':
        try:
            output = check_output('ping -n 1 -l 128 ' + ip_addr)
        
            #Obtain latency from the output, Regex find last int.
            latency = (findall('\d+', output))[-1]
            
            #Add latency to list.
            latency_list.append(int(latency))
            
        except CalledProcessError:
            msgbox('Could not ping: ' + ip_addr)
            latency_list.append(9999)

#GUI Variables.
gui_desc = 'Network Utils performs a series of tasks related to computer networking.'
gui_title = 'Network Utils'
gui_choice = ['Ping an IP', 'Fastest route finder', 'Network address finder']

#GUI Menus.
choice = buttonbox(gui_desc, gui_title, gui_choice)

#Main If statment.
if choice == gui_choice[0]: #Ping an IP address.
    
    #Input and ping the IP address.
    ip_addr = enterbox('Please enter an IP address:', gui_title, '8.8.8.8')
    
    #Ping IP address.
    ping()
    
elif choice == gui_choice[1]: #Fastest route finder.
    
    #Local Variables.
    ip_list = []
    latency_list = []
    finished = 1
    
    #Choose which way to input addresses.
    choice = buttonbox('Would you like to enter the addresses one-by-one or import them from a text file?', gui_title, ['One-by-one', 'Open file'])
    
    if choice == 'One-by-one':
        
        #Enter IP address until user is finished.
        while finished != 0:
                
                #Input IP address.
                ip_addr = enterbox('Please enter an IP address:', gui_title, '8.8.8.8')
                ip_list.append(ip_addr)
                
                #Continue/Cancel.
                finished = ynbox('Enter another IP address?')
    
    elif choice == 'Open file':
        
        #Open file window.
        ip_file = fileopenbox()
        
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
    gui_msg = 'The fastest route is: ' + ip_list[index] + ' with a latency of: ' + str(latency_list[index]) + ' ms.'
    msgbox(gui_msg, gui_title)
    
elif choice == gui_choice[2]: #Find the network address given the IP and subnet.
    
    #Variables.
    count = 0
    net_octet_list = []
    
    #Inputs.
    ip_addr = enterbox('Please enter the IP address:', gui_title, '192.168.1.56')
    subnet_mask = enterbox('Please enter the subnet mask:', gui_title, '255.255.255.240')
    
    #Split inputs.
    ip_octet_list = ip_addr.split('.')
    subnet_octet_list = subnet_mask.split('.')
    
    #And each octet in the IP and Subnet together.
    for ip_octet in ip_octet_list:
        net_octet = int(ip_octet) & int(subnet_octet_list[count])
        net_octet_list.append(net_octet)
        count += 1
        
    #Output.
    gui_msg = 'The network address is: ' + str(net_octet_list[0]) + '.' + str(net_octet_list[1]) + '.' + str(net_octet_list[2]) + '.' + str(net_octet_list[3])
    msgbox(gui_msg, gui_title)