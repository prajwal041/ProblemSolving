'''
    Dec  3 00:02:54 Mac Google Chrome Helper[69194]: Couldn't set selectedTextBackgroundColor from default ()
    Dec  3 00:03:05 Mac Safari[68992]: KeychainGetICDPStatus: keychain: -25300
'''
import re
import csv
from collections import defaultdict

def parse_syslog_generate_csv(input_file, output_file):
    minutes_count = defaultdict(int)
    file = open(input_file, 'r')
    lines = file.readlines()
    file.close()

    timestamp_re = re.compile(r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2})')
    for line in lines:
        match = timestamp_re.match(line)
        if match:
            minute = match.group(1)
            minutes_count[minute] += 1
    sorted_minutes = sorted(minutes_count.items(), key=lambda x: x[0])
    print(f"Successfully scraped {input_file}\n{sorted_minutes}")

    file = open(output_file, 'w')
    writer = csv.writer(file)
    writer.writerow(['minute', 'number_of_messages'])
    for minute, count in sorted_minutes:
        writer.writerow([minute, count])
    file.close()
    print(f"Successfully wrote data to {output_file}")

def parse_syslog_generate_programs(input_file, output_file):
    minute_data = defaultdict(lambda : {
        'total': 0,
        'programs': defaultdict(int)
    })
    file = open(input_file, 'r')
    lines = file.readlines()
    file.close()

    program_re = re.compile(r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}):\d{2}\s+\w+\s+([^\[:]+)(?:\[\d+\])?:\s+.*')
    for line in lines:
        match = program_re.match(line)
        if match:
            minute = match.group(1)
            program = match.group(2)
            minute_data[minute]['total'] += 1
            minute_data[minute]['programs'][program] += 1

    all_programs = set()
    for data in minute_data.values():
        all_programs.update(data['programs'].keys())
    all_programs = sorted(all_programs)

    sorted_minutes = sorted(minute_data.items(), key=lambda x:x[0])
    print(f"Successfully scraped {input_file}\n{sorted_minutes}")
    file = open(output_file, 'w')
    writer = csv.writer(file)
    header = ['minute', 'number_of_messages'] + all_programs
    writer.writerow(header)

    for minute, data in sorted_minutes:
        row = [minute, data['total']]
        for program in all_programs:
            row.append(data['programs'].get(program, 0))
        writer.writerow(row)
    print(f"Successfully wrote data to {output_file}")


input_file = 'syslog.txt'
output_file = 'message_counts.csv'
output_file_msg = 'message_counts_program.csv'
parse_syslog_generate_csv(input_file, output_file)
parse_syslog_generate_programs(input_file, output_file_msg)
