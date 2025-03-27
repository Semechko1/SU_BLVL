from ..IEEE754_to_float import ieee754_to_float


class read_xmlbin():

    def Index_to_int(self, num):
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

    def conv_vert_data_array(self, array):
        temp_arr = []
        for i in range(len(array)):
            temp_arr.append([])
            for j in range(len(array[i])):
                if (j == 11 or j == 16 or j == 21):
                    temp_arr[i].append(ieee754_to_float(array[i][j]))
        return temp_arr

    def array_sep(self, array):
        a = 0
        temp_arr = []
        i = 0
        while len(array) > i:
            temp_arr.append([])
            while (int(len(array[i]))) > a:
                temp_arr[i].append(array[i][a:a + 8])
                a += 8
            a = 0
            i += 1

        return temp_arr

    def array_creation(self, array):
        marray = []
        for i in array:
            temp = read_xmlbin.Index_to_int(self,str(i)[-(4 * 2):])
            marray.append(temp)

        return marray

    def array_conv(self, array):
        temp_arr = []
        for i in range(len(array)):
            temp_arr.append(int(array[i], 16))
        return temp_arr

    def array_read(self, array, Offset, file, lengh):
        temp_arr = []
        i = 0
        while (len(array)) > i:
            temp_arr.append(file[(array[i] + Offset) * 2:(array[i] + lengh + Offset) * 2])
            i += 1
        return temp_arr

    def new_array_cr(self, file, length, startAdr):
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

    def read_file(self, filepath):
        with open(filepath, 'rb') as f:
            file = f.read().hex()
        intro = file[:160 * 2]
        #print(len(intro))
        #print(intro)
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

        # AdjFaceIndex
        AdjFaceIndex_IDs = read_xmlbin.new_array_cr(self,file,
                                        int(file[
                                            (EndAddressOf2N + Offset + 8) * 2:(EndAddressOf2N + Offset + 8 + 4) * 2],
                                            16),
                                        (EndAddressOf2N + Offset + 16) * 2)
        AdjFaceIndex_adr = read_xmlbin.array_conv(self,AdjFaceIndex_IDs)
        #    print(AdjFaceIndex_adr)
        AdjFaceIndex_og = read_xmlbin.array_read(self,AdjFaceIndex_adr, Offset, file, 16)
        # print(AdjFaceIndex_og)
        AdjFaceIndex = read_xmlbin.array_creation(self,AdjFaceIndex_og)
        # print(AdjFaceIndex)

        # color
        color_IDs = read_xmlbin.new_array_cr(self,file,
                                 int(file[(EndAddressOf3N + Offset + 8) * 2:(EndAddressOf3N + Offset + 8 + 4) * 2], 16),
                                 (EndAddressOf3N + Offset + 16) * 2)
        # print(color_IDs)
        color_adr = read_xmlbin.array_conv(self,color_IDs)
        color_og = read_xmlbin.array_read(self,color_adr, Offset, file, 16)
        # print(color_og)
        color = read_xmlbin.array_creation(self,color_og)
        # print(color)
        # print(f'{len(color)} and {len(color_IDs)}')

        # Illum
        Illum_IDs = read_xmlbin.new_array_cr(self,file,
                                 int(file[(EndAddressOf4N + Offset + 8) * 2:(EndAddressOf4N + Offset + 8 + 4) * 2], 16),
                                 (EndAddressOf4N + Offset + 16) * 2)
        # print(Illum_IDs)
        Illum_adr = read_xmlbin.array_conv(self,Illum_IDs)
        Illum_og = read_xmlbin.array_read(self,Illum_adr, Offset, file, 16)
        # print(Illum_og)
        Illum = read_xmlbin.array_creation(self,Illum_og)
        # print(Illum)
        # print(f'{len(Illum)} and {len(Illum_IDs)}')

        # Vertex Data
        vd_IDs = read_xmlbin.new_array_cr(self,file,
                              int(file[(EndAddressOf5N + Offset + 8) * 2:(EndAddressOf5N + Offset + 8 + 4) * 2], 16),
                              (EndAddressOf5N + Offset + 16) * 2)
        # print(cd_IDs)
        vd_adr = read_xmlbin.array_conv(self,vd_IDs)
        vd_og = read_xmlbin.array_read(self,vd_adr, Offset, file, 88)
        # print(vd_og)
        test_vd_sep_og = read_xmlbin.array_sep(self,vd_og)
        # print(test_vd_sep_og)
        vd = read_xmlbin.conv_vert_data_array(self,test_vd_sep_og)
        # print(vd)

        # VertexIndex
        VertexIndex_IDs = read_xmlbin.new_array_cr(self,file,
                                       int(file[
                                           (EndAddressOf6N + Offset + 8) * 2:(EndAddressOf6N + Offset + 8 + 4) * 2],
                                           16),
                                       (EndAddressOf6N + Offset + 16) * 2)
        VertexIndex_adr = read_xmlbin.array_conv(self,VertexIndex_IDs)
        #    print(VertexIndex_adr)
        VertexIndex_og = read_xmlbin.array_read(self,VertexIndex_adr, Offset, file, 16)
        # print(VertexIndex_og)
        VertexIndex = read_xmlbin.array_creation(self,VertexIndex_og)
        # print(VertexIndex)

        return AdjFaceIndex, color, Illum, vd, VertexIndex
