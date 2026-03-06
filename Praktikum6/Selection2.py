#============================================================
# Nama: Yasmin Khoirun Nisa
# NIM: J0403251071
# Kelas: TPL A2
# Selection SORT Descending
#============================================================

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOFMin = 0
        for location in range(1,fillslot+1):
            if data[location] < data[positionOFMin]:
                positionOFMin = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOFMin]
        data[positionOFMin] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)
