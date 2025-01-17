def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    energy_required = distance_one_way / meters_per_energy
    if ( energy_required * 2 <= energy_available):
        return True
    else:
        return False
