import platform

import pc

print(" Informações do PC ".center(31, "="))

if platform.system():
    pc.mostrar_info()
else:
    print("Não foi possível definir seu sistema!")