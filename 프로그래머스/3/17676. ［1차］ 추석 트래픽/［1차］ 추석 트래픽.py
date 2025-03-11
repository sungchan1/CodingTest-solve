from datetime import datetime, timedelta

def solution(lines):
    logs = []
    
    for line in lines:
        date, time, duration = line.split()
        end_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S.%f")
        duration = float(duration.replace("s", ""))
        start_time = end_time - timedelta(seconds=duration - 0.001)  # 처리 시간 포함
        logs.append((start_time, end_time))

    max_requests = 0

    for start_time, end_time in logs:
        window_start = end_time
        window_end = end_time + timedelta(seconds=1)
        count = 0
        for _start, _end in logs:
            if _start < window_end and _end >= window_start:
                count += 1
        max_requests = max(max_requests, count)

    return max_requests
