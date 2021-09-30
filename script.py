import os
import sys
import shutil
from time import sleep

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

if __name__ == "__main__":
    print("Escolha qual conversor quer usar")
    print("1 - bmp2isc")
    print("2 - bmp2oac2")
    op = int(input())
    path = get_script_path()
    path += '/imagens'
    os.chdir(path)
    print(path)
    imgNames = os.listdir(path)
    for imgNames in imgNames:
        if imgNames[-1:-4] == '.bmp':
            imgNamesStrip = imgNames.replace(' ','')
            os.rename(imgNames, imgNamesStrip)
            imgNamesStrip = imgNamesStrip[-4:]
            if op == 1:
                x = 'bmp2isc.exe'
            if op == 2:
                x = 'bmp2oac2.exe'
            x += ' ' + imgNamesStrip
            print(imgNames + " convertido com sucesso!")
            os.system(x)
    if op == 1:
        directory = "arquivos .data"
        parent_dir = get_script_path()
        parent_dir += '/imagens'
        newpath = os.path.join(parent_dir, directory)
        try:
            os.mkdir(newpath)
        except:
            pass
        imgNames = os.listdir(path)
        for imgNames in imgNames:
            if imgNames[-1] == 'a':
                shutil.move(imgNames, newpath)
            
        print('Arquivos convertidos com sucesso!')
        sleep(1)

    if op == 2:
        parent_dir = get_script_path()
        parent_dir += '/imagens'
        directory = "arquivos .s"
        fs = os.path.join(parent_dir, directory)
        try:
            os.mkdir(fs)
        except:
            pass
        directory = "arquivos .mif"
        fmif = os.path.join(parent_dir, directory)
        try:
            os.mkdir(fmif)
        except:
            pass
        directory = "arquivos .bin"
        fbin = os.path.join(parent_dir, directory)
        try:
            os.mkdir(fbin)
        except:
            pass
        imgNames = os.listdir(path)
        for imgNames in imgNames:
            if imgNames[-1] == 's':
                shutil.move(imgNames, fs)
            elif imgNames[-1] == 'f':
                shutil.move(imgNames, fmif)
            elif imgNames[-1] == 'n':
                shutil.move(imgNames, fbin)
        print('Arquivos convertidos com sucesso!') 
