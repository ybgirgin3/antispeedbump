from json import loads
from pprint import pprint


# tag dicts
M =  {
  "M8": "#bmw #bmwm8 #m8 #m8competition #v8 #car #carsofinstagram",
  "M6": "#bmw #bmwm6 #m6 #v8 #m6grandcoupe #m6coupe #car #carsofinstagram #twinturbo",
  "M5": "#bmw #bmwm5 #m5 #v8 #m5competition #car #carsofinstagram #twinturbo #m5lci",
  "M4": "#bmw #bmwm4 #m4 #S55 #convertible #m4competition #car #carsofinstagram #twinturbo #m4csl",
  "M3": "#bmw #bmwm3 #m3 #S55 #v8 #e92 #f82 #g20 #m3competition #twinturbo #m3csl",
  "M2": "#bmw #bmwm2 #m2 #S55 #f87 #turbocharged #twinturbo #m2csl #m3competition #m2csl"
}


X =  {
  "X3": "#bmw #bmwx3 #x3 #x3m #x3mcompetition #S55 #car #carsofinstagram #turbocharged",
  "X5": "#bmw #bmwx5 #x5 #x5m #x5mcompetition #v8 #twinturbo #turbocharged #suv #carsofinstagram",
  "X6": "#bmw #bmwx6 #x6 #x6m #x6mcompetition #v8 #twinturbo #turbocharged #suv #twinturbocharged",
  "X7": "#bmw #bmwx7 #x7 #x7m50i #x7mcompetition #v8 #twinturbo #turbocharged #suv #twinturbocharged"
}



def fucker(model):
    sp = model.split(",")
    tag = None
    if sp[1] == 'M':
        if sp[2] in M:
            tag =  M[sp[2]]

    elif sp[1] == 'X':
        if sp[2] in X:
            tag = X[sp[2]]

    return sp[1], sp[2], sp[3], tag



# bu kısma şuan için dokunulmayacak
pic1 = '1,M,M6,white bmw cok guzel.jpg'
pic2 = 'X X7 black.jpg'

# resim dosyasını adını gördermek yeterli
ret = fucker(pic1)
print(ret)
