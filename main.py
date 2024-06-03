import argparse
import time

def countdown_timer(total_seconds):
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print('00:00')
    print("Time's up!")

def main():
    parser = argparse.ArgumentParser(description='Countdown Timer')
    parser.add_argument('time', type=str, help='Time in MM:SS format')
    
    args = parser.parse_args()
    
    try:
        mins, secs = map(int, args.time.split(':'))
        total_seconds = mins * 60 + secs
        countdown_timer(total_seconds)
    except ValueError:
        print("Invalid time format. Please use MM:SS format.")

if __name__ == '__main__':
    main()
