# harddisk içinden klasörler haline tuttuğum videolar olacak
# her biri farklı bir tam videodan kesilmiş parçalar
# program tüm klasörlerin içinde birer tane video alacak
# gönderilecek videoları böyle sıralamış olacağım 
# bu sayede bir sefer de aynı tip video yollamış olmayacağım



# bir den fazla klasör içinde dosya çekme işin hallet
import os

folder_name = ['1', '2', '3']

# list element of the folders
for folder in folder_name:
    for item in folder:
        print(item)
