def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0
    for i in range (-1, num_attacks):
        if (i == num_attacks):
            total_damage += base_damage * 4
        else:
            total_damage += base_damage * 2
    if (num_attacks == 0):
        return 0
    return total_damage
