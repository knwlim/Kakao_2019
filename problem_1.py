def solution(record):
    answer = []
    id_dict = {}
    for item in record:
        one_line = item.split(' ')
        if one_line[0] == 'Enter' or one_line[0] == 'Change':
            id_dict[one_line[1]] = one_line[2]
    for item in record:
        one_line = item.split(' ')
        if one_line[0] != 'Change':
            if one_line[0] == 'Enter':
                answer.append(id_dict[one_line[1]] + '님이 들어왔습니다.')
            elif one_line[0] == 'Leave':
                answer.append(id_dict[one_line[1]] + '님이 나갔습니다.')
    return answer
