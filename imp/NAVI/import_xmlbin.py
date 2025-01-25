with open('evil_myk_nvm.NAVI.xmlbin', 'rb') as f:
    hexdata = f.read().hex()


def Index_to_int(num):
    temp1 = ''
    k = 0
    while k < len(num):
        if num == "00000000":
            temp1 = "0"
            break
        if num[k] == "0":
            pass
        if num[k] != "0":
            temp1 = str(num[k:])
            break
        k += 1
    # print(f'{num} {temp1}')
    if str(num) == "ffffffff":
        out_value = -1
    else:
        out_value = int(temp1, 16)
    # print(out_value)
    return out_value


def array_creation(array):
    marray = []
    for i in array:
        temp = Index_to_int(str(i)[-(4*2):])
        marray.append(temp)

    return marray


def array_conv(array):
    temp_arr = []
    for i in range(len(array)):
        temp_arr.append(int(array[i], 16))
    return temp_arr


def array_read(array, Offset, file):
    temp_arr = []
    i = 0
    while (len(array)) > i:
        temp_arr.append(file[(array[i] + Offset) * 2:(array[i] + 16 + Offset) * 2])
        i += 1
    return temp_arr


def new_array_cr(file, length, startAdr):
    # print(f'{type(file)} {originalAdr} {length} {startAdr} {Offset}')
    start = startAdr
    end = startAdr + (length * 4) * 2
    my_array = []
    og_array = file[start:end]
    # print(og_array)

    i = 0
    while int(len(og_array) * 2) > i:
        a = ''
        ind = 0
        if i < length * 4 * 2:
            for j in range(8):
                a = a + str(og_array[i + ind])
                ind += 1
        else:
            break
        # print(a)
        my_array.append(a)
        i += 8
    return my_array


def ieee754_to_float(my_hexdata):
    scale = 16  # equals to hexadecimal
    num_of_bits = 8
    num_out = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    print(my_hexdata)
    flis = [int(x) for x in str(num_out)]
    slis = []
    for i in range(len(flis)):
        if (i == 1 or (i - 1) % 8 == 0):
            slis.append(" ")
            slis.append(flis[i])
        else:
            slis.append(flis[i])
    a = ''.join([str(s) for s in slis])
    # print(a)
    tlis = a.split()
    print(tlis)
    my_bin = ''.join(tlis)
    print(my_bin)


def read_file(file):
    intro = file[:160 * 2]
    splitted_intro = []
    i = 0
    while int(len(intro) * 2) > i:
        a = ''
        ind = 0
        if i < 320:
            for j in range(8):
                a = a + str(intro[i + ind])
                ind += 1
        else:
            break
        # print(a)
        splitted_intro.append(a)
        i += 8
    # print(splitted_intro)
    file_size = int(splitted_intro[0], 16)
    DataEndAddress = int(splitted_intro[2], 16)
    Offset = int(splitted_intro[3], 16)
    DataEndAddress2 = int(splitted_intro[4], 16)
    BlankSpace = int(splitted_intro[5], 16)
    Unknown1 = int(splitted_intro[8], 16)
    Unknown2 = int(splitted_intro[9], 16)
    ParentNodeCount = int(splitted_intro[10], 16)

    FirstNode, EndAddressOf1N = int(splitted_intro[11], 16), int(splitted_intro[12], 16)  # Layout
    SecondNode, EndAddressOf2N = int(splitted_intro[13], 16), int(splitted_intro[14], 16)  # AdjFaceIndex
    ThirdNode, EndAddressOf3N = int(splitted_intro[15], 16), int(splitted_intro[16], 16)  # color
    FourthNode, EndAddressOf4N = int(splitted_intro[17], 16), int(splitted_intro[18], 16)  # Illum
    FifthNode, EndAddressOf5N = int(splitted_intro[19], 16), int(splitted_intro[20], 16)  # Vertex Info
    SixsNode, EndAddressOf6N = int(splitted_intro[21], 16), int(splitted_intro[22], 16)  # Vertex Index
    #    print(f'{EndAddressOf2N + Offset} {EndAddressOf2N + 4 * 2 + Offset}')
    #    print(file[(EndAddressOf2N + Offset + 8) * 2:(EndAddressOf2N + Offset + 4 + 8) * 2])

    FirstBlockStart = int(splitted_intro[23], 16) * 2
    Unknown3 = int(splitted_intro[24], 16)
    UnknownNode, UnknownNodeValue = int(splitted_intro[25], 16), int(splitted_intro[26], 16)
    UnknownNode2, UnknownNode2Value = int(splitted_intro[27], 16), int(splitted_intro[28], 16)
    Unknown4 = int(splitted_intro[29], 16)
    UnknownNode3, UnknownNode3Value = int(splitted_intro[30], 16), int(splitted_intro[31], 16)
    SomethingFromDataSize1 = int(splitted_intro[32], 16)
    Unknown5 = int(splitted_intro[33], 16)
    UnknownNode4 = int(splitted_intro[34], 16)
    UnknownNode5 = int(splitted_intro[35], 16)
    Unknown6 = int(splitted_intro[36], 16)
    SomethingFromDataSize2 = int(splitted_intro[37], 16)
    Unknown7 = int(splitted_intro[38], 16)

    AdjFaceIndex_IDs = new_array_cr(file,
                                    int(file[(EndAddressOf2N + Offset + 8) * 2:(EndAddressOf2N + Offset + 8 + 4) * 2],
                                        16),
                                    (EndAddressOf2N + Offset + 16) * 2)
    AdjFaceIndex_adr = array_conv(AdjFaceIndex_IDs)
    #    print(AdjFaceIndex_adr)

    AdjFaceIndex_og = array_read(AdjFaceIndex_adr, Offset, file)
    #print(AdjFaceIndex_og)
    AdjFaceIndex = array_creation(AdjFaceIndex_og)
    print(AdjFaceIndex)


# checkpoints (end of ... )
first_part = (176 - 4) * 2
first_triplets = (21296 - 4) * 2
data_after_ft = (105792 - 4) * 2
second_triplets = (112832 - 4) * 2
data_after_st = (140992 - 4) * 2
third_triplets = (148048 - 4) * 2
data_after_tt = (176224 - 4) * 2  # 176208 or 176224

# first part (if I'll need it)
read_file(hexdata)

# AdjFaceIndex extraction (still first part)
# testingADJ = hexdata[first_part:first_triplets]
# AdjFaceIndex = array_creation(first_part, first_triplets, data_after_ft)
# print(len(testingADJ) / 8)
# print(len(AdjFaceIndex))  # the extracted AdjFaceIndex data

# loading second parts
# color = array_creation(data_after_ft, second_triplets, data_after_st)
# print(color)  # the extracted color data (should be 1)

# loading third parts
# Illum = array_creation(data_after_st + (12 * 2), third_triplets, data_after_tt)
# print(Illum)  # the extracted color data (should be 0)
