import re
from datetime import datetime, timedelta
from collections import defaultdict


log_path = 'C:\\Inbal\\University\\Chemistry Msc Weizmann\\Courses\\Python Course\\day08\\timelog.log'


def parse_time(t):
    return datetime.strptime(t, "%H:%M")

with open(log_path, "r") as f:
    sessions = []
    current_session = []
    for line in f:
        if line[:2].isdigit():
            current_session.append(line.strip())
        else:
            sessions.append(current_session)
            current_session = []
    
full_report = []
total_times = defaultdict(int)

for session in sessions:
    full_report.append(" ")
    times = []
    tasks = []
    for line in session:
        match = re.match(r"(\d{2}:\d{2})\s+(.+)", line)
        if match:
            times.append(parse_time(match.group(1)))
            if match.group(2) == "End":
                break
            tasks.append(match.group(2))

    for i in range(len(tasks)):
        start = times[i]
        if i + 1 < len(times):
            end = times[i+1]
        else:
            end = times[i]
        duration = int((end - start).total_seconds() / 60)
        full_report.append(f"{start.strftime('%H:%M')}-{end.strftime('%H:%M')} {tasks[i]}")
        total_times[tasks[i]] += duration
    

print("\n".join(full_report))

print()

total_duration = sum(total_times.values())

for task, minutes in sorted(total_times.items()):
    percentage = (minutes / total_duration) * 100
    print(f"{task:20} {minutes} minutes {percentage:.0f}%")
