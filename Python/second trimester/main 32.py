print("tiket de compra en el super salsa")
print("ingrese artículo 1:")
salsa=input()
print("ingresa precio del artículo 1:")
precio1=(int(input()))

print("ingrese artículo 2:")
masa=input()
print("ingresa precio del artículo 2:")
precio2=(int(input()))

print("ingrese artículo 3:")
boca=input()
print("ingresa precio del artículo 3:")
precio3=(int(input()))

print("ingrese artículo 4:")
sobre=input()
print("ingresa precio del artículo 4:")
precio4=(int(input()))

print("ingrese artículo 5:")
frijol=input()
print("ingresa precio del artículo 5:")
precio5=(int(input()))

suma=(precio1+precio2+precio3+precio4+precio5)
print("sub total:",suma)

iva=(suma*0.16)
print("iva:",iva)

print("total:",suma+iva)
print("gracias por comprar en el super salsa")