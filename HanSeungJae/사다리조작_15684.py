def ladder_game(n, m, h):
    links = []
    ns = []
    hs = []
    n_cnt = 0
    h_cnt = 0
    m_cnt = 0

    for _ in range(m):
        link = list(map(int, input().split()))
        links.append(link)

    for i in range(len(links)):
        hs.append(links[i][0])
        ns.append(links[i][1])

        if links[i][1] == links[i-1][1]+1:
            m_cnt += 1

    for i in range(1, n):
        if ns.count(i) % 2:
            n_cnt += 1

    if n_cnt > 3:
        return -1
    
    for i in range(1, h+1):
        if hs.count(i) >= n//2:
            h_cnt += 1

    if (h-h_cnt) < n_cnt:
        return -1

    if m_cnt > h//2:
        return -1


    return n_cnt

    

n, m, h = map(int, input().split())

print(ladder_game(n, m, h))
