def dirReduc(arr):
    exclude = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    output = []
    for direction in arr:
        if len(output) and exclude[direction] == output[-1]:
            output.pop()
        else:
            output.append(direction)
    return output