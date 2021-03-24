import re


def get_list_from_file(file_name):
    file_list = open(file_name, 'r')
    data = []
    for line_file in file_list:
        data.append(line_file)
    file_list.close()
    return data


file_name_md = 'intervals.md'
file_name_txt = 'source_leetcode_data.txt'

data_list_md = get_list_from_file(file_name_md)
data_list_txt = get_list_from_file(file_name_txt)


file_md = open(file_name_md, 'w')
task_name = re.split(r'\. ', data_list_txt[0])[1].strip()


if len(data_list_md) == 0:
    file_md.write('# ' + re.split(r'\.md', file_name_md)[0])
    file_md.write('\n\n')
    data_list_md.append('+[' + task_name + '](#' + re.sub(r' ', '-', task_name.lower()) + ')\n\n')
else:
    index = 1
    for line in data_list_md:
        index += 1
        if len(re.findall(r'\+', line)) != 0:
            break
    data_list_md.insert(index, '+[' + task_name + '](#' + re.sub(r' ', '-', task_name.lower()) + ')\n\n')

data_list_md.append('## ' + task_name + '\n')
data_list_md.append(data_list_txt[1])
data_list_md.append('```python\n')

for i in range(2, len(data_list_txt)):
    data_list_md.append(data_list_txt[i])

data_list_md.append('\n```\n')

for line in data_list_md:
    file_md.write(line)
file_md.close()



