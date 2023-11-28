storona1 = int(input('storona a'))
storona2 = int(input('storona b'))
storona3 = int(input('storona c'))
if (storona1+storona2) > storona3 and (storona1+storona3) > storona2 and (storona2+storona3) > storona1:
    print('sushestvuet')
else:
    print('ne sushestvuet')
