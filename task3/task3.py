from pathlib import Path
import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    date,time,level,info= line.strip().split(' ',3)
    dict = {"date":date,"time":time,"level":level,"info":info} # Перетворення рядків файлу в словник
    return dict


def load_logs(file_path: str) -> list:
    try:
        with open( file_path,'r',encoding='utf-8') as file: # Зчитуємо файл
            line_list= file.readlines()
            log_list = []

            for line in line_list:
                log_list.append(parse_log_line(line)) # Додавання словарів у список логу
            
            return log_list

    except Exception as e:
        print(e)           


def filter_logs_by_level(logs: list, level: str) -> list:

    filtered_list = list(filter(lambda log:log.get("level").upper()==level.upper(),logs)) # Фільтрування по рівню за допомогою анонімної функції
    return filtered_list

def count_logs_by_level(logs: list) -> dict:
    logs_by_level = Counter(log["level"] for log in logs) # Підрахунок логів по рівню
    return dict(logs_by_level)

def display_log_counts(counts: dict):
    print(' ')
    print("Log level  | Count")
    print("_" * 20)
    print(' ')

    for log, count in counts.items():  # вивід інформації
        print(f"{log:<10} | {count}")


def main():
    
    try:
        if len(sys.argv)<3:
            level = ''
        else:
            level= sys.argv[2] 

        file_path = Path(sys.argv[1])

        loglist = load_logs(file_path)

        counts = count_logs_by_level(loglist)

        display_log_counts(counts)    

        if level:
            filtered_logs = filter_logs_by_level(loglist,level)
            print(' ')
            print(f'Log details for the rank \'{level.upper()}\':')
            print(' ')
            for log in filtered_logs:
                print(f'{log["date"]} {log["time"]} {log["info"]}')

        

    except Exception as e:
        print(e)   

if __name__ == "__main__":

   main()
