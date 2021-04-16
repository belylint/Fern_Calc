#conversions
def length():
    print("Length\n")
    print("1. Millimeters        5. Inches")
    print("2. Centimeters        6. Feet")
    print("3. Meters             7. Yards")
    print("4. Kilometers         8. Miles")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Millimeters        5. Inches")
    print("2. Centimeters        6. Feet")
    print("3. Meters             7. Yards")
    print("4. Kilometers         8. Miles")
    t = input("\nAnd what are we converting this to?\n")
    #millimeters
    mm2cm = f * .1
    mm2m = f * .001
    mm2km = f * .000001
    mm2in = f * .03937
    mm2ft = f * .003281
    mm2yd = f * .001094
    mm2mi = f * .000000621
    #centimeters
    cm2mm = f * 10
    cm2m = f * .01
    cm2km = f * .00001
    cm2in = f * .393701
    cm2ft = f * .032808
    cm2yd = f * .010936
    cm2mi = f * .000006
    #meters
    m2mm = f * 1000
    m2cm = f * 100
    m2km = f * .001
    m2in = f * 39.37008
    m2ft = f * 3.28084
    m2yd = f * 1.093613
    m2mi = f * .000621
    #kilometers
    km2mm = f * 1000000
    km2cm = f * 100000
    km2m = f * 1000
    km2in = f * 39370.08
    km2ft = f * 3280.84
    km2yd = f * 1093.613
    km2mi = f * .621371
    #inches
    in2mm = f * 25.4
    in2cm = f * 2.54
    in2m = f * .0254
    in2km = f * .000025
    in2ft = f * .083333
    in2yd = f * .027778
    in2mi = f * .000016
    #feet
    ft2mm = f * 304.8
    ft2cm = f * 30.48
    ft2m = f * .3048
    ft2km = f * .000305
    ft2in = f * 12
    ft2yd = f * .333333
    ft2mi = f * .000189
    #yards
    yd2mm = f * 914.4
    yd2cm = f * 91.44
    yd2m = f * .9144
    yd2km = f * .000914
    yd2in = f * 36
    yd2ft = f * 3
    yd2mi = f * .000568
    #miles
    mi2mm = f * 1609344
    mi2cm = f * 160934.4
    mi2m = f * 1609.344
    mi2km = f * 1.609344
    mi2in = f * 63360
    mi2ft = f * 5280
    mi2yd = f * 1760

    if c == "1" and t == "2":
        print(mm2cm)
    elif c == "1" and t == "3":
        print(mm2m)
    elif c == "1" and t == "4":
        print(mm2km)
    elif c == "1" and t == "5":
        print(mm2in)
    elif c == "1" and t == "6":
        print(mm2ft)
    elif c == "1" and t == "7":
        print(mm2yd)
    elif c == "1" and t == "8":
        print(mm2mi)
    elif c == "2" and t == "1":
        print(cm2mm)
    elif c == "2" and t == "3":
        print(cm2m)
    elif c == "2" and t == "4":
        print(cm2km)
    elif c == "2" and t == "5":
        print(cm2in)
    elif c == "2" and t == "6":
        print(cm2ft)
    elif c == "2" and t == "7":
        print(cm2yd)
    elif c == "2" and t == "8":
        print(cm2mi)
    elif c == "3" and t == "1":
        print(m2mm)
    elif c == "3" and t == "2":
        print(m2cm)
    elif c == "3" and t == "4":
        print(m2km)
    elif c == "3" and t == "5":
        print(m2in)
    elif c == "3" and t == "6":
        print(m2ft)
    elif c == "3" and t == "7":
        print(m2yd)
    elif c == "3" and t == "8":
        print(m2mi)
    elif c == "4" and t == "1":
        print(km2mm)
    elif c == "4" and t == "2":
        print(km2cm)
    elif c == "4" and t == "3":
        print(km2m)
    elif c == "4" and t == "5":
        print(km2in)
    elif c == "4" and t == "6":
        print(km2ft)
    elif c == "4" and t == "7":
        print(km2yd)
    elif c == "4" and t == "8":
        print(km2mi)
    elif c == "5" and t == "1":
        print(in2mm)
    elif c == "5" and t == "2":
        print(in2cm)
    elif c == "5" and t == "3":
        print(in2m)
    elif c == "5" and t == "4":
        print(in2km)
    elif c == "5" and t == "6":
        print(in2ft)
    elif c == "5" and t == "7":
        print(in2yd)
    elif c == "5" and t == "8":
        print(in2mi)
    elif c == "6" and t == "1":
        print(ft2mm)
    elif c == "6" and t == "2":
        print(ft2cm)
    elif c == "6" and t == "3":
        print(ft2m)
    elif c == "6" and t == "4":
        print(ft2km)
    elif c == "6" and t == "5":
        print(ft2in)
    elif c == "6" and t == "7":
        print(ft2yd)
    elif c == "6" and t == "8":
        print(ft2mi)
    elif c == "7" and t == "1":
        print(yd2mm)
    elif c == "7" and t == "2":
        print(yd2cm)
    elif c == "7" and t == "3":
        print(yd2m)
    elif c == "7" and t == "4":
        print(yd2km)
    elif c == "7" and t == "5":
        print(yd2in)
    elif c == "7" and t == "6":
        print(yd2ft)
    elif c == "7" and t == "8":
        print(yd2mi)
    elif c == "8" and t == "1":
        print(mi2mm)
    elif c == "8" and t == "2":
        print(mi2cm)
    elif c == "8" and t == "3":
        print(mi2m)
    elif c == "8" and t == "4":
        print(mi2km)
    elif c == "8" and t == "5":
        print(mi2in)
    elif c == "8" and t == "6":
        print(mi2ft)
    elif c == "8" and t == "7":
        print(mi2yd)
def area():
    print("Area\n")
    print("1. Millimeters        4. Inches")
    print("2. Centimeters        5. Feet")
    print("3. Meters             6. Yards")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Millimeters        4. Inches")
    print("2. Centimeters        5. Feet")
    print("3. Meters             6. Yards")
    t = input("\nAnd what are we converting this to?\n")
    #millimeters
    mm2cm = f * 0.01
    mm2m = f * 0.000001
    mm2in = f * 0.00155
    mm2ft = f * 0.000011
    mm2yd = f * 0.000001
    #centimeters
    cm2mm = f * 100
    cm2m = f * 0.0001
    cm2in = f * 0.155
    cm2ft = f * 0.001076
    cm2yd = f * 0.00012
    #meters
    m2mm = f * 1000000
    m2cm = f * 10000
    m2in = f * 1550.003
    m2ft = f * 10.76391
    m2yd = f * 1.19599
    #inches
    in2mm = f * 645.16
    in2cm = f * 6.4516
    in2m = f * 0.000645
    in2ft = f * 0.006944
    in2yd = f * 0.000772
    #feet
    ft2mm = f * 92903
    ft2cm = f * 929.0304
    ft2m = f * 0.092903
    ft2in = f * 144
    ft2yd = f * 0.111111
    #yards
    yd2mm = f * 836127
    yd2cm = f * 8361.274
    yd2m = f * 0.836127
    yd2in = f * 1296
    yd2ft = f * 9

    if c == "1" and t == "2":
        print(mm2cm)
    elif c == "1" and t == "3":
        print(mm2m)
    elif c == "1" and t == "4":
        print(mm2in)
    elif c == "1" and t == "5":
        print(mm2ft)
    elif c == "1" and t == "6":
        print(mm2yd)
    elif c == "2" and t == "1":
        print(cm2mm)
    elif c == "2" and t == "3":
        print(cm2m)
    elif c == "2" and t == "4":
        print(cm2in)
    elif c == "2" and t == "5":
        print(cm2ft)
    elif c == "2" and t == "6":
        print(cm2yd)
    elif c == "3" and t == "1":
        print(m2mm)
    elif c == "3" and t == "2":
        print(m2cm)
    elif c == "3" and t == "4":
        print(m2in)
    elif c == "3" and t == "5":
        print(m2ft)
    elif c == "3" and t == "6":
        print(m2yd)
    elif c == "4" and t == "1":
        print(in2mm)
    elif c == "4" and t == "2":
        print(in2cm)
    elif c == "4" and t == "3":
        print(in2m)
    elif c == "4" and t == "5":
        print(in2ft)
    elif c == "4" and t == "6":
        print(in2yd)
    elif c == "5" and t == "1":
        print(ft2mm)
    elif c == "5" and t == "2":
        print(ft2cm)
    elif c == "5" and t == "3":
        print(ft2m)
    elif c == "5" and t == "4":
        print(ft2in)
    elif c == "5" and t == "6":
        print(ft2yd)
    elif c == "6" and t == "1":
        print(yd2mm)
    elif c == "6" and t == "2":
        print(yd2cm)
    elif c == "6" and t == "3":
        print(yd2m)
    elif c == "6" and t == "4":
        print(yd2in)
    elif c == "6" and t == "5":
        print(yd2ft)
def volume():
    print("Volume\n")
    print("1. Centimeters    5. Feet")
    print("2. Meters         6. US Gallons")
    print("3. Liters         7. Imperial Gallons")
    print("4. Inches         8. US Barrel (Oil) ")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Centimeters    5. Feet")
    print("2. Meters         6. US Gallons")
    print("3. Liters         7. Imperial Gallons")
    print("4. Inches         8. US Barrel (Oil) ")
    t = input("\nAnd what are we converting this to?\n")
    #centimeters
    cm2m = f * 0.000001
    cm2ltr = f * 0.001
    cm2in = f * 0.061024
    cm2ft = f * 0.000035
    cm2usgal = f * 0.000264
    cm2impgal = f * 0.00022
    cm2usbrl = f * 0.000006
    #meters
    m2cm = f * 1000000
    m2ltr = f * 1000
    m2in = f * 61024
    m2ft = f * 35
    m2usgal = f * 264
    m2impgal = f * 220
    m2usbrl = f * 6.29
    #liter
    ltr2cm = f * 1000
    ltr2m = f * 0.001
    ltr2in = f * 61
    ltr2ft = f * 0.035
    ltr2usgal = f * 0.264201
    ltr2impgal = f * 0.22
    ltr2usbrl = f * 0.00629
    #inches
    in2cm = f * 16.4
    in2m = f * 0.000016
    in2ltr = f * 0.016387
    in2ft = f * 0.000579
    in2usgal = f * 0.004329
    in2impgal = f * 0.003605
    in2usbrl = f * 0.000103
    #feet
    ft2cm = f * 28317
    ft2m = f * 0.028317
    ft2ltr = f * 28.31685
    ft2in = f * 1728
    ft2usgal = f * 7.481333
    ft2impgal = f * 6.229712
    ft2usbrl = f * 0.178127
    #us gallons
    usgal2cm = f * 3785
    usgal2m = f * 0.003785
    usgal2ltr = f * 3.79
    usgal2in = f * 231
    usgal2ft = f * 0.13
    usgal2impgal = f * 0.832701
    usgal2usbrl = f * 0.02381
    #imperial gallons
    impgal2cm = f * 4545
    impgal2m = f * 0.004545
    impgal2ltr = f * 4.55
    impgal2in = f * 277
    impgal2ft = f * 0.16
    impgal2usgal = f * 1.20
    impgal2usbrl = f * 0.028593
    #us barrel (oil)
    usbrl2cm = f * 158970
    usbrl2m = f * 0.15897
    usbrl2ltr = f * 159
    usbrl2in = f * 9701
    usbrl2ft = f * 6
    usbrl2usgal = f * 42
    usbrl2impgal = f * 35

    if c == "1" and t == "2":
        print(cm2m)
    elif c == "1" and t == "3":
        print(cm2ltr)
    elif c == "1" and t == "4":
        print(cm2in)
    elif c == "1" and t == "5":
        print(cm2ft)
    elif c == "1" and t == "6":
        print(cm2usgal)
    elif c == "1" and t == "7":
        print(cm2impgal)
    elif c == "1" and t == "8":
        print(cm2usbrl)
    elif c == "2" and t == "1":
        print(m2cm)
    elif c == "2" and t == "3":
        print(m2ltr)
    elif c == "2" and t == "4":
        print(m2in)
    elif c == "2" and t == "5":
        print(m2ft)
    elif c == "2" and t == "6":
        print(m2usgal)
    elif c == "2" and t == "7":
        print(m2impgal)
    elif c == "2" and t == "8":
        print(m2usbrl)
    elif c == "3" and t == "1":
        print(ltr2cm)
    elif c == "3" and t == "2":
        print(ltr2m)
    elif c == "3" and t == "4":
        print(ltr2in)
    elif c == "3" and t == "5":
        print(ltr2ft)
    elif c == "3" and t == "6":
        print(ltr2usgal)
    elif c == "3" and t == "7":
        print(ltr2impgal)
    elif c == "3" and t == "8":
        print(ltr2usbrl)
    elif c == "4" and t == "1":
        print(in2cm)
    elif c == "4" and t == "2":
        print(in2m)
    elif c == "4" and t == "3":
        print(in2ltr)
    elif c == "4" and t == "5":
        print(in2ft)
    elif c == "4" and t == "6":
        print(in2usgal)
    elif c == "4" and t == "7":
        print(in2impgal)
    elif c == "4" and t == "8":
        print(in2usbrl)
    elif c == "5" and t == "1":
        print(ft2cm)
    elif c == "5" and t == "2":
        print(ft2m)
    elif c == "5" and t == "3":
        print(ft2ltr)
    elif c == "5" and t == "4":
        print(ft2in)
    elif c == "5" and t == "6":
        print(ft2usgal)
    elif c == "5" and t == "7":
        print(ft2impgal)
    elif c == "5" and t == "8":
        print(ft2usbrl)
    elif c == "6" and t == "1":
        print(usgal2cm)
    elif c == "6" and t == "2":
        print(usgal2m)
    elif c == "6" and t == "3":
        print(usgal2ltr)
    elif c == "6" and t == "4":
        print(usgal2in)
    elif c == "6" and t == "5":
        print(usgal2ft)
    elif c == "6" and t == "7":
        print(usgal2impgal)
    elif c == "6" and t == "8":
        print(usgal2usbrl)
    elif c == "7" and t == "1":
        print(impgal2cm)
    elif c == "7" and t == "2":
        print(impgal2m)
    elif c == "7" and t == "3":
        print(impgal2ltr)
    elif c == "7" and t == "4":
        print(impgal2in)
    elif c == "7" and t == "5":
        print(impgal2ft)
    elif c == "7" and t == "6":
        print(impgal2usgal)
    elif c == "7" and t == "8":
        print(impgal2usbrl)
    elif c == "8" and t == "1":
        print(usbrl2cm)
    elif c == "8" and t == "2":
        print(usbrl2m)
    elif c == "8" and t == "3":
        print(usbrl2ltr)
    elif c == "8" and t == "4":
        print(usbrl2in)
    elif c == "8" and t == "5":
        print(usbrl2ft)
    elif c == "8" and t == "6":
        print(usbrl2usgal)
    elif c == "8" and t == "7":
        print(usbrl2impgal)
def mass():
    print("Mass\n")
    print("1. Grams             5. Long Ton")
    print("2. Kilograms         6. Pounds")
    print("3. Metric Tonnes     7. Ounces")
    print("4. Short Ton ")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Grams             5. Long Ton")
    print("2. Kilograms         6. Pounds")
    print("3. Metric Tonnes     7. Ounces")
    print("4. Short Ton ")
    t = input("\nAnd what are we converting this to?\n")
    #grams
    g2kg = f * 0.001
    g2tonne = f * 0.000001
    g2shton = f * 0.000001
    g2lton = f * 9.84e-07
    g2lb = f * 0.002205
    g2oz = f * 0.035273
    #kilograms
    kg2g = f * 1000
    kg2tonne = f * 0.001
    kg2shton = f * 0.001102
    kg2lton = f * 0.000984
    kg2lb = f * 2.204586
    kg2oz = f * 35.27337
    #metric tonnes
    tonne2g = f * 1000000
    tonne2kg = f * 1000
    tonne2shton = f * 1.102293
    tonne2lton = f * 0.984252
    tonne2lb = f * 2204.586
    tonne2oz = f * 35273.37
    #short ton
    shton2g = f * 907200
    shton2kg = f * 907.2
    shton2tonne = f * 0.9072
    shton2lton = f * 0.892913
    shton2lb = f * 2000
    shton2oz = f * 32000
    #long ton
    lton2g = f * 1016000
    lton2kg = f * 1016
    lton2tonne = f * 1.016
    lton2shton = f * 1.119929
    lton2lb = f * 2239.859
    lton2oz = f * 35837.74
    #pounds
    lb2g = f * 453.6
    lb2kg = f * 0.4536
    lb2tonne = f * 0.000454
    lb2shton = f * 0.0005
    lb2lton = f * 0.000446
    lb2oz = f * 16
    #ounces
    oz2g = f * 28
    oz2kg = f * 0.02835
    oz2tonne = f * 0.000028
    oz2shton = f * 0.000031
    oz2lton = f * 0.000028
    oz2lb = f * 0.0625
    #work
    if c == "1" and t == "2":
        print(g2kg)
    elif c == "1" and t == "3":
        print(g2tonne)
    elif c == "1" and t == "4":
        print(g2shton)
    elif c == "1" and t == "5":
        print(g2lton)
    elif c == "1" and t == "6":
        print(g2lb)
    elif c == "1" and t == "7":
        print(g2oz)
    elif c == "2" and t == "1":
        print(kg2g)
    elif c == "2" and t == "3":
        print(kg2tonne)
    elif c == "2" and t == "4":
        print(kg2shton)
    elif c == "2" and t == "5":
        print(kg2lton)
    elif c == "2" and t == "6":
        print(kg2lb)
    elif c == "2" and t == "7":
        print(kg2oz)
    elif c == "3" and t == "1":
        print(tonne2g)
    elif c == "3" and t == "2":
        print(tonne2kg)
    elif c == "3" and t == "4":
        print(tonne2shton)
    elif c == "3" and t == "5":
        print(tonne2lton)
    elif c == "3" and t == "6":
        print(tonne2lb)
    elif c == "3" and t == "7":
        print(tonne2oz)
    elif c == "4" and t == "1":
        print(shton2g)
    elif c == "4" and t == "2":
        print(shton2kg)
    elif c == "4" and t == "3":
        print(shton2tonne)
    elif c == "4" and t == "5":
        print(shton2lton)
    elif c == "4" and t == "6":
        print(shton2lb)
    elif c == "4" and t == "7":
        print(shton2oz)
    elif c == "5" and t == "1":
        print(lton2g)
    elif c == "5" and t == "2":
        print(lton2kg)
    elif c == "5" and t == "3":
        print(lton2tonne)
    elif c == "5" and t == "4":
        print(lton2shton)
    elif c == "5" and t == "6":
        print(lton2lb)
    elif c == "5" and t == "7":
        print(lton2oz)
    elif c == "6" and t == "1":
        print(lb2g)
    elif c == "6" and t == "2":
        print(lb2kg)
    elif c == "6" and t == "3":
        print(lb2tonne)
    elif c == "6" and t == "4":
        print(lb2shton)
    elif c == "6" and t == "5":
        print(lb2lton)
    elif c == "6" and t == "7":
        print(lb2oz)
    elif c == "7" and t == "1":
        print(oz2g)
    elif c == "7" and t == "2":
        print(oz2kg)
    elif c == "7" and t == "3":
        print(oz2tonne)
    elif c == "7" and t == "4":
        print(oz2shton)
    elif c == "7" and t == "5":
        print(oz2lton)
    elif c == "7" and t == "6":
        print(oz2lb)
def density():
    print("Density\n")
    print("1. Gram/ml        3. Pound/Foot")
    print("2. kg/meter       4. Pound/Inch")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Gram/ml        3. Pound/Foot")
    print("2. kg/meter       4. Pound/Inch")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        g2kg_m = f * 1000
        print(g2kg_m)
    elif c == "1" and t == "3":
        g2lb_ft = f * 62.42197
        print(g2lb_ft)
    elif c == "1" and t == "4":
        g2lb_in = f * 0.036127
        print(g2lb_in)
    elif c == "2" and t == "1":
        kg2g_ml = f * 0.001
        print(kg2g_ml)
    elif c == "2" and t == "3":
        kg2lb_ft = f * 0.062422
        print(kg2lb_ft)
    elif c == "2" and t == "4":
        kg2lb_in = f * 0.000036
        print(kg2lb_in)
    elif c == "3" and t == "1":
        lb_ft2g_ml = f * 0.01602
        print(lb_ft2g_ml)
    elif c == "3" and t == "2":
        lb_ft2kg_m = f * 16.02
        print(lb_ft2kg_m)
    elif c == "3" and t == "4":
        lb_ft2lb_in = f * 0.000579
        print(lb_ft2lb_in)
    elif c == "4" and t == "1":
        lb_in2g_ml = f * 27.68
        print(lb_in2g_ml)
    elif c == "4" and t == "2":
        lb_in2kg_m = f * 27680
        print(lb_in2kg_m)
    elif c == "4" and t == "3":
        lb_in2lb_ft = f * 1727.84
        print(lb_in2lb_ft)
def liquidflow():
    print("Liquid Flow\n")
    print("1. Litter/Second         5. Foot/Hour")
    print("2. Litter/minute         6. US Gallon/Minute")
    print("3. Meter/Hour            7. US Barrel Daily")
    print("4. Foot/Minute ")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Litter/Second         5. Foot/Hour")
    print("2. Litter/minute         6. US Gallon/Minute")
    print("3. Meter/Hour            7. US Barrel Daily")
    print("4. Foot/Minute ")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        ltrs2ltrm = f * 60
        print(ltrs2ltrm)
    elif c == "1" and t == "3":
        ltrs2mh = f * 3.6
        print(ltrs2mh)
    elif c == "1" and t == "4":
        ltrs2ftm = f * 2.119093
        print(ltrs2ftm)
    elif c == "1" and t == "5":
        ltrs2fth = f * 127.1197
        print(ltrs2fth)
    elif c == "1" and t == "6":
        ltrs2galm = f * 15.85037
        print(ltrs2galm)
    elif c == "1" and t == "7":
        ltrs2usbrld = f * 543.4783
        print(ltrs2usbrld)
    elif c == "2" and t == "1":
        ltrm2ltrs = f * 0.016666
        print(ltrm2ltrs)
    elif c == "2" and t == "3":
        ltrm2mh = f * 0.06
        print(ltrm2mh)
    elif c == "2" and t == "4":
        ltrm2ftm = f * 0.035317
        print(ltrm2ftm)
    elif c == "2" and t == "5":
        ltrm2fth = f* 2.118577
        print(ltrm2fth)
    elif c == "2" and t == "6":
        ltrm2galm = f * 0.264162
        print(ltrm2galm)
    elif c == "2" and t == "7":
        ltrm2usbrld = f * 9.057609
        print(ltrm2usbrld)
    elif c == "3" and t == "1":
        mh2ltrs = f * 0.277778
        print(mh2ltrs)
    elif c == "3" and t == "2":
        mh2ltrm = f * 16.6667
        print(mh2ltrm)
    elif c == "3" and t == "4":
        mh2ftm = f * 0.588637
        print(mh2ftm)
    elif c == "3" and t == "5":
        mh2fth = f * 35.31102
        print(mh2fth)
    elif c == "3" and t == "6":
        mh2galm = f * 4.40288
        print(mh2galm)
    elif c == "3" and t == "7":
        mh2usbrld = f * 150.9661
        print(mh2usbrld)
    elif c == "4" and t == "1":
        ftm2ltrs = f * 0.4719
        print(ftm2ltrs)
    elif c == "4" and t == "2":
        ftm2ltrm = f * 28.31513
        print(ftm2ltrm)
    elif c == "4" and t == "3":
        ftm2mh = f * 1.69884
        print(ftm2mh)
    elif c == "4" and t == "5":
        ftm2fth = f * 60
        print(ftm2fth)
    elif c == "4" and t == "6":
        ftm2galm = f * 7.479791
        print(ftm2galm)
    elif c == "4" and t == "7":
        ftm2usbrld = f * 256.4674
        print(ftm2usbrld)
    elif c == "5" and t == "1":
        fth2ltrs = f * 0.007867
        print(fth2ltrs)
    elif c == "5" and t == "2":
        fth2ltrm = f * 0.472015
        print(fth2ltrm)
    elif c == "5" and t == "3":
        fth2mh = f * 0.02832
        print(fth2mh)
    elif c == "5" and t == "4":
        fth2ftm = f * 0.01667
        print(fth2ftm)
    elif c == "5" and t == "6":
        fth2galm = f * 0.124689
        print(fth2galm)
    elif c == "5" and t == "7":
        fth2usbrld = f * 4.275326
        print(fth2usbrld)
    elif c == "6" and t == "1":
        galm2ltrs = f * 0.06309
        print(galm2ltrs)
    elif c == "6" and t == "2":
        galm2ltrm = f * 3.785551
        print(galm2ltrm)
    elif c == "6" and t == "3":
        galm2mh = f * 0.227124
        print(galm2mh)
    elif c == "6" and t == "4":
        galm2ftm = f * 0.133694
        print(galm2ftm)
    elif c == "6" and t == "5":
        galm2fth = f * 8.019983
        print(galm2fth)
    elif c == "6" and t == "7":
        galm2usbrld = f * 34.28804
        print(galm2usbrld)
    elif c == "7" and t == "1":
        usbrld2ltrs = f * 0.00184
        print(usbrld2ltrs)
    elif c == "7" and t == "2":
        usbrld2ltrm = f * 0.110404
        print(usbrld2ltrm)
    elif c == "7" and t == "3":
        usbrld2mh = f * 0.006624
        print(usbrld2mh)
    elif c == "7" and t == "4":
        usbrld2ftm = f * 0.003899
        print(usbrld2ftm)
    elif c == "7" and t == "5":
        usbrld2fth = f * 0.2339
        print(usbrld2fth)
    elif c == "7" and t == "6":
        usbrld2galm = f * 0.029165
        print(usbrld2galm)
def gasflow():
    print("Gas Flow\n")
    print("1. Normal Meter Cube/Hour")
    print("2. Standard Cubic Feet/hour")
    print("3. Standard Cubic Feet/Minute")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Normal Meter Cube/Hour")
    print("2. Standard Cubic Feet/hour")
    print("3. Standard Cubic Feet/Minute")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        nm2scfh = f * 35.31073
        print(nm2scfh)
    elif c == "1" and t == "3":
        nm2scfm = f * 0.588582
        print(nm2scfm)
    elif c == "2" and t == "1":
        scfh2nm = f * 0.02832
        print(scfh2nm)
    elif c == "2" and t == "3":
        scfh2scfm = f * 0.016669
        print(scfh2scfm)
    elif c == "3" and t == "1":
        scfm2nm = f * 1.699
        print(scfm2nm)
    elif c == "3" and t == "2":
        scfm2scfh = f * 59.99294
        print(scfm2scfh)
def massflow():
    print("Mass Flow\n")
    print("1. Kilogram/Hour        3. Kilogram/Second")
    print("2. Pound/Hour           4. Ton/Hour")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Kilogram/Hour        3. Kilogram/Second")
    print("2. Pound/Hour           4. Ton/Hour")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        kgh2lb = f * 2.204586
        print(kgh2lb)
    elif c == "1" and t == "3":
        kgh2kgs = f * 0.000278
        print(kgh2kgs)
    elif c == "1" and t == "4":
        kgh2th = f * 0.001
        print(kgh2th)
    elif c == "2" and t == "1":
        lb2kgh = f * 0.4536
        print(lb2kgh)
    elif c == "2" and t == "3":
        lb2kgs = f * 0.000126
        print(lb2kgs)
    elif c == "2" and t == "4":
        lb2th = f * 0.000454
        print(lb2th)
    elif c == "3" and t == "1":
        kgs2kgh = f * 3600
        print(kgs2kgh)
    elif c == "3" and t == "2":
        kgs2lb = f * 27936.508
        print(kgs2lb)
    elif c == "3" and t == "4":
        kgs2th = f * 3.6
        print(kgs2th)
    elif c == "4" and t == "1":
        th2kgh = f * 1000
        print(th2kgh)
    elif c == "4" and t == "2":
        th2lb = f * 2204.586
        print(th2lb)
    elif c == "4" and t == "3":
        th2kgs = f * 0.277778
        print(th2kgs)
def highpressure():
    print("High Pressure\n")
    print("1. Bar                5. Kilogram Force/Centimeter Square")
    print("2. PSI                6. Millimeter of Mercury")
    print("3. Kilopascal         7. Atmospheres")
    print("4. Magapascal ")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Bar                5. Kilogram Force/Centimeter Square")
    print("2. PSI                6. Millimeter of Mercury")
    print("3. Kilopascal         7. Atmospheres")
    print("4. Magapascal ")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        bar2psi = f * 14.50326
        print(bar2psi)
    elif c == "1" and t == "3":
        bar2kpa = f * 100
        print(bar2kpa)
    elif c == "1" and t == "4":
        bar2mpa = f * 0.1
        print(bar2mpa)
    elif c == "1" and t == "5":
        bar2kgf = f * 1.01968
        print(bar2kgf)
    elif c == "1" and t == "6":
        bar2mm = f * 750.0188
        print(bar2mm)
    elif c == "1" and t == "7":
        bar2atm = f * 0.987167
        print(bar2atm)
    elif c == "2" and t == "1":
        psi2bar = f * 0.06895
        print(psi2bar)
    elif c == "2" and t == "3":
        psi2kpa = f * 6.895
        print(psi2kpa)
    elif c == "2" and t == "4":
        psi2mpa = f * 0.006895
        print(psi2mpa)
    elif c == "2" and t == "5":
        psi2kgf = f * 0.070307
        print(psi2kgf)
    elif c == "2" and t == "6":
        psi2mm = f * 51.71379
        print(psi2mm)
    elif c == "2" and t == "7":
        psi2atm = f * 0.068065
        print(psi2atm)
    elif c == "3" and t == "1":
        kpa2bar = f * 0.01
        print(kpa2bar)
    elif c == "3" and t == "2":
        kpa2psi = f * 0.1450
        print(kpa2psi)
    elif c == "3" and t == "4":
        kpa2mpa = f * 0.001
        print(kpa2mpa)
    elif c == "3" and t == "5":
        kpa2kgf = f * 0.01020
        print(kpa2kgf)
    elif c == "3" and t == "6":
        kpa2mm = f * 7.5002
        print(kpa2mm)
    elif c == "3" and t == "7":
        kpa2atm = f * 0.00987
        print(kpa2atm)
    elif c == "4" and t == "1":
        mpa2bar = f * 10
        print(mpa2bar)
    elif c == "4" and t == "2":
        mpa2psi = f * 145.03
        print(mpa2psi)
    elif c == "4" and t == "3":
        mpa2kpa = f * 1000
        print(mpa2kpa)
    elif c == "4" and t == "5":
        mpa2kgf = f * 10.197
        print(mpa2kgf)
    elif c == "4" and t == "6":
        mpa2mm = f * 7500.2
        print(mpa2mm)
    elif c == "4" and t == "7":
        mpa2atm = f * 9.8717
        print(mpa2atm)
    elif c == "5" and t == "1":
        kgf2bar = f * 0.9807
        print(kgf2bar)
    elif c == "5" and t == "2":
        kgf2psi = f * 14.22335
        print(kgf2psi)
    elif c == "5" and t == "3":
        kgf2kpa = f * 98.07
        print(kgf2kpa)
    elif c == "5" and t == "4":
        kgf2mpa = f * 0.09807
        print(kgf2mpa)
    elif c == "5" and t == "6":
        kgf2mm = f * 735.5434
        print(kgf2mm)
    elif c == "5" and t == "7":
        kgf2atm = f * 0.968115
        print(kgf2atm)
    elif c == "6" and t == "1":
        mm2bar = f * 0.001333
        print(mm2bar)
    elif c == "6" and t == "2":
        mm2psi = f * 0.019337
        print(mm2psi)
    elif c == "6" and t == "3":
        mm2kpa = f * 0.13333
        print(mm2kpa)
    elif c == "6" and t == "4":
        mm2mpa = f * 0.000133
        print(mm2mpa)
    elif c == "6" and t == "5":
        mm2kfg = f * 0.00136
        print(mm2kfg)
    elif c == "6" and t == "7":
        mm2atm = f * 0.001316
        print(mm2atm)
    elif c == "7" and t == "1":
        atm2bar = f * 1.013
        print(atm2bar)
    elif c == "7" and t == "2":
        atm2psi = f * 14.69181
        print(atm2psi)
    elif c == "7" and t == "3":
        atm2kpa = f * 101.3
        print(atm2kpa)
    elif c == "7" and t == "4":
        atm2mpa = f * 0.1013
        print(atm2mpa)
    elif c == "7" and t == "5":
        atm2kfg = f * 1.032936
        print(atm2kfg)
    elif c == "7" and t == "6":
        atm2mm = f * 759.769
        print(atm2mm)
def lowpressure():
    print("Low Pressure\n")
    print("1. Meter of Water                 4. Inches of Mercury")
    print("2. Foot of Water                  5. Inches of Water")
    print("3. Centimeters of Mercury         6. Pascal")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Meter of Water                 4. Inches of Mercury")
    print("2. Foot of Water                  5. Inches of Water")
    print("3. Centimeters of Mercury         6. Pascal")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        m2f = f * 3.280696
        print(m2f)
    elif c == "1" and t == "3":
        m2cm = f * 7.356339
        print(m2cm)
    elif c == "1" and t == "4":
        m2inm = f * 2.896043
        print(m2inm)
    elif c == "1" and t == "5":
        m2inw = f * 39.36572
        print(m2inw)
    elif c == "1" and t == "6":
        m2pa = f * 9806
        print(m2pa)
    elif c == "2" and t == "1":
        f2m = f * 0.304813
        print(f2m)
    elif c == "2" and t == "3":
        f2cm = f * 2.242311
        print(f2cm)
    elif c == "2" and t == "4":
        f2inm = f * 0.882753
        print(f2inm)
    elif c == "2" and t == "5":
        f2inw = f * 11.9992
        print(f2inw)
    elif c == "2" and t == "6":
        f2pa = f * 2989
        print(f2pa)
    elif c == "3" and t == "1":
        cm2m = f * 0.135937
        print(cm2m)
    elif c == "3" and t == "2":
        cm2f = f * 0.445969
        print(cm2f)
    elif c == "3" and t == "4":
        cm2inm = f * 0.393689
        print(cm2inm)
    elif c == "3" and t == "5":
        cm2inw = f * 5.351265
        print(cm2inw)
    elif c == "3" and t == "6":
        cm2pa = f * 1333
        print(cm2pa)
    elif c == "4" and t == "1":
        inm2m = f * 0.345299
        print(inm2m)
    elif c == "4" and t == "2":
        inm2f = f * 1.13282
        print(inm2f)
    elif c == "4" and t == "3":
        inm2cm = f * 2.540135
        print(inm2cm)
    elif c == "4" and t == "5":
        inm2inw = f * 13.59293
        print(inm2inw)
    elif c == "4" and t == "6":
        inm2pa = f * 3386
        print(inm2pa)
    elif c == "5" and t == "1":
        inw2m = f * 0.025403
        print(inw2m)
    elif c == "5" and t == "2":
        inw2f = f * 0.083339
        print(inw2f)
    elif c == "5" and t == "3":
        inw2cm = f * 0.186872
        print(inw2cm)
    elif c == "5" and t == "4":
        inw2inf = f * 0.073568
        print(inw2inf)
    elif c == "5" and t == "6":
        inw2pa = f * 249.1
        print(inw2pa)
    elif c == "6" and t == "1":
        pa2m = f * 0.000102
        print(pa2m)
    elif c == "6" and t == "2":
        pa2f = f * 0.000335
        print(pa2f)
    elif c == "6" and t == "3":
        pa2cm = f * 0.00075
        print(pa2cm)
    elif c == "6" and t == "4":
        pa2inm = f * 0.000295
        print(pa2inm)
    elif c == "6" and t == "5":
        pa2inw = f * 0.004014
        print(pa2inw)
def speedunits():
    print("Speed Units\n")
    print("1. Meter/Second           4. Foot/Second")
    print("2. Meter/Minute           5. Foot/Minute")
    print("3. Kilometer/Hour         6. Miles/Hour")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Meter/Second           4. Foot/Second")
    print("2. Meter/Minute           5. Foot/Minute")
    print("3. Kilometer/Hour         6. Miles/Hour")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        ms2mm = f * 59.988
        print(ms2mm)
    elif c == "1" and t == "3":
        ms2kmh = f * 3.599712
        print(ms2kmh)
    elif c == "1" and t == "4":
        ms2fts = f * 3.28084
        print(ms2fts)
    elif c == "1" and t == "5":
        ms2ftm = f * 196.8504
        print(ms2ftm)
    elif c == "1" and t == "6":
        ms2mih = f * 2.237136
        print(ms2mih)
    elif c == "2" and t == "1":
        mm2ms = f * 0.01667
        print(mm2ms)
    elif c == "2" and t == "3":
        mm2kmh = f * 0.060007
        print(mm2kmh)
    elif c == "2" and t == "4":
        mm2fts = f * 0.054692
        print(mm2fts)
    elif c == "2" and t == "5":
        mm2ftm = f * 3.281496
        print(mm2ftm)
    elif c == "2" and t == "6":
        mm2mih = f * 0.037293
        print(mm2mih)
    elif c == "3" and t == "1":
        kmh2ms = f * 0.2778
        print(kmh2ms)
    elif c == "3" and t == "2":
        kmh2mm = f * 16.66467
        print(kmh2mm)
    elif c == "3" and t == "4":
        kmh2fts = f * 0.911417
        print(kmh2fts)
    elif c == "3" and t == "5":
        kmh2ftm = f * 54.68504
        print(kmh2ftm)
    elif c == "3" and t == "6":
        kmh2mih = f * 0.621477
        print(kmh2mih)
    elif c == "4" and t == "1":
        fts2ms = f * 0.3048
        print(fts2ms)
    elif c == "4" and t == "2":
        fts2mm = f * 18.28434
        print(fts2mm)
    elif c == "4" and t == "3":
        fts2kmh = f * 1.097192
        print(fts2kmh)
    elif c == "4" and t == "5":
        fts2ftm = f * 60
        print(fts2ftm)
    elif c == "4" and t == "6":
        fts2mih = f * 0.681879
        print(fts2mih)
    elif c == "5" and t == "1":
        ftm2ms = f * 0.00508
        print(ftm2ms)
    elif c == "5" and t == "2":
        ftm2mm = f * 0.304739
        print(ftm2mm)
    elif c == "5" and t == "3":
        ftm2kmh = f * 0.018287
        print(ftm2kmh)
    elif c == "5" and t == "4":
        ftm2fts = f * 0.016667
        print(ftm2fts)
    elif c == "5" and t == "6":
        ftm2mih = f * 0.011365
        print(ftm2mih)
    elif c == "6" and t == "1":
        mih2ms = f * 0.447
        print(mih2ms)
    elif c == "6" and t == "2":
        mih2mm = f * 26.81464
        print(mih2mm)
    elif c == "6" and t == "3":
        mih2kmh = f * 1.609071
        print(mih2kmh)
    elif c == "6" and t == "4":
        mih2fts = f * 1.466535
        print(mih2fts)
    elif c == "6" and t == "5":
        mih2ftm = f * 87.99213
        print(mih2ftm)
def torqueunits():
    print("Torque Units\n")
    print("1. Newton Meter                   3. Foot Pound")
    print("2. Kilogram Force Meter           4. Inch Pound")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Newton Meter                   3. Foot Pound")
    print("2. Kilogram Force Meter           4. Inch Pound")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        nm2kgfm = f * 0.101972
        print(nm2kgfm)
    elif c == "1" and t == "3":
        nm2ftlb = f * 0.737561
        print(nm2ftlb)
    elif c == "1" and t == "4":
        nm2inlb = f * 8.850732
        print(nm2inlb)
    elif c == "2" and t == "1":
        kgfm2nm = f * 9.80665
        print(kgfm2nm)
    elif c == "2" and t == "3":
        kgfm2ftlb = f * 7.233003
        print(kgfm2ftlb)
    elif c == "2" and t == "4":
        kgfm2inlb = f * 86.79603
        print(kgfm2inlb)
    elif c == "3" and t == "1":
        ftlb2nm = f * 1.35582
        print(ftlb2nm)
    elif c == "3" and t == "2":
        ftlb2kgfm = f * 0.138255
        print(ftlb2kgfm)
    elif c == "3" and t == "4":
        ftlb2inlb = f * 12
        print(ftlb2inlb)
    elif c == "4" and t == "1":
        inlb2nm = f * 0.112985
        print(inlb2nm)
    elif c == "4" and t == "2":
        inlb2kgfm = f * 0.011521
        print(inlb2kgfm)
    elif c == "4" and t == "3":
        inlb2ftlb = f * 0.083333
        print(inlb2ftlb)
def dynamicviscosity():
    print("Dynamic Viscosity\n")
    print("1. Centipoise")
    print("2. Poise")
    print("3. Pound / Foot*Second")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Centipoise")
    print("2. Poise")
    print("3. Pound / Foot*Second")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        cp2p = f * 0.01
        print (cp2p)
    elif c == "1" and t == "3":
        cp2lb = f * 0.000672
        print (cp2lb)
    elif c == "2" and t == "1":
        p2cp = f * 100
        print(p2cp)
    elif c == "2" and t == "3":
        p2lb = f * 0.067197
        print(p2lb)
    elif c == "3" and t == "1":
        lb2cp = f * 1488.16
        print(lb2cp)
    elif c == "3" and t == "2":
        lb2p = f * 14.8816
        print(lb2p)
def shoes():
    print("Shoe Size Convertor\n")
    print("1. Women's to Men's")
    print("2. Men's to Women's")
    print("3. Country to Country")
    opt = input("\nWhat are we going to do?\n")
    if opt == "1":
            w = input("\nWhat is your size?\n ")
            f = int(w)
            w2m = f - 1.5
            print("Your size in men's is", w2m)
    if opt == "2":
            w = input("\nWhat is your size?\n ")
            f = int(w)
            m2w = f + 1.5
            print("Your size in women's is", m2w)
    if opt == "3":
            print("1. Women's\n2. Men's")
            sex = input("\nWomen's or Men's\n")
            print("1. United States      4. Australia")
            print("2. Europe             5. Japan")
            print("3. United Kingdom     6. Asia")
            c = input("\nWhat are we converting?\n")
            w = input("\nWhat is your size?\n ")
            f = int(w)
            print("1. United States      4. Australia")
            print("2. Europe             5. Japan")
            print("3. United Kingdom     6. Asia")
            t = input("\nAnd what are we converting this to?\n")
            if sex == "1" and c == "1" and t == "2":
                w2eu = f + 30
                print("Your European size is", w2eu)
            elif sex == "1" and c == "1" and t == "3":
                w2uk = f - 2
                print("Your size in the UK is", w2uk)
            elif sex == "1" and c == "1" and t == "4":
                w2aus = f + 2.5
                print("Your Australian size is", w2aus)
            elif sex == "1" and c == "1" and t == "5":
                w2jap = f + 16
                print("Your size in Japan is", w2jap)
            elif sex == "1" and c == "1" and t == "6":
                w2asia = f + 16.5
                print("Your Asian size is", w2asia)
            elif sex == "1" and c == "2" and t == "1":
                eu2w = f - 30
                print("Your American size is", eu2w)
            elif sex == "1" and c == "2" and t == "3":
                eu2uk = f - 32
                print("Your American size is", eu2uk)
            elif sex == "1" and c == "2" and t == "4":
                eu2aus = f - 27.5
                print("Your Australian size is", eu2aus)
            elif sex == "1" and c == "2" and t == "5":
                eu2jap = f - 14
                print("Your size in Japan is", eu2jap)
            elif sex == "1" and c == "2" and t == "6":
                eu2asia = f - 13.5
                print("Your Asian size is", eu2asia)
            elif sex == "1" and c == "3" and t == "1":
                uk2w = f + 2
                print("Your American size is", uk2w)
            elif sex == "1" and c == "3" and t == "2":
                uk2eu = f + 32
                print("Your European size is", uk2eu)
            elif sex == "1" and c == "3" and t == "4":
                uk2aus = f - .5
                print("Your European size is", uk2aus)
            elif sex == "1" and c == "3" and t == "5":
                uk2jap = f + 18
                print("Your European size is", uk2jap)
            elif sex == "1" and c == "3" and t == "6":
                uk2asia = f + 18.5
                print("Your European size is", uk2asia)
            elif sex == "1" and c == "4" and t == "1":
                aus2w = f - 2.5
                print("Your European size is", aus2w)
            elif sex == "1" and c == "4" and t == "2":
                aus2eu = f + 27.5
                print("Your European size is", aus2eu)
            elif sex == "1" and c == "4" and t == "3":
                aus2uk = f + .5
                print("Your European size is", aus2uk)
            elif sex == "1" and c == "4" and t == "5":
                aus2jap = f + 13.5
                print("Your European size is", aus2jap)
            elif sex == "1" and c == "4" and t == "6":
                aus2asia = f + 14
                print("Your European size is", aus2asia)
            elif sex == "1" and c == "5" and t == "1":
                jap2w = f - 16
                print("Your European size is", jap2w)
            elif sex == "1" and c == "5" and t == "2":
                jap2eu = f + 14
                print("Your European size is", jap2eu)
            elif sex == "1" and c == "5" and t == "3":
                jap2uk = f - 18
                print("Your European size is", jap2uk)
            elif sex == "1" and c == "5" and t == "4":
                jap2aus = f - 13.5
                print("Your European size is", jap2aus)
            elif sex == "1" and c == "5" and t == "6":
                jap2asia = f + .5
                print("Your European size is", jap2asia)
            elif sex == "1" and c == "6" and t == "1":
                asia2w = f - 16.5
                print("Your European size is", asia2w)
            elif sex == "1" and c == "6" and t == "2":
                asia2eu = f + 27.5
                print("Your European size is", asia2eu)
            elif sex == "1" and c == "6" and t == "3":
                asia2uk = f - 18.5
                print("Your European size is", asia2uk)
            elif sex == "1" and c == "6" and t == "4":
                asia2aus = f - 14
                print("Your European size is", asia2aus)
            elif sex == "1" and c == "6" and t == "5":
                asia2jap = f + 13.5
                print("Your European size is", asia2jap)
            # mens
            elif sex == "2" and c == "1" and t == "2":
                m2eu = f + 33
                print("Your size in the UK is", m2eu)
            elif sex == "2" and c == "1" and t == "3":
                m2uk = f - 1
                print("Your size in the UK is", m2uk)
            elif sex == "2" and c == "1" and t == "4":
                m2aus = f - 1
                print("Your size in the UK is", m2aus)
            elif sex == "2" and c == "1" and t == "5":
                m2jap = f + 18.5
                print("Your size in the UK is", m2jap)
            elif sex == "2" and c == "1" and t == "6":
                m2asia = f + 17.5
                print("Your size in the UK is", m2asia)
            elif sex == "2" and c == "2" and t == "1":
                meu2m = f - 33
                print("Your size in the UK is", meu2m)
            elif sex == "2" and c == "2" and t == "3":
                meu2uk = f - 34
                print("Your size in the UK is", meu2uk)
            elif sex == "2" and c == "2" and t == "4":
                meu2aus = f - 34
                print("Your size in the UK is", meu2aus)
            elif sex == "2" and c == "2" and t == "5":
                meu2jap = f - 14.5
                print("Your size in the UK is", meu2jap)
            elif sex == "2" and c == "2" and t == "6":
                meu2asia = f - 15.5
                print("Your size in the UK is", meu2asia)
            elif sex == "2" and c == "3" and t == "1":
                muk2m = f + 1
                print("Your size in the UK is", muk2m)
            elif sex == "2" and c == "3" and t == "2":
                muk2eu = f + 34
                print("Your size in the UK is", muk2eu)
            elif sex == "2" and c == "3" and t == "4":
                muk2aus = f
                print("Your size in the UK is", muk2aus)
            elif sex == "2" and c == "3" and t == "5":
                muk2jap = f + 19.5
                print("Your size in the UK is", muk2jap)
            elif sex == "2" and c == "3" and t == "6":
                muk2asia = f + 18.5
                print("Your size in the UK is", muk2asia)
            elif sex == "2" and c == "4" and t == "1":
                maus2m = f + 1
                print("Your size in the UK is", maus2m)
            elif sex == "2" and c == "4" and t == "2":
                maus2eu = f + 34
                print("Your size in the UK is", maus2eu)
            elif sex == "2" and c == "4" and t == "3":
                maus2uk = f
                print("Your size in the UK is", maus2uk)
            elif sex == "2" and c == "4" and t == "5":
                maus2jap = f + 19.5
                print("Your size in the UK is", maus2jap)
            elif sex == "2" and c == "4" and t == "6":
                maus2asia = f + 18.5
                print("Your size in the UK is", maus2asia)
            elif sex == "2" and c == "5" and t == "1":
                mjap2m = f - 18.5
                print("Your size in the UK is", mjap2m)
            elif sex == "2" and c == "5" and t == "2":
                mjap2eu = f + 14.5
                print("Your size in the UK is", mjap2eu)
            elif sex == "2" and c == "5" and t == "3":
                mjap2uk = f - 19.5
                print("Your size in the UK is", mjap2uk)
            elif sex == "2" and c == "5" and t == "4":
                mjap2aus = f - 19.5
                print("Your size in the UK is", mjap2aus)
            elif sex == "2" and c == "5" and t == "6":
                mjap2asia = f - 1
                print("Your size in the UK is", mjap2asia)
            elif sex == "2" and c == "6" and t == "1":
                masia2m = f - 17.5
                print("Your size in the UK is", masia2m)
            elif sex == "2" and c == "6" and t == "2":
                masia2eu = f + 15.5
                print("Your size in the UK is", masia2eu)
            elif sex == "2" and c == "6" and t == "3":
                masia2uk = f - 18.5
                print("Your size in the UK is", masia2uk)
            elif sex == "2" and c == "6" and t == "4":
                masia2aus = f - 18.5
                print("Your size in the UK is", masia2aus)
            elif sex == "2" and c == "6" and t == "5":
                masia2jap = f + 1
                print("Your size in the UK is", masia2jap)
            else :
                print("Please enter valid information")
def kinematicviscosity():
    print("Kinematic Viscosity\n")
    print("1. Centistoke      3. Foot Square/Second")
    print("2. Stoke           4. Meter Square/Second")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter what will be converted\n ")
    f = int(w)
    print("1. Centistoke      3. Foot Square/Second")
    print("2. Stoke           4. Meter Square/Second")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        c2s = f * 0.01
        print(c2s)
    elif c == "1" and t == "3":
        c2f = f * 0.000011
        print(c2f)
    elif c == "1" and t == "4":
        c2m = f * 0.000001
        print(c2m)
    elif c == "2" and t == "1":
        s2c = f * 100
        print(s2c)
    elif c == "2" and t == "3":
        s2f = f * 0.001076
        print(s2f)
    elif c == "2" and t == "4":
        s2m = f * 0.0001
        print(s2m)
    elif c == "3" and t == "1":
        f2c = f * 92903
        print(f2c)
    elif c == "3" and t == "2":
        f2s = f * 929.03
        print(f2s)
    elif c == "3" and t == "4":
        f2m = f * 0.092903
        print(f2m)
    elif c == "4" and t == "1":
        m2c = f * 1000000
        print(m2c)
    elif c == "4" and t == "2":
        m2s = f * 10000
        print(m2s)
    elif c == "4" and t == "3":
        m2f = f * 10.76392
        print(m2f)
def tempconv():
    print("Temperature Conversions\n")
    print("1. Fahrenheit")
    print("2. Celsius")
    print("3. Kelvin")
    c = input("\nWhat are we converting?\n")
    w = input("\nPlease enter your degree\n ")
    f = int(w)
    print("1. Fahrenheit")
    print("2. Celsius")
    print("3. Kelvin")
    t = input("\nAnd what are we converting this to?\n")
    if c == "1" and t == "2":
        f2c = (f * 9 / 5) + 32
        print(f2c, "C")
    elif c == "1" and t == "3":
        f2k = (1.8 * f) - 459.67
        print(f2k, "Kelvin")
    elif c == "2" and t == "1":
        c2f = (f - 32) * 5/9
        print(c2f, "F")
    elif c == "2" and t == "3":
        c2k = (f - 273.15)
        print(c2k, "Kelvin")
    elif c == "3" and t == "1":
        k2f = (f + 459.67) / 1.8
        print(k2f, "F")
    elif c == "3" and t == "2":
        k2c = f + 273.15
        print(k2c, "C")
def dress():
    print("Womens Dress Sizes\n")
    print("1. United States      5. Germany")
    print("2. United Kingdom     6. Italy")
    print("3. Japan              7. Australia")
    print("4. Europe")
    c = input("\nWhat are we converting?\n")
    w = input("\nWhat is your size?\n ")
    f = int(w)
    print("1. United States      5. Germany")
    print("2. United Kingdom     6. Italy")
    print("3. Japan              7. Australia")
    print("4. Europe")
    t = input("\nAnd what are we converting this to?\n")
    w2uk = f + 2
    w2jap = f + 1, f + 2, f + 3
    w2eu = f + 30
    w2germ = f + 28
    w2it = f + 34
    w2aus = f + 2
    uk2w = f - 2
    uk2jap = f -1, f, f + 1
    uk2eu = f + 28
    uk2germ = f + 26
    uk2it = f + 32
    uk2aus = f
    jap2w = f - 1, f - 2, f - 3
    jap2uk = f + 1, f, f - 1
    jap2eu = f + 28
    jap2germ = f + 27
    jap2it = f + 33
    jap2aus = f
    eu2w = f - 30
    eu2uk = f - 28
    eu2jap = f - 28
    eu2germ = f - 2
    eu2it = f + 4
    eu2aus = f - 28
    germ2w = f - 28
    germ2uk = f - 26
    germ2jap = f - 27
    germ2eu = f + 2
    germ2it = f + 6
    germ2aus = f - 26
    it2w = f - 34
    it2uk = f - 32
    it2jap = f - 33
    it2germ = f - 6
    it2aus = f - 32
    it2eu = f - 4
    aus2w = f - 2
    aus2uk = f
    aus2jap = f
    aus2eu = f + 28
    aus2germ = f + 26
    aus2it = f + 32

    if c == "1" and t == "2":
        print(w2uk)
    elif c == "1" and t == "3":
        print(w2jap)
    elif c == "1" and t == "4":
        print(w2eu)
    elif c == "1" and t == "5":
        print(w2germ)
    elif c == "1" and t == "6":
        print(w2it)
    elif c == "1" and t == "7":
        print(w2aus)
    elif c == "2" and t == "1":
        print(uk2w)
    elif c == "2" and t == "3":
        print(uk2jap)
    elif c == "2" and t == "4":
        print(uk2eu)
    elif c == "2" and t == "5":
        print(uk2germ)
    elif c == "2" and t == "6":
        print(uk2it)
    elif c == "2" and t == "7":
        print(uk2aus)
    elif c == "3" and t == "1":
        print(jap2w)
    elif c == "3" and t == "2":
        print(jap2uk)
    elif c == "3" and t == "4":
        print(jap2eu)
    elif c == "3" and t == "5":
        print(jap2germ)
    elif c == "3" and t == "6":
        print(jap2it)
    elif c == "3" and t == "7":
        print(jap2aus)
    elif c == "4" and t == "1":
        print(eu2w)
    elif c == "4" and t == "2":
        print(eu2uk)
    elif c == "4" and t == "3":
        print(eu2jap)
    elif c == "4" and t == "5":
        print(eu2germ)
    elif c == "4" and t == "6":
        print(eu2it)
    elif c == "4" and t == "7":
        print(eu2aus)
    elif c == "5" and t == "1":
        print(germ2w)
    elif c == "5" and t == "2":
        print(germ2uk)
    elif c == "5" and t == "3":
        print(germ2jap)
    elif c == "5" and t == "4":
        print(germ2eu)
    elif c == "5" and t == "6":
        print(germ2it)
    elif c == "5" and t == "7":
        print(germ2aus)
    elif c == "6" and t == "1":
        print(it2w)
    elif c == "6" and t == "2":
        print(it2uk)
    elif c == "6" and t == "3":
        print(it2jap)
    elif c == "6" and t == "4":
        print(it2eu)
    elif c == "6" and t == "5":
        print(it2germ)
    elif c == "6" and t == "7":
        print(it2aus)
    elif c == "7" and t == "1":
        print(aus2w)
    elif c == "7" and t == "2":
        print(aus2uk)
    elif c == "7" and t == "3":
        print(aus2jap)
    elif c == "7" and t == "4":
        print(aus2eu)
    elif c == "7" and t == "5":
        print(aus2germ)
    elif c == "7" and t == "6":
        print(aus2it)
def cookingm():
    print("1. Cup            5. Milliliter")
    print("2. Fluid ounce    6. Pint")
    print("3. Tablespoon     7. Quart")
    print("4. Teaspoon       8. Bushel")
    c = input("\nWhat are we converting?\n")
    w = input("\nHow many of these are we converting?\n ")
    f = int(w)
    print("1. Cup            5. Milliliter")
    print("2. Fluid ounce    6. Pint")
    print("3. Tablespoon     7. Quart")
    print("4. Teaspoon       8. Bushel")
    print("                  9. Gallon")
    print("                  10. Peck")
    t = input("\nAnd what are we converting this to?\n")
    cup2foz = f * 8
    cup2tblspn = f * 16
    cup2tspn = f * 48
    cup2ml = f * 237
    cup2pint = f * .5
    cup2quart = f / 4
    foz2cup = f / 8
    foz2tblspn = f * 2
    foz2tspn = f * 6
    foz2ml = f * 30
    tblspn2cup = f / 16
    tblspn2foz = f * .5
    tblspn2tspn = f * 3
    tblspn2ml = f * 15
    tspn2cup = f / 48
    tspn2foz = f / 6
    tspn2tblspn = f / 3
    tspn2ml = f * 5
    ml2cup = f / 237
    ml2foz = f / 30
    ml2tblspn = f / 15
    ml2tspn = f / 5
    pint2cup = f / .5
    pint2quart = f / 2
    quart2gal = f / 4
    quart2peck = f / 8
    quart2cup = 4 * 4
    peck2bush = f / 4
    if c == "1" and t == "2":
        print(int(cup2foz))
    elif c == "1" and t == "3":
        print(cup2tblspn)
    elif c == "1" and t == "4":
        print(cup2tspn)
    elif c == "1" and t == "5":
        print(cup2ml)
    elif c == "1" and t == "6":
        print(cup2pint)
    elif c == "1" and t == "7":
        print(cup2quart)
    elif c == "1" and t == "8":
        print("Sorry, not available.")
    elif c == "2" and t == "1":
        print(foz2cup)
    elif c == "2" and t == "3":
        print(foz2tblspn)
    elif c == "2" and t == "4":
        print(foz2tspn)
    elif c == "2" and t == "5":
        print(foz2ml)
    elif c == "3" and t == "1":
        print(tblspn2cup)
    elif c == "3" and t == "2":
        print(tblspn2foz)
    elif c == "3" and t == "4":
        print(tblspn2tspn)
    elif c == "3" and t == "5":
        print(tblspn2ml)
    elif c == "3" and t == "1":
        print(tblspn2cup)
    elif c == "4" and t == "1":
        print(tspn2cup)
    elif c == "4" and t == "2":
        print(tspn2foz)
    elif c == "4" and t == "3":
        print(tspn2tblspn)
    elif c == "4" and t == "5":
        print(tspn2ml)
    elif c == "5" and t == "1":
        print(ml2cup)
    elif c == "5" and t == "2":
        print(ml2foz)
    elif c == "5" and t == "3":
        print(ml2tblspn)
    elif c == "5" and t == "4":
        print(ml2tspn)
    elif c == "6" and t == "1":
        print(pint2cup)
    elif c == "6" and t == "7":
        print(pint2quart)
    elif c == "7" and t == "9":
        print(quart2gal)
    elif c == "7" and t == "1":
        print(quart2cup)
    elif c == "7" and t == "10":
        print(quart2peck)
    elif c == "10" and t == "8":
        print(peck2bush)
    else :
        print("Sorry, not available!")
def safecooking():
    print("1. Beef        5. Chicken (whole) ")
    print("2. Pork        6. Turkey (whole)")
    print("3. Lamb        7. Stuffing in poultry")
    print("4. Ham (precooked) ")
    whichmeat = input("\nWhich meat are we working with?\n")
    if whichmeat == "1":
        print("1. Rare\n2. Medium\n 3. Well Done")
        rarity = input("\nAt what rarity?\n")
        if rarity == "1":
            print("140°F")
        elif rarity == "2":
            print("160°F")
        elif rarity == "3":
            print("170°F")
    elif whichmeat == "2":
        print("1. Roast\n2. Ground")
        rg = input("\nAre we doing a roast or ground pork?\n")
        if rg == "1":
            print("165°F")
        elif rg == "2":
            print("160°F")
    elif whichmeat == "3":
        print("1. Roast\n2. Ground")
        rg = input("\nAre we doing a roast or ground pork?\n")
        if rg == "1":
            print("145°F")
        elif rg == "2":
            print("160°F")
    elif whichmeat == "4":
        print("140°F")
    elif whichmeat == "5":
        print("180°F")
    elif whichmeat == "6":
        print("180°F")
    elif whichmeat == "7":
        print("165°F")
def oventemp():
    print("1. Very low (250 - 275°F)          4. High heat (400 - 425°F)")
    print("2. Slow cook (300 - 325°F)         5. Very hot (450 - 475°F)")
    print("3. Moderate heat (350 - 375°F)     6. Extremely hot (500 - 525°F)")
def physics():
    print("Physics\n")
    print("1. Average Speed             13. Kinetic Energy ")
    print("2. Average Velocity          14. Power")
    print("3. Acceleration              15. Work Done")
    print("4. Final Velocity            16. Pressure of Liquid Column")
    print("5. Displacement              17. Pressure")
    print("6. Charge Flow               18. Distance traveled")
    print("7. Newton's Second Law       19. Momentum ")
    print("8. Weight                    20. Efficiency ")
    print("9. Density                   21. Potential Difference ")
    print("10. Moment of Force          22. Curvature...")
    print("11. Wave Frequency           ")
    print("12. Wave Velocity          ")
    choice = input("What shall we work on?: ")
    if choice == '1':
        d = input("What is the total distance?: ")
        t = input("And how long did it take to travel this distance?")
        dis = int(d)
        time = int(t)
        speed = dis / time
        print(speed)
    elif choice == "2":
        a = input("What is the total displacement? ")
        b = input("And how long did it take to travel this distance?")
        c = int(a)
        d = int(b)
        e = c / d
        print(e)
    elif choice == "3":
        a = input("What is the total velocity? ")
        b = input("And how long did it take to travel this distance?")
        c = int(a)
        d = int(b)
        e = c / d
        print(e)
    elif choice == "4":
        a = input("What is the initial velocity? ")
        b = input("What is the acceleration? ")
        x = input("And what was the total time taken?")
        c = int(a)
        d = int(b)
        y = int(x)
        e = c + (d * y)
        print(e)
    elif choice == "5":
        a = input("What is the initial velocity? ")
        b = input("What is the acceleration? ")
        x = input("And what was the total time taken?")
        c = int(a)
        d = int(b)
        y = int(x)
        e = c * y + .5 * ((d * y) ^ 2)
        print(e)
    elif choice == "6":
        a = input("What is the current? ")
        b = input("And how long did it take? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "7":
        a = input("What is the mass? ")
        b = input("And it's acceleration? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "8":
        a = input("What is the mass? ")
        b = input("And it's 'gravitational field strength'? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "9":
        a = input("What is the mass? ")
        b = input("And it's volume? ")
        c = int(a)
        d = int(b)
        e = c / d
        print(e)
    elif choice == "10":
        a = input("What is the force? ")
        b = input("And it's distance from force to pivot? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "11":
        a = input("What is the period? ")
        c = int(a)
        e = 1 / c
        print(e)
    elif choice == "12":
        a = input("What is the frequency? ")
        b = input("And it's wavelength? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "13":
        a = input("What is the mass? ")
        b = input("And it's velocity? ")
        c = int(a)
        d = int(b)
        e = .5 * c * b ^ 2
        print(e)
    elif choice == "14":
        a = input("How much work was done? ")
        b = input("And in how many units of time? ")
        c = int(a)
        d = int(b)
        e = c / d
        print(e)
    elif choice == "15":
        a = input("What is the force? ")
        b = input("And the distance in direction of force? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "16":
        a = input("What is the height of the column? ")
        b = input("It's density? ")
        n = input("And it's gravitational field strength?")
        c = int(a)
        d = int(b)
        f = int(n)
        e = c * d * f
        print(e)
    elif choice == "17":
        a = input("What is the force over the area? ")
        b = input("And it's area? ")
        c = int(a)
        d = int(b)
        e = c / d
        print(e)
    elif choice == "18":
        a = input("What is the speed? ")
        b = input("And it's time? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "19":
        a = input("What is the mass? ")
        b = input("And it's velocity? ")
        c = int(a)
        d = int(b)
        e = c * d
        print(e)
    elif choice == "20":
        a = input("What is the useful power output? ")
        b = input("And it's total power unit? ")
        c = int(a)
        d = int(b)
        e = c / d
        print(e)
    elif choice == "21":
        a = input("What is the current? ")
        b = input("And it's resistence? ")
        c = int(a)
        d = int(b)
        e = c / d
        print(e)
    elif choice == "22":
        miles = input("How for away in miles is the location? ")
        curvature = 8 * int(miles) ** 2
        inch2mile = curvature / 63360
        inch2feet = curvature / 12
        print("This is how far below the horizon the location is\n", curvature, "inches\n", inch2feet, "feet\n",
              inch2mile, "miles")
        lol = input("Can you see beyond the horizon? ")
        if lol == "yes":
            print("That's pretty weird :p")
def more():
    again = input("Anything else I can help with? (Y/N):\n").lower()
    if again == "y":
        startscreen()
def startscreen():
    print("Welcome to Fern!")
    print("Pick an option below\n")
    print("1. Length             12. Torque Units")
    print("2. Area               13. Dynamic Viscosity")
    print("3. Volume             14. Shoes")
    print("4. Mass               15. Kinematic Viscosity")
    print("5. Density            16. Temperature Conversion")
    print("6. Liquid Flow        17. Dress Sizes")
    print("7. Gas Flow           18. Cooking Measurements")
    print("8. Mass Flow          19. Safe Cooking")
    print("9. High Pressure      20. Oven Temperatures")
    print("10. Low Pressure      21. Physics")
    print("11. Speed Units       22. Coming soon... ")
    op = input("Insert # here, please: ")
    if op == "1":
        length()
    elif op == "2":
        area()
    elif op == "3":
        volume()
    elif op == "4":
        mass()
    elif op == "5":
        density()
    elif op == "6":
        liquidflow()
    elif op == "7":
        gasflow()
    elif op == "8":
        massflow()
    elif op == "9":
        highpressure()
    elif op == "10":
        lowpressure()
    elif op == "11":
        speedunits()
    elif op == "12":
        torqueunits()
    elif op == "13":
        dynamicviscosity()
    elif op == "14":
        shoes()
    elif op == "15":
        kinematicviscosity()
    elif op == "16":
        tempconv()
    elif op == "17":
        dress()
    elif op == "18":
        cookingm()
    elif op == "19":
        safecooking()
    elif op == "20":
        oventemp()
    elif op == "21":
        physics()
    else:
        print("Enter a valid number")
        startscreen()
    more()

startscreen()
