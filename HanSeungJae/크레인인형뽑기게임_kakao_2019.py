def solution(board, moves):
    
    def pick(move):
        for i in range(len(board)):
            if board[i][move] != 0:
                stack.append(board[i][move])
                board[i][move] = 0
                return
    
    answer = 0
    stack = []
    
    for i in range(len(moves)):
        move = moves[i] - 1
        pick(move)
        
        if len(stack) > 1 and stack[-2] == stack[-1]:
            for _ in range(2):
                answer += 1
                stack.pop()
    
    return answer