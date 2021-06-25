def swapFileData():

    nameOfSwapppableFile=input("Enter Your File to swap for Name here (Mention path if in another folder) : ")
    nameOfSwappingFile=input("Enter Your File to swap with Name here (Mention path if in another folder) : ")

    data_a=open("sample1.txt",'w')
    data_b=open("sample2.txt",'w')

    data_a = nameOfSwapppableFile
    data_b=nameOfSwappingFile

swapFileData()