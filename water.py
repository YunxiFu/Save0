def water():
    staus = get_water()
    while staus <= 0.25: # 水分低于25%时浇水
        use_item(Items.Water)
        staus = get_water()
    return 1