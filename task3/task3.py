from pathlib import Path
import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    date,time,level,info= line.strip().split(' ',3)
    dict = {"date":date,"time":time,"level":level,"info":info}
    return dict


def load_logs(file_path: str) -> list:
    try:
        with open( file_path,'r',encoding='utf-8') as file:
            line_list= file.readlines()
            log_list = []

            for line in line_list:
                log_list.append(parse_log_line(line))
            
            return log_list

    except Exception as e:
        print(e)           


def filter_logs_by_level(logs: list, level: str) -> list:

    filtered_list = list(filter(lambda log:log.get("level").upper()==level.upper(),logs))
    return filtered_list

def count_logs_by_level(logs: list) -> dict:
    logs_by_level = Counter(log["level"] for log in logs)
    return dict(logs_by_level)

def display_log_counts(counts: dict):
    print(counts)


def main():
    try:
        file_path = Path("logfile.log")

        loglist = load_logs(file_path)
        # print(loglist)

        if len(sys.argv)<2:
            level = ''
        else:
            level= sys.argv[1] 

        if level:
            filtered_logs = filter_logs_by_level(loglist,level)

        counts = count_logs_by_level(loglist)

        display_log_counts(counts)

    except Exception as e:
        print(e)   

if __name__ == "__main__":

   main()
