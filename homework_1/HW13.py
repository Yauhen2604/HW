day = int(input('enter day'))
month = input('enter month')
if ((month == 'march') and (21 <= day <= 31)) or ((month == 'april') and (1 <= day <= 20)):
    print('oven')
elif ((month == 'april') and (21 <= day <= 30)) or ((month == 'may') and (1 <= day <= 21)):
    print('taurus')
elif ((month == 'may') and (22 <= day <= 31)) or ((month == 'june') and (1 <= day <= 21)):
    print('bliznec')
elif ((month == 'june') and (22 <= day <= 30)) or ((month == 'july') and (1 <= day <= 22)):
    print('rak')
elif ((month == 'july') and (23 <= day <= 31)) or ((month == 'august') and (1 <= day <= 21)):
    print('lion')
elif ((month == 'august') and (22 <= day <= 31)) or ((month == 'september') and (1 <= day <= 23)):
    print('deva')
elif ((month == 'september') and (24 <= day <= 30)) or ((month == 'oktober') and (1 <= day <= 23)):
    print('vesy')
elif ((month == 'oktober') and (24 <= day <= 31)) or ((month == 'november') and (1 <= day <= 22)):
    print('skorp')
elif ((month == 'nowember') and (23 <= day <= 30)) or ((month == 'december') and (1 <= day <= 22)):
    print('strelec')
elif ((month == 'december') and (23 <= day <= 31)) or ((month == 'january') and (1 <= day <= 20)):
    print('kozerog')
elif ((month == 'january') and (21 <= day <= 31)) or ((month == 'february') and (1 <= day <= 19)):
    print('vodoley')
elif ((month == 'february') and (20 <= day <= 28)) or ((month == 'march') and (1 <= day <= 20)):
    print('fish')
else:
    print('enter correctly')
