import re
from datetime import datetime

pattern = r'TH_photo'

file_name = "access.log"
date_f = '%d/%b/%Y:%H:%M:%S'
date_from = datetime.strptime('24/Mar/2009:14:39:35', date_f)
date_to = datetime.strptime('25/Mar/2009:11:43:29', date_f)

with open(file_name, 'r') as file:
    count = 0
    for line in file:
        log = re.search('.*((\d\d/Mar/2009:\d\d:\d\d:\d\d).*(2\d\d) (\d+))', str(line))
        if log:
            date = datetime.strptime(log.group(2), date_f)
            if date_from <= date <= date_to:
                find_pattern = re.search(pattern, line)
                if find_pattern is not None:
                    # print(find_pattern.group())
                    print(line)
                    count += 1
    print(f"Count of matches: {count}")
