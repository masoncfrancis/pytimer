import argparse
import time
from rich.progress import track

def countdown_timer(total_seconds):
    while track(total_seconds):
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print('00:00')
    print("Time's up!")

def main():
    parser = argparse.ArgumentParser(description='Countdown Timer')
    parser.add_argument('time', type=str, help='Time in MM:SS or SS format')
    
    args = parser.parse_args()
    
    try:
        # Try to split the input by ':'. If it fails, assume it's in seconds.
        if ':' in args.time:
            mins, secs = map(int, args.time.split(':'))
            total_seconds = mins * 60 + secs
        else:
            total_seconds = int(args.time)
        
        countdown_timer(total_seconds)
    except ValueError:
        print("Invalid time format. Please use MM:SS or SS format.")

if __name__ == '__main__':
    main()
