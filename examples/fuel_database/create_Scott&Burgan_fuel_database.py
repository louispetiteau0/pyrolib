"""

Create the fuel database for Rothermel rate of spread model
40 fuel models described in Scott and Burgan [1]_

References
----------

[1] Scott, J. H. (2005).
    Standard fire behavior fuel models: a comprehensive set for use with Rothermel's surface fire spread model.
    US Department of Agriculture, Forest Service, Rocky Mountain Research Station.
    https://www.fs.fed.us/rm/pubs/rmrs/gtr/rmrs_gtr0305.pdf

"""

from pyrolib.fuelmap import FuelDatabase, FuelMap, BalbiFuel, RothFuel

# create fuel db
db = FuelDatabase()

# Conversion factor from ton/ac (units in Scott and Burgan [1]_) to lb/ft2 (units used in Rothermel Rate of Spread and RothFuel))
ton_ac_to_lb_ft2 = 0.0459137

# Defines the Grass fuel models (GR1 to GR9) of Scott and Burgan [1]_
GR1 = RothFuel()
GR2 = RothFuel(wo_1hd=0.10*ton_ac_to_lb_ft2, wo_10hd=0,                    wo_hl=1.0*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=1800, delta=1.0, mx_dead=0.15)
GR3 = RothFuel(wo_1hd=0.10*ton_ac_to_lb_ft2, wo_10hd=0.4*ton_ac_to_lb_ft2, wo_hl=1.5*ton_ac_to_lb_ft2, sigma_1hd=1500, sigma_hl=1300, delta=2.0, mx_dead=0.30)
GR4 = RothFuel(wo_1hd=0.25*ton_ac_to_lb_ft2, wo_10hd=0,                    wo_hl=1.9*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=1800, delta=2.0, mx_dead=0.15)
GR5 = RothFuel(wo_1hd=0.40*ton_ac_to_lb_ft2, wo_10hd=0,                    wo_hl=2.5*ton_ac_to_lb_ft2, sigma_1hd=1800, sigma_hl=1600, delta=1.5, mx_dead=0.40)
GR6 = RothFuel(wo_1hd=0.10*ton_ac_to_lb_ft2, wo_10hd=0,                    wo_hl=3.4*ton_ac_to_lb_ft2, sigma_1hd=2200, sigma_hl=2000, delta=1.5, mx_dead=0.40)
GR7 = RothFuel(wo_1hd=1.00*ton_ac_to_lb_ft2, wo_10hd=0,                    wo_hl=5.4*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=1800, delta=3.0, mx_dead=0.15)
GR8 = RothFuel(wo_1hd=0.50*ton_ac_to_lb_ft2, wo_10hd=1.0*ton_ac_to_lb_ft2, wo_hl=7.3*ton_ac_to_lb_ft2, sigma_1hd=1500, sigma_hl=1300, delta=4.0, mx_dead=0.30)
GR9 = RothFuel(wo_1hd=1.00*ton_ac_to_lb_ft2, wo_10hd=1.0*ton_ac_to_lb_ft2, wo_hl=9.0*ton_ac_to_lb_ft2, sigma_1hd=1800, sigma_hl=1600, delta=5.0, mx_dead=0.40)

# add fuels to the database
for fuel_name, fuel in (("GR1", GR1),("GR2", GR2),("GR3", GR3),("GR4", GR4),("GR5", GR5),("GR6", GR6),("GR7", GR7),("GR8", GR8),("GR9", GR9)):
    db[fuel_name] = {"RothFuel": fuel}

# Defines the Grass-Shrub fuel models (GS1 to GS4) of Scott and Burgan [1]_
GS1 = RothFuel(wo_1hd=0.2*ton_ac_to_lb_ft2, wo_10hd=0,                     wo_100hd=0,                    wo_hl=0.50*ton_ac_to_lb_ft2, wo_wl= 0.65*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=1800, sigma_wl=1800, delta=0.9, mx_dead=0.15)
GS2 = RothFuel(wo_1hd=0.5*ton_ac_to_lb_ft2, wo_10hd=0.50*ton_ac_to_lb_ft2, wo_100hd=0,                    wo_hl=0.60*ton_ac_to_lb_ft2, wo_wl= 1.00*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=1800, sigma_wl=1800, delta=1.5, mx_dead=0.15)
GS3 = RothFuel(wo_1hd=0.3*ton_ac_to_lb_ft2, wo_10hd=0.25*ton_ac_to_lb_ft2, wo_100hd=0,                    wo_hl=1.45*ton_ac_to_lb_ft2, wo_wl= 1.25*ton_ac_to_lb_ft2, sigma_1hd=1800, sigma_hl=1600, sigma_wl=1600, delta=1.8, mx_dead=0.40)
GS4 = RothFuel(wo_1hd=1.9*ton_ac_to_lb_ft2, wo_10hd=0.30*ton_ac_to_lb_ft2, wo_100hd=0.1*ton_ac_to_lb_ft2, wo_hl=3.40*ton_ac_to_lb_ft2, wo_wl= 7.10*ton_ac_to_lb_ft2, sigma_1hd=1800, sigma_hl=1600, sigma_wl=1600, delta=2.1, mx_dead=0.40)

# add fuels to the database
for fuel_name, fuel in (("GS1", GS1),("GS2", GS2),("GS3", GS3),("GS4", GS4)):
    db[fuel_name] = {"RothFuel": fuel}

# Defines the Shrub fuel models (SH1 to SH9) of Scott and Burgan [1]_
SH1 = RothFuel(wo_1hd=0.25*ton_ac_to_lb_ft2, wo_10hd=0.25*ton_ac_to_lb_ft2, wo_100hd=0,                     wo_hl=0.15*ton_ac_to_lb_ft2, wo_wl=1.30*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=1800, sigma_wl=1600, delta=1.0, mx_dead=0.15)
SH2 = RothFuel(wo_1hd=1.35*ton_ac_to_lb_ft2, wo_10hd=2.40*ton_ac_to_lb_ft2, wo_100hd=0.75*ton_ac_to_lb_ft2, wo_hl=0,                     wo_wl=3.85*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=9999, sigma_wl=1600, delta=1.0, mx_dead=0.15)
SH3 = RothFuel(wo_1hd=0.45*ton_ac_to_lb_ft2, wo_10hd=3.00*ton_ac_to_lb_ft2, wo_100hd=0,                     wo_hl=0,                     wo_wl=6.20*ton_ac_to_lb_ft2, sigma_1hd=1600, sigma_hl=9999, sigma_wl=1400, delta=2.4, mx_dead=0.40)
SH4 = RothFuel(wo_1hd=0.85*ton_ac_to_lb_ft2, wo_10hd=1.15*ton_ac_to_lb_ft2, wo_100hd=0.20*ton_ac_to_lb_ft2, wo_hl=0,                     wo_wl=2.55*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=9999, sigma_wl=1600, delta=3.0, mx_dead=0.30)
SH5 = RothFuel(wo_1hd=3.60*ton_ac_to_lb_ft2, wo_10hd=2.10*ton_ac_to_lb_ft2, wo_100hd=0,                     wo_hl=0,                     wo_wl=2.90*ton_ac_to_lb_ft2, sigma_1hd=750,  sigma_hl=9999, sigma_wl=1600, delta=6.0, mx_dead=0.15)
SH6 = RothFuel(wo_1hd=2.90*ton_ac_to_lb_ft2, wo_10hd=1.45*ton_ac_to_lb_ft2, wo_100hd=0,                     wo_hl=0,                     wo_wl=1.40*ton_ac_to_lb_ft2, sigma_1hd=750,  sigma_hl=9999, sigma_wl=1600, delta=2.0, mx_dead=0.30)
SH7 = RothFuel(wo_1hd=3.50*ton_ac_to_lb_ft2, wo_10hd=5.30*ton_ac_to_lb_ft2, wo_100hd=2.20*ton_ac_to_lb_ft2, wo_hl=0,                     wo_wl=3.40*ton_ac_to_lb_ft2, sigma_1hd=750,  sigma_hl=9999, sigma_wl=1600, delta=6.0, mx_dead=0.15)
SH8 = RothFuel(wo_1hd=2.05*ton_ac_to_lb_ft2, wo_10hd=3.40*ton_ac_to_lb_ft2, wo_100hd=0.85*ton_ac_to_lb_ft2, wo_hl=0,                     wo_wl=4.35*ton_ac_to_lb_ft2, sigma_1hd=750,  sigma_hl=9999, sigma_wl=1600, delta=3.0, mx_dead=0.40)
SH9 = RothFuel(wo_1hd=4.50*ton_ac_to_lb_ft2, wo_10hd=2.45*ton_ac_to_lb_ft2, wo_100hd=0,                     wo_hl=1.55*ton_ac_to_lb_ft2, wo_wl=7.00*ton_ac_to_lb_ft2, sigma_1hd=750,  sigma_hl=1800, sigma_wl=1500, delta=4.4, mx_dead=0.40)

# add fuels to the database
for fuel_name, fuel in (("SH1", SH1),("SH2", SH2),("SH3", SH3),("SH4", SH4),("SH5", SH5),("SH6", SH6),("SH7", SH7),("SH8", SH8),("SH9", SH9)):
    db[fuel_name] = {"RothFuel": fuel}

# Defines the Timber understory fuel models (TU1 to TU5) of Scott and Burgan [1]_
TU1 = RothFuel(wo_1hd=0.20*ton_ac_to_lb_ft2, wo_10hd=0.90*ton_ac_to_lb_ft2, wo_100hd=1.50*ton_ac_to_lb_ft2, wo_hl=0.20*ton_ac_to_lb_ft2, wo_wl=0.90*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=1800, sigma_wl=1600, delta=0.6, mx_dead=0.20)
TU2 = RothFuel(wo_1hd=0.95*ton_ac_to_lb_ft2, wo_10hd=1.80*ton_ac_to_lb_ft2, wo_100hd=1.25*ton_ac_to_lb_ft2, wo_hl=0,                     wo_wl=0.20*ton_ac_to_lb_ft2, sigma_1hd=2000, sigma_hl=9999, sigma_wl=1600, delta=1.0, mx_dead=0.30)
TU3 = RothFuel(wo_1hd=1.10*ton_ac_to_lb_ft2, wo_10hd=0.15*ton_ac_to_lb_ft2, wo_100hd=0.25*ton_ac_to_lb_ft2, wo_hl=0.65*ton_ac_to_lb_ft2, wo_wl=1.10*ton_ac_to_lb_ft2, sigma_1hd=1800, sigma_hl=1600, sigma_wl=1400, delta=1.3, mx_dead=0.30)
TU4 = RothFuel(wo_1hd=4.50*ton_ac_to_lb_ft2, wo_10hd=0,                     wo_100hd=0,                     wo_hl=0,                     wo_wl=2.00*ton_ac_to_lb_ft2, sigma_1hd=2300, sigma_hl=9999, sigma_wl=2000, delta=0.5, mx_dead=0.12)
TU5 = RothFuel(wo_1hd=4.00*ton_ac_to_lb_ft2, wo_10hd=4.00*ton_ac_to_lb_ft2, wo_100hd=3.00*ton_ac_to_lb_ft2, wo_hl=0,                     wo_wl=3.00*ton_ac_to_lb_ft2, sigma_1hd=1500, sigma_hl=9999, sigma_wl=750,  delta=1.0, mx_dead=0.25)

# add fuels to the database
for fuel_name, fuel in (("TU1", TU1),("TU2", TU2),("TU3", TU3),("TU4", TU4),("TU5", TU5)):
    db[fuel_name] = {"RothFuel": fuel}

# Defines the Timber litter fuel models (TL1 to TL9) of Scott and Burgan [1]_
TL1 = RothFuel(wo_1hd=1.00*ton_ac_to_lb_ft2, wo_10hd=2.2*ton_ac_to_lb_ft2, wo_100hd=3.60*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=0.2, mx_dead=0.30)
TL2 = RothFuel(wo_1hd=1.40*ton_ac_to_lb_ft2, wo_10hd=2.3*ton_ac_to_lb_ft2, wo_100hd=2.20*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=0.2, mx_dead=0.25)
TL3 = RothFuel(wo_1hd=0.50*ton_ac_to_lb_ft2, wo_10hd=2.2*ton_ac_to_lb_ft2, wo_100hd=2.80*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=0.3, mx_dead=0.20)
TL4 = RothFuel(wo_1hd=0.50*ton_ac_to_lb_ft2, wo_10hd=1.5*ton_ac_to_lb_ft2, wo_100hd=4.20*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=0.4, mx_dead=0.25)
TL5 = RothFuel(wo_1hd=1.15*ton_ac_to_lb_ft2, wo_10hd=2.5*ton_ac_to_lb_ft2, wo_100hd=4.20*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=0.6, mx_dead=0.25)
TL6 = RothFuel(wo_1hd=2.40*ton_ac_to_lb_ft2, wo_10hd=1.2*ton_ac_to_lb_ft2, wo_100hd=1.20*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=0.3, mx_dead=0.25)
TL7 = RothFuel(wo_1hd=0.30*ton_ac_to_lb_ft2, wo_10hd=1.4*ton_ac_to_lb_ft2, wo_100hd=8.10*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=0.4, mx_dead=0.25)
TL8 = RothFuel(wo_1hd=5.80*ton_ac_to_lb_ft2, wo_10hd=1.4*ton_ac_to_lb_ft2, wo_100hd=1.10*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=1800, sigma_hl=9999, delta=0.3, mx_dead=0.35)
TL9 = RothFuel(wo_1hd=6.65*ton_ac_to_lb_ft2, wo_10hd=3.3*ton_ac_to_lb_ft2, wo_100hd=4.15*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=1800, sigma_hl=9999, delta=0.6, mx_dead=0.35)

# add fuels to the database
for fuel_name, fuel in (("TL1", TL1),("TL2", TL2),("TL3", TL3),("TL4", TL4),("TL5", TL5),("TL6", TL6),("TL7", TL7),("TL8", TL8),("TL9", TL9)):
    db[fuel_name] = {"RothFuel": fuel}

# Defines the Slash-Blowdown Fuel Type Models (SB1 to SB4) of Scott and Burgan [1]_
SB1 = RothFuel(wo_1hd=1.50*ton_ac_to_lb_ft2, wo_10hd=3.00*ton_ac_to_lb_ft2, wo_100hd=11.0*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=1.0, mx_dead=0.25)
SB2 = RothFuel(wo_1hd=4.50*ton_ac_to_lb_ft2, wo_10hd=4.25*ton_ac_to_lb_ft2, wo_100hd=4.00*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=1.0, mx_dead=0.25)
SB3 = RothFuel(wo_1hd=5.50*ton_ac_to_lb_ft2, wo_10hd=2.75*ton_ac_to_lb_ft2, wo_100hd=3.00*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=1.2, mx_dead=0.25)
SB4 = RothFuel(wo_1hd=5.25*ton_ac_to_lb_ft2, wo_10hd=5.25*ton_ac_to_lb_ft2, wo_100hd=5.25*ton_ac_to_lb_ft2, wo_hl=0, sigma_1hd=2000, sigma_hl=9999, delta=2.7, mx_dead=0.25)

# add fuels to the database
for fuel_name, fuel in (("SB1", SB1),("SB2", SB2),("SB3", SB3),("SB4", SB4)):
    db[fuel_name] = {"RothFuel": fuel}


# save database in compact mode
db.dump_database(
    filename = "Scott&Burgan",
    info = "30 Fuel type models defied in Scott and Burgan [1]_ for Rothermel rate of spread model.",
    compact = True
)