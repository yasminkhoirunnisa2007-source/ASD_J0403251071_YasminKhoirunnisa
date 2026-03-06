#============================================================
# Nama: Yasmin Khoirun Nisa
# NIM: J0403251071
# Kelas: TPL A2
# Insertion SORT Ascending
#============================================================

def insertionsort(data):
    for index in range(1,len(data)):

        currentvalue = data[index]
        position = index

        while position>0 and data[position-1]>currentvalue:
            data[position]=data[position-1]
            position = position-1
            data[position]=currentvalue

data = [54,26,93,17,77,31,44,55,20]
insertionsort(data)
print(data)