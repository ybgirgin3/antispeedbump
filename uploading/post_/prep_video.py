# harddisk içinden klasörler haline tuttuğum videolar olacak
# her biri farklı bir tam videodan kesilmiş parçalar
# program tüm klasörlerin içinde birer tane video alacak
# gönderilecek videoları böyle sıralamış olacağım 
# bu sayede bir sefer de aynı tip video yollamış olmayacağım



# bir den fazla klasör içinde dosya çekme işin hallet
import os
from pprint import pprint
import shutil


def get(folder_name):
    v = {}

    # list element of the folders
    for folder in folder_name:
        for image in os.listdir(folder):
            #item = f"{folder}_{image}"
            #v.append(item)

            # çalışıyor ama neden olduğunu bilmiyorum 
            # folderların içinden rastgele bir tane elemanı dict'e ekliyor
            v[folder] = image

    return v


# dict içinde elemanları taşı
def move(data, mp):
    # data must be a list of target folder names
    files = get(data)
    #print(files)
    #pprint(files.values())
    for i,j in files.items():
        #print(i,j)
        fp = f"{i}/{j}"
        shutil.move(fp, mp)
        print(f'{fp} dosyası taşındı')



#main_path = '/media/berkay/Elements/editlenecek_videolar/'
main_path = '/media/berkay/Elements/editlenecek2/'
path = os.path.join(main_path, 'hazır_videolar/')
move_path = os.path.join(main_path, 'tasinmislar/')
#path = '/home/berkay'

# çalışacak olan komut burası 
cmd = [x for x in os.listdir(path)]
paths = []
for i in cmd:
    paths.append(os.path.join(path, i))

move(paths, move_path)


#move(['1', '2', '3'])
