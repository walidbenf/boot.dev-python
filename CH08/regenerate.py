def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health:
        if(enemy_distance <= 3):
            break
        current_health+= 1
        enemy_distance = enemy_distance - 2
    return current_health
