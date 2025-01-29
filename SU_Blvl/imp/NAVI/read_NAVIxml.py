import xml.etree.ElementTree as ET

class read_NAVIxml():
    def read_file(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()

        #VertexData
        vd = []
        for i in range(len(root[1])):
            vd.append([])
            for j in range(len(root[1][i])):
                vd[i].append(float(root[1][i][j].text))

        #VertexIndex
        VertexIndex = []
        for i in range(len(root[2])):
            VertexIndex.append(int(root[2][i].text))

        #AdjFaceIndex
        AdjFaceIndex = []
        for i in range(len(root[3])):
            AdjFaceIndex.append(int(root[3][i].text))

        #color
        color = []
        for i in range(len(root[4])):
            color.append(int(root[4][i].text))

        #Illum
        Illum = []
        for i in range(len(root[5])):
            Illum.append(int(root[5][i].text))

        return AdjFaceIndex, color, Illum, vd, VertexIndex