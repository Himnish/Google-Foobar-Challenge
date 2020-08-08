def solution(entrances, exits, path):
    # Your code here
    length_entrances = len(entrances)
    length_paths = len(path)
    length_exits = len(exits)
    bunn_count = 0
    inter_paths = path[length_entrances:(length_paths-length_exits)]     # To find all intermediate rooms
    for i in range(length_paths - length_entrances - length_exits):      # Loop through range of length of intermediate rooms
        sum_range = sum(inter_paths[i])                                  # Sum of an intermediate room's possible number of bunnies allowed
        sum_enter = 0                                                    # Sum of bunnies that enter that room
        for j in entrances:
            sum_enter += path[j][length_entrances + i]                   # Get all bunnies that enter a room
        bunn_count += min(sum_enter, sum_range)
    return bunn_count
