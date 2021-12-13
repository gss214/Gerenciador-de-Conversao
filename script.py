import os
import sys
import shutil
from time import sleep


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


PATH_IMGS = get_script_path() + '/imagens/'
PATH_IMGS_TO_CONVERT = get_script_path() + '/imagens/imagens_para_conversao'
PATH_CONVERT_IMGS = get_script_path() + '/imagens/imagens_convertidas'
PATH_BMP2 = get_script_path() + '/imagens/bmp2'


def print_menu():
    print('Bem vindo ao gerenciador de conversão! Para utiliza-lo é facil, basta por todas as imagens .bmp na pasta \imagens\imagens_para_conversao e escolher um conversor abaixo, no final é só olhar a pasta /imagens/imagens_convertidas e pegar suas imagens!\n\n')
    print("Escolha qual conversor quer usar:")
    print("1 - bmp2isc")
    print("2 - bmp2oac2")


def get_input():
    user_option = input()
    while(user_option != '1' and user_option != '2'):
        print('\nOu 1 ou 2 Mermão\n')
        user_option = input()
    return user_option


def create_dir(dir_name, path):
    new_path = os.path.join(get_script_path() + path, dir_name)
    try:
        os.mkdir(new_path)
        print(f'Diretorio {dir_name} criado com sucesso!')
    except Exception as exception:
        print(exception)
    return new_path


def convert_imgs(img_names, user_option):
    for img in img_names:
        imgNamesStrip = img.replace(' ', '')
        os.rename(img, imgNamesStrip)
        imgNamesStrip = imgNamesStrip[:-4]
        if user_option == '1':
            exec_command = 'bmp2isc.exe'
        else:
            exec_command = 'bmp2oac2.exe'
        exec_command += ' ' + '..\\imagens_para_conversao\\' + imgNamesStrip
        os.chdir(PATH_BMP2)
        os.system(exec_command)
        os.chdir(PATH_IMGS_TO_CONVERT)
        print(img + " convertido com sucesso!")


def save_imgs(img_names, user_option):
    path_save = '\\imagens\\imagens_convertidas'

    if user_option == '1':
        path_type_data = create_dir('arquivos .data', path_save)
        for img in img_names:
            if img.endswith('.data'):
                try:
                    shutil.move(img, path_type_data)
                except Exception as exception:
                    print(exception)

    else:
        path_type_s = create_dir('arquivos .s', path_save)
        path_type_mif = create_dir('arquivos .mif', path_save)
        path_type_bin = create_dir('arquivos .bin', path_save)

        for img in img_names:
            if img.endswith('.s'):
                try:
                    shutil.move(img, path_type_s)
                except Exception as exception:
                    print(exception)
            elif img.endswith('.mif'):
                try:
                    shutil.move(img, path_type_mif)
                except Exception as exception:
                    print(exception)
            elif img.endswith('.bin'):
                try:
                    shutil.move(img, path_type_bin)
                except Exception as exception:
                    print(exception)

    print('Imagens convertidas com sucesso!')
    sleep(2)


def main():
    print_menu()
    user_option = get_input()
    os.chdir(PATH_IMGS_TO_CONVERT)
    convert_imgs(os.listdir(PATH_IMGS_TO_CONVERT), user_option)
    os.chdir(PATH_IMGS)
    if not os.path.isdir('imagens_convertidas'):
        create_dir('imagens_convertidas', '\\imagens\\')
    os.chdir(PATH_IMGS_TO_CONVERT)
    save_imgs(os.listdir(PATH_IMGS_TO_CONVERT), user_option)


if __name__ == "__main__":
    main()
