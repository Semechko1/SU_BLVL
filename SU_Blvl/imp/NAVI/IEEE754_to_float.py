# 00008bac or 4318497a
import math

my_hexdata = "4318497A"

bytes_sep = []
a = 0
while a < 8:
    bytes_sep.append(f'{my_hexdata[a]}{my_hexdata[a + 1]}')
    a += 2
print(bytes_sep)
scale = 16  # equals to hexadecimal
num_of_bits = 8

a = bytes_sep[0]
b = bytes_sep[1]
c = bytes_sep[2]
d = bytes_sep[3]
numA_out = bin(int(a, scale))[2:].zfill(num_of_bits)
numB_out = bin(int(b, scale))[2:].zfill(num_of_bits)
numC_out = bin(int(c, scale))[2:].zfill(num_of_bits)
numD_out = bin(int(d, scale))[2:].zfill(num_of_bits)
print(f'{numA_out} {numB_out} {numC_out} {numD_out}')

num_out = str(numA_out) + str(numB_out) + str(numC_out) + str(numD_out)

flis = [int(x) for x in num_out]

slis = []
for i in range(len(flis)):
    if i == 1 or (i - 1) % 8 == 0:
        slis.append(" ")
        slis.append(flis[i])
    else:
        slis.append(flis[i])

a = ''.join([str(s) for s in slis])
# print(a)

tlis = a.split()
print(tlis)
# my_bin = ''.join(tlis)
# print(my_bin)

sign = str(tlis[0])
exponent = str(tlis[1])
mantissa = ''.join(tlis[2:])

conv_mant = 1
the_div = 2
for i in mantissa:
    if i == "0":
        the_div = the_div*2
    else:
        conv_mant += (1/the_div)
        the_div = the_div*2
# print(conv_mant)

conv_exp = math.pow(2, (int(exponent, 2)-127))
# print(conv_exp)
conv_sign = 0
if sign=="0":
    conv_sign=1
if sign=="1":
    conv_sign=-1
float_num = conv_sign * conv_exp * conv_mant
print(float_num)