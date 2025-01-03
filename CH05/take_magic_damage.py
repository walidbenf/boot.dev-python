def take_magic_damage(health, resist, amp, spell_power):
    total_max_damage = spell_power * amp
    damage_dealt = total_max_damage - resist
    new_health = health - damage_dealt
    
    return new_health
