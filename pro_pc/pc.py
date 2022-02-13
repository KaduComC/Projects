import platform as pl 

def mostrar_info():
    """Recebe as informações do sistema e as printa no terminal."""
    processador = pl.processor()

    if not processador:
        processador = "Processador não encontrado."

    print(f"- Sistema Operacional: {pl.system()}")
    print(f"- Plataforma do sistema: {pl.platform()}")
    print(f"- Versão do sistema: {pl.version()}")
    print(f"- Processador: {pl}")
    print(f"- Arquitetura do processador: {pl.architecture()[0]}")

    if pl.system() == "Windows":
        print(f"- Edição do Windows: {pl.win32_edition()}")