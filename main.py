def digit_sum(n):
    if n < 0:
        n = -n 
    return sum(int(digit) for digit in str(n))


def is_accessible(x, y):
    return digit_sum(x) + digit_sum(y) <= 25


def count_accessible_cells(start_x, start_y):
    stack = [(start_x, start_y)]
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    accessible_cells = 0

    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            if is_accessible(x, y):
                accessible_cells += 1
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    stack.append((new_x, new_y))

    return accessible_cells


start_x, start_y = 1000, 1000
result = count_accessible_cells(start_x, start_y)
print("Количество доступных клеток для муравья:", result)
