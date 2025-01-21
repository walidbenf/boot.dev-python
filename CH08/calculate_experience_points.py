def calculate_experience_points(level):
    xp_multiplier = 0
    if (level == 2):
        return 5
    for i in range(1,level):
        xp_multiplier += 2.5
    total_xp = level * xp_multiplier
    return total_xp
