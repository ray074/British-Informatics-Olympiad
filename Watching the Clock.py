from datetime import datetime, timedelta

def find_meeting_time(c1, c2):
    time1, time2 = datetime(1, 1, 1, 0, 0, 0), datetime(1, 1, 1, 0, 0, 0)
    interval1, interval2 = timedelta(minutes=60+c1), timedelta(minutes=60+c2)
    time1 += interval1
    time2 += interval2
    
    while time1.time() != time2.time():
        time1 += interval1
        time2 += interval2
    
    str_time = str(time1.time())
    parts = str_time.split(":")
    hrs, mins = parts[:2]
    return f"{hrs}:{mins}"
            
def main():
    c1, c2 = (int(x) for x in input().split())
    print(find_meeting_time(c1, c2))
          
main()