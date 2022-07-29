from pickletools import pyunicode
import pyautogui
import time
import pokemons

cordenadasPokeball = 928,920 
cordenadasTirarPokeball = 936,550  

def sercarPokemons():
    contador = 22
    x_inici = 662
    y_inici = 563
    x_final = 1218
    y_final = 844
    screenshot = pyautogui.screenshot()
    while contador >= 20:
        comensar = x_inici,y_inici
        pixel = screenshot.getpixel(comensar)
        for x in pokemons.pokemon:
            if pixel == x:
                pyautogui.click(comensar)
                time.sleep(6) 
                mirarSiPokemonPetat()    
                mirarSiTocat()
                contador = 10
            if pixel != x:
                x_inici += 1
            if x_inici == x_final:
                x_inici = 662
                y_inici += 1
            if y_inici == y_final:
                mirarSiTocat()
                contador = 10

def mirarSiTocat():
    x = 1155
    y = 126
    blancRA = (255,  255,  255)
    screenshot = pyautogui.screenshot()
    comensar = x,y
    pixel = screenshot.getpixel(comensar)
    if pixel == blancRA:     
        tirarPokeball()
    else:
        mirarSiEsPokeparada()

def mirarSiPokemonPetat():
    x = 1073
    y = 618
    BotoAdimPokes = ( 36, 204, 170)
    screenshot = pyautogui.screenshot()
    comensar = x,y
    pixel = screenshot.getpixel(comensar)
    if pixel == BotoAdimPokes: 
        print("Tranferiendo pokemons...")    
        pyautogui.click(comensar)
        time.sleep(1)
        transferirPokemons()

def mirarSiEsPokeparada():
    contador = 22
    x_inici = 885
    y_inici = 922
    x_final = 998
    y_final = 996
    botoPokeparada = ( 34, 137, 154)
    screenshot = pyautogui.screenshot()
    while contador >= 20:
        comensar = x_inici,y_inici
        pixel = screenshot.getpixel(comensar)
        if pixel == botoPokeparada:
            print("Girando y saliendo de la pokeparada...")
            pyautogui.mouseDown( 760 ,523)
            pyautogui.moveTo(1128 , 504)
            pyautogui.mouseUp()
            time.sleep(0.5)
            pyautogui.click(946,968) 
            contador = 10
        if pixel != botoPokeparada:
            x_inici += 1
        if x_inici == x_final:
            x_inici = 885
            y_inici += 1
        if y_inici == y_final:  
            contador = 10

def tirarPokeball():
    print("Capturando pokemon...")
    pyautogui.mouseDown(cordenadasPokeball) 
    pyautogui.moveTo(cordenadasTirarPokeball)
    pyautogui.mouseUp()   
    time.sleep(18)
    mirarSiAtrapat()

def mirarSiAtrapat():
    contador = 22
    x_inici = 680
    y_inici = 663
    x_final = 1203
    y_final = 795
    botoAtrapat = ( 75, 209, 164)
    screenshot = pyautogui.screenshot()
    while contador >= 20:
        comensar = x_inici,y_inici
        pixel = screenshot.getpixel(comensar)
        if pixel == botoAtrapat:
            print("Pokemon atrapado!!")
            pyautogui.click(comensar)
            time.sleep(5)
            pyautogui.click(940 ,  963) 
            time.sleep(1)
            contador = 10
        if pixel != botoAtrapat:
            x_inici += 1
        if x_inici == x_final:
            x_inici = 680
            y_inici += 1
        if y_inici == y_final:  
            contador = 10    

def mirarSiEstasACamp():
    x = 959
    y = 944
    BotoAdimPokes = (255,  57,  69)
    screenshot = pyautogui.screenshot()
    comensar = x,y
    camp = False
    pixel = screenshot.getpixel(comensar)
    if pixel == BotoAdimPokes: 
        camp = True
        return camp

    return camp    

def SalirDeTodo():
    pyautogui.click(1218, 64)
    time.sleep(0.5)
    pyautogui.click(1218, 64)
    time.sleep(0.5)
    pyautogui.click(1218, 64)
    time.sleep(0.5)
    pyautogui.click(1218, 64)
    time.sleep(0.5)
    pyautogui.click(1900 ,961)
    time.sleep(0.5)
    pyautogui.click(1900 ,961)
    time.sleep(0.5)
    pyautogui.click(1900 ,961)
    time.sleep(0.5)
    pyautogui.click(1900 ,961)
    time.sleep(0.5)
    x = 1060
    y = 537
    BotoAdimPokes = ( 45, 205, 169)
    screenshot = pyautogui.screenshot()
    comensar = x,y
    pixel = screenshot.getpixel(comensar)
    if pixel == BotoAdimPokes: 
        pyautogui.click(1900 ,961)

def transferirPokemons():
    BotoTransferir = 946 , 959
    pokemon1 = 761 , 392
    pokemon2 = 940 , 392
    pokemon3 = 1119 , 392
    pokemon4 = 761 , 577
    pokemon5 = 940 , 577
    pokemon6 = 1119 , 577
    pokemon7 = 761 , 784
    pokemon8 = 940 , 784
    pokemon9 = 1119 , 784
    ubi = [pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,pokemon7,pokemon8,pokemon9]
    for x in ubi:
        pyautogui.mouseDown(x)
        time.sleep(1)
        pyautogui.mouseUp()
    pyautogui.click(BotoTransferir) 
    time.sleep(0.5)
    pyautogui.click(953 ,588)
    time.sleep(0.5)
    pyautogui.click(940 ,961)