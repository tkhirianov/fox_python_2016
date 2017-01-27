states = {'change', 'move', 'finished'}
stop_states = {'finished'}
alphabet = {'A', 'B', 'C', '_'}
shifts = {'S':0, '<-':-1, '->':+1}

rules = {'change' :{'A' :('change', 'B', '->'),
                    'B' :('change', 'C', '->'),
                    'C' :('change', 'A', '->'),
                    '_' :('move',   '_', '<-')},
         'move' :{'A' :('move', 'A', '<-'),
                  'B' :('move', 'B', '<-'),
                  'C' :('move', 'C', '<-'),
                  '_' :('finished', '_', 'S')}}
                   
lenta = list('_AAAABBCCABC__');
state = 'change'
position = 3
print('Начальное состояние каретки:', state, ', позиция', position)
print(position*' ', 'v', (len(lenta) - position)*' ', state, sep='')
print(*lenta, sep='')
while not state in stop_states:
    alpha = lenta[position]
    state, alpha, shift = rules[state][alpha]
    lenta[position] = alpha
    position += shifts[shift]
    print(position*' ', 'v', (len(lenta) - position)*' ', state, sep='')
    print(*lenta, sep='')
