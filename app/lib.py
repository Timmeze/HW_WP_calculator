def wallpaper_calc(lengh, widgh, heigh, wall_paper):
    """
    >>> wallpaper_calc(5, 6, 2.5, 1.04)
    9

    """
    perimetr_round = 1 # округление значение кол-во полотнищ после деления перимера на ширину полотнища
    reserve_rate = 2 # значение общего запаса обоев
    result = round((((lengh + widgh) * 2 // wall_paper + perimetr_round) / (10 // (heigh + 0.1))) + reserve_rate)
    return result