import math

print('##  Program Python Menghitung Volume Kerucut  ##')
print('==============================================')
print()

jari_jari = float(input('Input jari-jari kerucut: '))
tinggi_kerucut = float(input('Input tinggi kerucut: '))

volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi_kerucut

print('Volume kerucut =', round(volume, 2))
