# digit_0 = 289_123_456
# digit_1 = 389_123_456
digit_0 = 5
digit_1 = 16
digits_answer = {}
for i in range(digit_0, digit_1 + 1):
    cnt = []
    for j in range(2, 16 + 1):
        if i % j == 0:
            cnt.append(j)
        if len(cnt) == 3:
            answer = max(cnt)
            digits_answer[j] = answer


print(digits_answer)
