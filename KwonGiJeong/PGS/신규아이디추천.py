def solution(new_id):
    
    
    #1
    new_id_lower = new_id.lower()
    
    #2
    new_id_list = []
    for new_id_word in new_id_lower:
        if new_id_word.isalpha() or new_id_word.isdigit() or new_id_word in ['-', '_', '.']:
            new_id_list.append(new_id_word)
            
    #3
    new_id_list_one_dot = []
    for new_id_word in new_id_list:
        new_id_list_one_dot.append(new_id_word)
        if len(new_id_list_one_dot) > 1 and new_id_list_one_dot[-1] == '.' and new_id_list_one_dot[-2] == '.':
            new_id_list_one_dot.pop()
    
    #4
    while len(new_id_list_one_dot) > 0 and new_id_list_one_dot[0] == '.':
        del new_id_list_one_dot[0]
    while len(new_id_list_one_dot) > 0 and new_id_list_one_dot[-1] == '.':
        del new_id_list_one_dot[-1]
    
    #5
    if not new_id_list_one_dot:
        new_id_list_one_dot.append('a')
        
    #6
    if len(new_id_list_one_dot) > 16:
        del new_id_list_one_dot[15:-1]
    if len(new_id_list_one_dot) == 16:
        del new_id_list_one_dot[-1]
    while len(new_id_list_one_dot) > 0 and new_id_list_one_dot[-1] == '.':
        del new_id_list_one_dot[-1]
        
    #7
    last_word = new_id_list_one_dot[-1]
    while len(new_id_list_one_dot) < 3:
        new_id_list_one_dot.append(last_word)
    
    answer = ''.join(new_id_list_one_dot)

    return answer