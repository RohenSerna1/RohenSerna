def simulate_landslides(mountain_system, thousand_years):
    rows, cols = len(mountain_system), len(mountain_system[0])

    for _ in range(thousand_years):
        new_system = [row[:] for row in mountain_system]
        changed = False

        for r in range(rows):
            for c in range(cols):
                if mountain_system[r][c] == 'X' and c + 1 < cols and mountain_system[r][c + 1] == '-':
                    if r + 1 < rows and mountain_system[r + 1][c + 1] == 'X':
                        new_system[r][c + 1] = 'X'
                        new_system[r][c] = '-'
                        changed = True

        mountain_system = new_system

        if not changed:
            break

    return [''.join(row) for row in mountain_system]

if __name__ == "__main__":
    mountain_system = [
        ['-', '-', '-', '-', '-', 'X', '-'],
        ['-', 'X', '-', 'X', '-', '-', '-'],
        ['X', '-', 'X', '-', '-', 'X', '-'],
        ['-', 'X', '-', 'X', '-', 'X', 'X'],
        ['X', 'X', '-', 'X', '-', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    thousand_years = 6
    result = simulate_landslides(mountain_system, thousand_years)
    
    for row in result:
        print(row)
