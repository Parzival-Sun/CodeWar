def champion_rank_v1(pilot: int, events: str) -> int:
    ranks = []
    event_list = events.split()
    event_len = len(event_list)
    print(event_list)
    if event_len == 0:
        return pilot
    for i in range(1, 21):
        ranks.append(i)
    # for p_idx, e_idx in range(0, event_len, 2), range(1, event_len+1, 2):
    for i in range(0, event_len, 2):
        p_idx = i
        e_idx = i+1
        print(f"p_idx = {p_idx}, e_idx = {e_idx}")
        p = int(event_list[p_idx])
        e = event_list[e_idx]
        if p == pilot and e == 'I':
            return -1
        if e == 'I':
            ranks.remove(p)
        if e == 'O':
            index = ranks.index(p)
            temp = ranks[index-1]
            ranks[index-1] = p
            ranks[index] = temp

    return ranks.index(pilot) + 1


def champion_rank(pilot: int, events: str) -> int:
    ranks = []
    event_list = events.split()
    event_tuple = list(zip(event_list[::2], event_list[1::2]))
    event_len = len(event_list)
    if event_len == 0:
        return pilot
    for i in range(1, 21):
        ranks.append(i)
    for p, e in event_tuple:
        p = int(p)
        if p == pilot and e == 'I':
            return -1
        if e == 'I':
            ranks.remove(p)
        if e == 'O':
            index = ranks.index(p)
            temp = ranks[index-1]
            ranks[index-1] = p
            ranks[index] = temp

    return ranks.index(pilot) + 1


print(champion_rank(3, ""))
print(champion_rank(12, "4 O 3 O"))
print(champion_rank(10, "1 I 10 O 2 I"))
