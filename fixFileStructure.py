import os, shutil

filePath = 'C:/Users/Colby/Desktop/Test/UTSig/UTSig'

filePathGen = filePath + '/Genuine'
filePathFor = filePath + '/Forgery'
filePathForSk = filePath + '/Forgery/Skilled' 
filePathForOh = filePath + '/Forgery/Opposite Hand' 
filePathForSi = filePath + '/Forgery/Simple' 

if "1" in os.listdir(filePathGen):
    for i in os.listdir(filePathGen):
        author = i
        for j in os.listdir(filePathGen + '/' + author):
            os.rename(filePathGen + '/' + author + "/" + j, filePathGen + "/" + "g_" + author + "_" + j + ".tif")
        os.removedirs(filePathGen + "/" + author)

if "Skilled" in os.listdir(filePathFor):
    for i in os.listdir(filePathForSk):
        author = i
        for j in os.listdir(filePathForSk + '/' + author):
            os.rename(filePathForSk + '/' + author + "/" + j, filePathFor + "/" + "fSk_" + author + "_" + j + ".tif")
        os.removedirs(filePathForSk + "/" + author)

if "Opposite Hand" in os.listdir(filePathFor):
    for i in os.listdir(filePathForOh):
        author = i
        for j in os.listdir(filePathForOh + '/' + author):
            os.rename(filePathForOh + '/' + author + "/" + j, filePathFor + "/" + "fOh_" + author + "_" + j + ".tif")
        os.removedirs(filePathForOh + "/" + author)

if "Simple" in os.listdir(filePathFor):
    shutil.rmtree(filePathForSi)
