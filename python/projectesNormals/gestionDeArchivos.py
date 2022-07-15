import shutil
import os

source = r'C:\Users\Jaume Fernandez\Downloads'
destinationFotos = r'C:\Users\Jaume Fernandez\Downloads\imagenes'
destinationPdfs = r'C:\Users\Jaume Fernandez\Downloads\pdfs'
destinationZips = r'C:\Users\Jaume Fernandez\Downloads\zips'
destinationTorrents = r'C:\Users\Jaume Fernandez\Downloads\torrents'
destinationExe = r'C:\Users\Jaume Fernandez\Downloads\exes'
destinationApk = r'C:\Users\Jaume Fernandez\Downloads\apks'
destinationIsos = r'C:\Users\Jaume Fernandez\Downloads\isos'
destinationRandom = r'C:\Users\Jaume Fernandez\Downloads\random'

files = os.listdir(source)
imatges = ["PNG","png","jpg","peg","fif","gif"]
pdf = ["pdf"]
zips = ["rar","zip"]
torrents = ["ent"]
exes = ["exe","msi"]
apks = ["apk"]
isos = ["iso"]
tipos = (imatges,pdf,zips,torrents,exes,apks,isos)
destinaciones = (destinationFotos,destinationPdfs,destinationZips,destinationTorrents,destinationExe,destinationApk,destinationIsos)

def organizar(array):
    textos = []

    for file in files:
        for y in array:
            if (file[-3:] == y):
                textos.append(file)

    return textos

def organizarTotARandom():
    for x in files:
        if (x != "imagenes" and x != "pdfs" and x != "zips" and x != "torrents" and x != "exes" and x != "apks" and x != "isos"):
            new_path = shutil.move(f"{source}/{x}", destinationRandom)
            print(new_path)   

def organizarMain(tipo,destinacio):            
    for x in tipo:
        new_path = shutil.move(f"{source}/{x}", destinacio)
        print(new_path)

def ProgramaMain():
    contador = 0
    for x in destinaciones:
        organizarMain(organizar(tipos[contador]),destinaciones[contador])
        contador = contador + 1

    organizarTotARandom()    

ProgramaMain()   