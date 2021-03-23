def run ():
    pal = str(input("escribe la palabra ")).replace(' ','').lower()
    revez = pal[::-1]
    if pal == revez:
        print("es un palindromo")
    else:
        print("ni mergas")

if __name__ == '__main__':
    run()
