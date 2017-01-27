states = ['changing', 'moving left', 'finished']
state_number = len(states)
stop_states = [2]
alphabet = ['A', 'B', 'C', ' ']
alpha_number = len(alphabet)
shifts = [' S', '<-', '->']

rules = [[(0, 'B', 2), (0, 'C', 2), (0, 'A', 2), (1, ' ', 1)],
         [(1, 'A', 1), (1, 'B', 1), (1, 'C', 1), (2, ' ', 0)]]
lenta = list(' AAAABBCCABC  ');

state = 0
position = 1
print('Начальное состояние каретки:', state, ', позиция', position)
print(position*' ', state, sep='')
print(*lenta, sep='')
while not state in stop_states:
    alpha = lenta[position]
    state, alpha, shift = rules[state][alphabet.index(alpha)]
    lenta[position] = alpha
    if shift == 1:
        position -= 1
    elif shift == 2:
        position += 1
    print(position*' ', state, sep='')
    print(*lenta, sep='')   
