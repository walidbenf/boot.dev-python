def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    alert = "Achievement Unlocked: " + ach_name
    print(alert)
    return after_xp, alert
