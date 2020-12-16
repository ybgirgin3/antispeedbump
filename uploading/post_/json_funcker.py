# filename: json_funcker.py
# tag dictleri
M =  {
    "regular": "#bmw #car #luxury #sports #carsofinstagram #m4 #m3 #m2 #1m #7 #m6 #m8",
    "eski_model": "#bmw #bmw2002 #classical #nostalgia #old #oldcar #2002 #carsofinstagram",
    "7_series": "#bmw #m #7 #The7 #7Series #7series #bmw7 #v12 #v8 #luxury",
    "M8": "#bmw #bmwm8 #m8 #m8competition #v8 #car #carsofinstagram",
    "M6": "#bmw #bmwm6 #m6 #v8 #m6grandcoupe #m6coupe #car #carsofinstagram #twinturbo",
    "M5": "#bmw #bmwm5 #m5 #v8 #m5competition #car #carsofinstagram #twinturbo #m5lci",
    "M4": "#bmw #bmwm4 #m4 #S55 #convertible #m4competition #car #carsofinstagram #twinturbo #m4csl",
    "M3": "#bmw #bmwm3 #m3 #S55 #v8 #e92 #f82 #g20 #m3competition #twinturbo #e46 #m3csl",
    "M2": "#bmw #bmwm2 #m2 #S55 #f87 #turbocharged #twinturbo #m2csl #m3competition #m2csl"
}


X =  {
    "X3": "#bmw #bmwx3 #x3 #x3m #x3mcompetition #S55 #car #carsofinstagram #turbocharged",
    "X5": "#bmw #bmwx5 #x5 #x5m #x5mcompetition #v8 #twinturbo #turbocharged #suv #carsofinstagram",
    "X6": "#bmw #bmwx6 #x6 #x6m #x6mcompetition #v8 #twinturbo #turbocharged #suv #twinturbocharged",
    "X7": "#bmw #bmwx7 #x7 #x7m50i #x7mcompetition #v8 #twinturbo #turbocharged #suv #twinturbocharged"
}


def json_funcker(model):
    sp = model.split(",")
    tag = None
    if sp[1] == 'M':
        if sp[2] in M:
            tag =  M[sp[2]]

    elif sp[1] == 'X':
        if sp[2] in X:
            tag = X[sp[2]]

    # ret = "M", "M6", "white", "#bmwm6"
    ret = sp[1], sp[2], sp[3], tag
    return ret

# end file