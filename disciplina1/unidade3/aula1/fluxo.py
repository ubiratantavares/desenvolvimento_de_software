estaChovendo = True

if estaChovendo:
    print("Fique em casa")

if estaChovendo:
    print("Fique em casa")
else:
    print("Vá brincar")

estaChovendo = False
temSunga = True

if estaChovendo:
    print("Fique em casa")
elif temSunga:
    print("Va para piscina")
else:
    print("Vá brincar")

if estaChovendo:
    print("Fique em casa")
else:
    if temSunga:
        print("Va para piscina")
    else:
        print("Vá brincar")