import re                                                   #for splitting according multiple seperators

IP=input("Enter IP: ")
octets_as_string=re.split("[./]",IP)                        #[192,168,6,161,24]  ==> string
octets_as_integer=[]                                        #[192,168,6,161,24]  ==> integer
octets_as_binary=[]                                         #['11000000', '10101000', '00000110', '10100001']
subnet_in_binary=[]
IP=''                                                       #11000000101010000000011010100001
mask=''                                                     #11111111111111111111111100000000
subnet_id=''


#192.168.6.161/24

def string_to_int(octets_as_string):
    integer=0
    for i in range(0,len(octets_as_string)):
        integer=int(octets_as_string[i])
        if(integer>255):
            print("Format is not true!")
            quit()
        octets_as_integer.append(integer)

def ip_as_binary(octets_as_int):
    ip=''
    for i in range(0,len(octets_as_int)-1):
        octets_as_binary.append("{0:08b}".format(octets_as_int[i]))
        ip+=octets_as_binary[i]

    return ip

def mask_as_binary(mask_as_int):
    mask=''
    for i in range(0,32):
        if(i<mask_as_int):
            mask+='1'
        else:
            mask+='0'

    return mask

def subnet_id_as_binary(ip,mask):
    subnet_id=''
    for i in range(0,32):
        subnet_id+=str(int(ip[i]) & int(mask[i]))

    return subnet_id
    
def binary_to_int(binary):
    integer=[]
    temp=''
    for i in range (0,32,8):
        for j in range (i,i+8):
            temp+=binary[j]
        
        integer.append(int(temp,2))
        temp=''

    return integer
        
def print_ip(type,ip_as_massive):
    print(type+' is: '+ str(ip_as_massive[0])+'.'+ str(ip_as_massive[1])+'.'+ str(ip_as_massive[2])+'.'+ str(ip_as_massive[3]))


string_to_int(octets_as_string)
IP=ip_as_binary(octets_as_integer)
mask=mask_as_binary(octets_as_integer[4])
subnet_id=subnet_id_as_binary(IP,mask)

print('\n-------------------------------------------------------------------------')
print_ip("Subnet mask",binary_to_int(mask))
print_ip("Subnet ID",binary_to_int(subnet_id))
print('---------------------------------------------------------------------------\n')