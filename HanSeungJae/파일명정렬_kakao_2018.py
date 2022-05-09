def solution(files):
    answer = []
    preprocessings = []
    
    for file in files:
        tmp = []
        for i in range(len(file)):
            if file[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                tmp.append(file[:i])
                file = file[i:]
                break
        for i in range(len(file)):
            if file[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                tmp.append(file[:i])
                file = file[i:]
                break
        tmp.append(file)
        preprocessings.append(tmp)
    
    preprocessings.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    for p in preprocessings:
        answer.append(''.join(p))
        
    return answer





print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))  # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))  # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]