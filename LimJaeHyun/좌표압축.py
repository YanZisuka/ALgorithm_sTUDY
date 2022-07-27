# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

coordinates_number = int(input())
coordinates = list(map(int, input().split()))
duplicate_coordinates = sorted(list(set(coordinates)))
compression_dict = {}
answer = []

for i in range(len(duplicate_coordinates)):
    compression_dict[duplicate_coordinates[i]] = i

for number in coordinates:
    answer.append(compression_dict[number])

for number in answer:
    print(number, end=' ')

# print(coordinates)
# print(compression_dict)
# print(answer)

