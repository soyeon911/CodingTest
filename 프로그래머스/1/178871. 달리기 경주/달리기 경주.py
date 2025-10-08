def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}
    for name in callings:
        i = rank[name]
        if i == 0:
            continue
    
        temp = players[i - 1]
        players[i - 1] = players[i]
        players[i] = temp

        rank[players[i]] = i
        rank[players[i - 1]] = i - 1

    return players
