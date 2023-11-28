#opredelite k kakoy vozrostnoy gryppe otonistsya polzovatel,
# esly 0-17 rebenok, 18-50 vzrosiy
# 51 i bolee pozhiloy
age = int(input('vvedite vozrast'))
if age <= 17:
    print('rebenok')
elif 18 <= age <= 50:
    print('vzrosliy')
else:
    print('pozhiloy')