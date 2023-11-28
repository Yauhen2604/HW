s = input('enter str')
s1 = s.replace(' ', '')
if s1 == s1[::-1]:
    print('poliandrom')
else:
    print('not poliandrom')

s2 = 'Hello Every1'
s3 = (s2[s2.find(' '):] + ' ' + s2[0:s2.find(' ')])
print(s3)
print(s3.replace('1', 'one'))

s4 = input('enter')
print(s4[2])
print(s4[-2])
print(s4[0:5])
print(s4[0:-2])
print(s4[0::2])
print(s4[1::2])
print(s4[::-1])
print(s4[::-2])
print(len(s4))




