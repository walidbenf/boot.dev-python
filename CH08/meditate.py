def meditate(mana, max_mana, energy, energy_drinks):

    for i in range(mana, max_mana):
        if (energy == 0):
            energy+= 50
            energy_drinks = energy_drinks - 1
        energy_drinks 
        mana = mana + 1
        energy  = energy - 1
        if (mana == max_mana or (energy == 0 and energy_drinks == 0)):
            return mana,energy,energy_drinks 
    return mana,energy,energy_drinks
