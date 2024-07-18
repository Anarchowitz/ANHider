import subprocess, os
print('Blocker activated.')
print('Закройте что бы завершить блокирование')
os.system('title Microsoft Conhost')
if __name__ == '__main__':
    while True:
        tasks = subprocess.getoutput('tasklist').split('\n')[4:]
        for task in tasks:
            if 'lastactivityview.exe' in task.lower() or 'everything.exe' in task.lower() or 'usbdeview.exe' in task.lower() or 'ysteminformer.exe' in task.lower():
                process_name = 'LastActivityView.exe' if 'lastactivityview.exe' in task.lower() else 'Everything.exe' if 'everything.exe' in task.lower() else 'UsbDeview.exe' if 'usbdeview.exe' in task.lower() else 'SystemInformer.exe'
                subprocess.run(['taskkill', '/im', process_name])