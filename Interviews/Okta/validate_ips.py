import os
import re

from Leetcode.longestPalindrome import get_runtime


def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        nums = int(part)
        if nums < 0 or nums > 255:
            return False
    return True

def get_ips_from_ips(file_path):
    ips = set()
    regex_ip = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                potential_ips = re.findall(regex_ip, line)
                for ip in potential_ips:
                    if is_valid_ip(ip):
                        ips.add(ip)
    except:
        pass
    return ips

@get_runtime
def main():
    devops_dir = '../Okta/devops'
    all_ips = set()

    for root, dir, files in os.walk(devops_dir):
        for file in files:
            file_path = os.path.join(root, file)
            ips = get_ips_from_ips(file_path)
            all_ips.update(ips)
    for ip in sorted(all_ips):
        print(ip)

import time
def get_runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f"Function: {func.__name__} took {runtime} secs")
        return result
    return wrapper


if __name__ == "__main__":
    main()
