import os
import requests
import time
import sys

def lan_en(api_key):
    def upload_file_to_virustotal(file_path):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': api_key}

        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files, params=params)

        return response.json()

    def get_report_from_virustotal(resource):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': api_key, 'resource': resource}
        response = requests.get(url, params=params)

        return response.json()

    def analyze_report(report):
        positives = report.get('positives', 0)
        if positives == 0:
            print("No viruses detected.")
        else:
            print(f"{positives} viruses detected:")
            scans = report.get('scans', {})
            for scanner, result in scans.items():
                if result.get('detected'):
                    print(f"- {scanner}: {result.get('result')}")

    def check_and_copy_file():
        folder_name = "Program"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print("Folder 'Program' created. Please move your file into that folder and start the check by typing '1!'")

        while True:
            start = input("Enter '1' to start the check: ")
            if start == "1":
                files = os.listdir(folder_name)
                if len(files) != 1:
                    for file in files:
                        os.remove(os.path.join(folder_name, file))
                    print("Please copy only one file into the folder.")
                else:
                    file_path = os.path.join(folder_name, files[0])
                    file_size = os.path.getsize(file_path) / (1024 * 1024)  # file size in megabytes
                    if file_size > 650:
                        print("File is larger than 650 MB and won't be checked.")
                        os.remove(file_path)
                    else:
                        print(f"File {file_path} is ready for checking.")
                        upload_response = upload_file_to_virustotal(file_path)
                        resource = upload_response['resource']
                        report_response = get_report_from_virustotal(resource)
                        analyze_report(report_response)
                        os.remove(file_path)
            time.sleep(1)

    agreement_file = 'agreement.txt'
    if os.path.exists(agreement_file):
        with open(agreement_file, 'r') as file:
            agreement = file.read().strip()
            if agreement == '1':
                check_and_copy_file()
                return

    print("Have you read the README.txt before using the application?")
    agreement = input("Do you agree? 1 - Agree, 2 - Disagree: ")
    if agreement == '1':
        with open(agreement_file, 'w') as file:
            file.write('1')
        check_and_copy_file()
        return
    elif agreement == '2':
        sys.exit()
    else:
        print("Invalid choice. Please enter 1 or 2.")

def lan_ru(api_key):
    def upload_file_to_virustotal(file_path):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': api_key}

        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files, params=params)

        return response.json()

    def get_report_from_virustotal(resource):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': api_key, 'resource': resource}
        response = requests.get(url, params=params)

        return response.json()

    def analyze_report(report):
        positives = report.get('positives', 0)
        if positives == 0:
            print("Нет обнаруженных вирусов.")
        else:
            print(f"Обнаружено {positives} вирусов:")
            scans = report.get('scans', {})
            for scanner, result in scans.items():
                if result.get('detected'):
                    print(f"- {scanner}: {result.get('result')}")

    def check_and_copy_file():
        folder_name = "Program"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print("Создана папка 'Program'. Пожалуйста, переместите ваш файл в эту папку и начните проверку, набрав '1!'")

        while True:
            start = input("Введите '1' для начала проверки: ")
            if start == "1":
                files = os.listdir(folder_name)
                if len(files) != 1:
                    for file in files:
                        os.remove(os.path.join(folder_name, file))
                    print("Пожалуйста, скопируйте только один файл в папку.")
                else:
                    file_path = os.path.join(folder_name, files[0])
                    file_size = os.path.getsize(file_path) / (1024 * 1024)  # размер файла в мегабайтах
                    if file_size > 650:
                        print("Файл больше 650 МБ и не будет проверяться.")
                        os.remove(file_path)
                    else:
                        print(f"Файл {file_path} готов к проверке.")
                        upload_response = upload_file_to_virustotal(file_path)
                        resource = upload_response['resource']
                        report_response = get_report_from_virustotal(resource)
                        analyze_report(report_response)
                        os.remove(file_path)
            time.sleep(1)

    agreement_file = 'agreement.txt'
    if os.path.exists(agreement_file):
        with open(agreement_file, 'r') as file:
            agreement = file.read().strip()
            if agreement == '1':
                check_and_copy_file()
                return

    print("Прочитали ли вы Readme.txt перед использованием приложения?")
    agreement = input("Вы согласны? 1 - Согласен, 2 - Не согласен: ")
    if agreement == '1':
        with open(agreement_file, 'w') as file:
            file.write('1')
        check_and_copy_file()
        return
    elif agreement == '2':
        sys.exit()
    else:
        print("Неверный выбор. Пожалуйста, введите 1 или 2.")

def select_language():
    api_key = 'Your_api_key'

    selected_language = ''
    if os.path.exists('selected_language.txt'):
        with open('selected_language.txt', 'r') as file:
            selected_language = file.read().strip()

    if selected_language == '1':
        lan_en(api_key)
        return

    elif selected_language == '2':
        lan_ru(api_key)
        return

    else:
        print("Please select a language: ")
        print("1 - English")
        print("2 - Русский")
        choice = input("Enter 1 or 2: ")
        if choice == '1' or choice == '2':
            with open('selected_language.txt', 'w') as file:
                file.write(choice)
            if choice == '1':
                lan_en(api_key)
                return
            elif choice == '2':
                lan_ru(api_key)
                return
        else:
            print("Invalid choice. Please enter 1 or 2.")
