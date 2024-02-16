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
    pass

def count_logs_by_level(logs: list) -> dict:
    pass

def display_log_counts(counts: dict):
    pass


def main():
    # if len(sys.argv)<2:
    #     user_input = ''
    # else:
    #     user_input= sys.argv[1] 

    try:
        file_path = Path("logfile.log")

        loglist = load_logs(file_path)
        print(loglist)
    except Exception as e:
        print(e)   

if __name__ == "__main__":

   main()
