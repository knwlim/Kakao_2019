def solution(N, stages):
    answer_tuple = []
    answer = []
    for i in range(1, N+1):
        sum_of_user_reached = sum(element >= i for element in stages)
        if sum_of_user_reached == 0:
            answer.append(0)
        else:
            answer.append(stages.count(i)/sum_of_user_reached)

    for index, failure_rate in enumerate(answer):
        answer_tuple.append((failure_rate, index+1))
        answer_tuple = sorted(answer_tuple, key=lambda item: item[0], reverse=True)
    answer = [i[1] for i in answer_tuple]
    return answer
