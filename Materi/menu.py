import os
from time import sleep

from Materi import Logika as l

def refresh():
    menu()

def menu():
    from rich.progress import track
    from rich.markdown import Markdown
    from rich.console import Console
    import time

    ## Menu Table
    menu = ['Algoritma','Fungsi','Himpunan', 'Induksi Matematika', 'Logika','Matrix','Relasi']
    n = 0
    os.system('cls')

    md = Markdown('# Daftar Materi', style='purple')
    console = Console()
    console.print(md)

    for name in menu :
        n += 1
        print(f'{n}. {name}')

    in_menu = input(f'\nPilih Materi 1-{len(menu)} : ')
    choose = int(in_menu)

    if choose == 1:
        pass
    elif choose == 2:
        os.system('cls')
    elif choose == 3:
        os.system('cls')
    elif choose == 4:
        os.system('cls')
    elif choose == 5:
        os.system('cls')
        l.logic_menu()
    elif choose == 6:
        os.system('cls')
    elif choose == 7:
        os.system('cls')
    else:
        print('Pilihan tidak ada dalam materi ^_^\n')
        for i in track(range(3),description='Cooldown. . .'):
            time.sleep(1)
        refresh()        

