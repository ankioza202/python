from struct import *

# store as bytes data
packed_data=pack('iif', 6, 19, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get data back to normal data
original_data = unpack('iif',packed_data)
print(original_data)

#print(unpack('iif',b\'      )\�@'))
