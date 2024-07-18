import os, sys, ctypes, requests, time, winreg, subprocess
from SteamPathFinder import get_steam_path, get_app_path, get_game_path

def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
def open_pg(program_path):
                script_dir = os.path.dirname(os.path.abspath(__file__))
                program_path = os.path.join(script_dir, program_path)
                os.startfile(program_path)

class SecurityCheck():
    def __init__(self):
        os.system('cls & title ANSecurity')
        link = 'https://raw.githubusercontent.com/Anarchowitz/ANHider/main/anhider.anhider'
        response = requests.get(link)
        key = response.text.strip()
        answer = input('Введите ключ доступа: ')
        if answer == key:
            MainMenu()
        else:
            os.system('cls')
            print('Неправильный ключ доступа.')
            print('Выход через 5 секунд.')
            time.sleep(5)
            os.system("exit")

class MainMenu():
    def __init__(self):
        os.system('cls & title ANHider')
        print("""
    █     ▀█▄   ▀█▀ ▀██▀  ▀██▀ ▀██▀ ▀██▀▀█▄   ▀██▀▀▀▀█  ▀██▀▀█▄   
   ███     █▀█   █   ██    ██   ██   ██   ██   ██  ▄     ██   ██  
  █  ██    █ ▀█▄ █   ██▀▀▀▀██   ██   ██    ██  ██▀▀█     ██▀▀█▀   
 ▄▀▀▀▀█▄   █   ███   ██    ██   ██   ██    ██  ██        ██   █▄  
▄█▄  ▄██▄ ▄█▄   ▀█  ▄██▄  ▄██▄ ▄██▄ ▄██▄▄▄█▀  ▄██▄▄▄▄▄█ ▄██▄  ▀█▀ 
""")
        os.system('pause & cls')
        print("""
Уважаемый пользователь, выберите пункт из меню, который

              1) Меню очистки.
              2) Меню блокировок.
Нажмите Enter, что бы выйти.
""")
        a = input('Выбранное значение: ')
        if a == '1':
            os.system('cls & title HiderMenu')
            HiderMenu()
        elif a == '2':
            os.system('cls & title BlockMenu')
            BlockMenu()
        else:
            os.system('exit')

class HiderMenu():
    def __init__ (self):
        print("""
 █▄█ █ █▀▄ ██▀ █▄ ▄█ ██▀ █▄ █ █ █
 █ █ █ █▄▀ █▄▄ █ ▀ █ █▄▄ █ ▀█ ▀▄█
                
            1) Запустить батник очистки.
            2) Удалить записи из реестра.
            3) Очистить лог стим аккаунтов.
Нажмите Enter, что бы вернуться назад.
""")
        answer = input('Выбранное значение: ')
        if answer == '1':
            os.system('cls')
            print('Запускаю батник...')
            open_pg('cleaner_first.bat')
            print('Успешно.')
            print('Под этим сообщением инструкция как вернуться назад\n ')
            os.system('pause & cls')
            HiderMenu()
        elif answer == '2':
            os.system('cls')
            print('Начинаю очистку...')
            def delete_registry_key(key, subkey):
                try:
                    reg_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_ALL_ACCESS)
                    winreg.DeleteKey(reg_key, "")
                    winreg.CloseKey(reg_key)
                    print(f"Нужный инструмент: {subkey} успешно удален.")
                except FileNotFoundError:
                    print(f"Нужный инструмент: {subkey} не найден.")
                except Exception as e:
                    print(f"Произошла ошибка при очистке: {e}")
            delete_registry_key(winreg.HKEY_CURRENT_USER, r"Software\Classes\Local Settings\Software\Microsoft\Windows\Shell")
        elif answer == '3':
            os.system('cls')
            print('Пытаюсь найти стим путь..')
            steam_path = get_steam_path()
            print(f'Ваш стим путь -> ({steam_path})')
            print('Пытаюсь очистить логи входов...')
            os.remove(f'{steam_path}/config/loginusers.vdf')
            print('Успешно очистил.')
            print('Перехожу в главное меню...')
            time.sleep(3)
            HiderMenu()
        else:
            MainMenu()

class BlockMenu():
    def __init__(self):
        os.system('cls')
        print("""
 ██▄ █   ▄▀▄ ▄▀▀ █▄▀ █▄ ▄█ ██▀ █▄ █ █ █
 █▄█ █▄▄ ▀▄▀ ▀▄▄ █ █ █ ▀ █ █▄▄ █ ▀█ ▀▄█
            
            1) Заблокировать открытие LastActivity и т.д
            2) Отключить службы
            3) Включить службы
Нажмите Enter, что бы вернуться назад.
""")
        a = input('Выбранное значение: ')
        if a == '1':
            os.system('cls')
            open_pg('Blocker.exe')
            print('Под этим сообщением инструкция как вернуться назад\n ')
            os.system('pause & cls')
            BlockMenu()
        elif a == '2':
            os.system('cls')
            subprocess.run(["sc", "stop", "DusmSvc"])
            subprocess.run(["sc", "config", "DusmSvc", "start=", "disabled"])
            print('Отключил службы.')
            os.system('pause & cls')
            BlockMenu()
        elif a == '3':
            os.system('cls')
            subprocess.run(["sc", "start", "DusmSvc"])
            subprocess.run(["sc", "config", "DusmSvc", "start=", "auto"])
            print('Включил службы.')
            os.system('pause & cls')
            BlockMenu()
        else:
            MainMenu()

if __name__ == '__main__':
    if not is_admin():
        os.system('cls & title ANSecurity')
        print('Пожалуйста, запустите файл от имени администратора.')
        os.system('pause')
    else:
        SecurityCheck()
