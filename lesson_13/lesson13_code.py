#исполнитель алгорифмов Маркова

def read_rules(filename):
    """example of format of file:
        A -> B
        BB -> C. #комментарий к строке
        C ->
        # D -> D --- комментированное правило
        -> A

        возвращает список кортежей (слово, замена, bool), где
            bool -- признак терминальности правила
        """
    rules = []
    file = open(filename)
    for line in file:
        line = line.strip() # убираем лишние пробелы слева и справа
        if line.find('#') != -1:
            line = line[:line.find('#')] # убираем из строки правила комментарий
        if len(line) == 0: # пустые строки просто пропускаем
            continue
        word1, word2 = line.split('->')
        word1 = word1.strip()
        word2 = word2.strip()
        if len(word2) != 0 and word2[-1] == '.':
            rule = (word1, word2[:-1], True) # терминальное правило
        else:
            rule = (word1, word2, False) # не терминальное правило
        rules.append(rule)
    return rules


rules = read_rules('rules1.txt')
s = input()
terminate_rule_found = False
while not terminate_rule_found:
    for rule in rules:
        word, substitute, is_terminator = rule
        if s.find(word) != -1:
            s = s.replace(word, substitute, 1)
            print(s) # распечатка промежуточного результата
            terminate_rule_found = is_terminator
            break #прерываем движение по приоритетам вниз
