def check_mount_rental(time_used, time_purchased):
    if ( time_used >= time_purchased):
        return "overtime charged"
    else:
        return "no charges yet"
