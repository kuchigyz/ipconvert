def submit(ipString, maskString):
    def binToList(b):
        return [int(d) for d in bin((1 << 8) + b)[-8:]]

    def listToStr(l):
        return '.'.join([str(i) for i in l])

    ip = [int(i) for i in ipString.split('.')]
    mask = [int(i) for i in maskString.split('.')]
    if ip[0] < 128:
        ipClass = 1
    elif ip[0] < 192:
        ipClass = 2
    else:
        ipClass = 3
    a = binToList(ip[ipClass])
    b = binToList(mask[ipClass])

    # Number of Subnet Bits
    subnetBits = 0
    for i in range(len(b) - 1, -1, -1):
        if b[i] == 1:
            subnetBits = i + 1
            break

    # Number of Host Bits
    if ipClass == 1:
        hostBits = 3 * 8 - subnetBits
    if ipClass == 2:
        hostBits = 2 * 8 - subnetBits
    if ipClass == 3:
        hostBits = 8 - subnetBits

    # Network Address
    networkAddress = ip.copy()
    networkAddress[ipClass] = ip[ipClass] & mask[ipClass]
    if ipClass == 1:
        networkAddress[ipClass + 1] = 0
        networkAddress[ipClass + 2] = 0
    if ipClass == 2:
        networkAddress[ipClass + 1] = 0

    # First Host Address
    firstHostAddress = networkAddress.copy()
    firstHostAddress[3] += 1

    # Broadcast Address
    broadcastAddress = networkAddress.copy()
    broadcastAddress[ipClass] = binToList(broadcastAddress[ipClass])
    for i in range(subnetBits, 8):
        broadcastAddress[ipClass][i] = 1
    broadcastAddress[ipClass] = int(''.join(map(str, broadcastAddress[ipClass])), 2)
    if ipClass == 1:
        broadcastAddress[2] = 255
        broadcastAddress[3] = 255
    if ipClass == 2:
        broadcastAddress[3] = 255

    # Last Host Address
    lastHostAddress = broadcastAddress.copy()
    lastHostAddress[3] -= 1

    # Print
    result = 'SubnetBits: {}\nSubnets:    {}\nHostBits:   {}\nHosts:      {}\nNetwork:    {}\nFirst host: {}\nLast host:  {' \
             '}\nBroadcast:  {}\n\n Bitwise Multiplication\n{}\n{}\n{}'.format(
        str(subnetBits), str(2 ** subnetBits), str(hostBits), str(2 ** hostBits - 2), listToStr(networkAddress),
        listToStr(firstHostAddress), listToStr(lastHostAddress), listToStr(broadcastAddress), a, b,
        binToList(networkAddress[ipClass]))

    return result
