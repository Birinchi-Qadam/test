import random

sorov = int(input("Parl uzunligini kiriting:  "))

belgilar = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

natija = "".join(random.sample(belgilar, sorov))

print(natija)