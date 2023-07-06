import openmc
from materials import materials
from surfaces import surfaces

###############################################################################
#                     Create a dictionary of all shared cells
###############################################################################

# Instantiate Cells
cells = {}
cells['UO2']                         = openmc.Cell(name='UO2')
cells['MOX 4.3%']                    = openmc.Cell(name='MOX 4.3%')
cells['MOX 7.0%']                    = openmc.Cell(name='MOX 7.0%')
cells['MOX 8.7%']                    = openmc.Cell(name='MOX 8.7%')
cells['Fission Chamber']             = openmc.Cell(name='Fission Chamber')
cells['Guide Tube']                  = openmc.Cell(name='Guide Tube')
cells['Reflector']                   = openmc.Cell(name='Reflector')
cells['Control Rod']                 = openmc.Cell(name='Control Rod')
cells['UO2 Moderator']               = openmc.Cell(name='UO2 Moderator')
cells['MOX 4.3% Moderator']          = openmc.Cell(name='MOX 4.3% Moderator')
cells['MOX 7.0% Moderator']          = openmc.Cell(name='MOX 7.0% Moderator')
cells['MOX 8.7% Moderator']          = openmc.Cell(name='MOX 8.7% Moderator')
cells['Fission Chamber Moderator']   = openmc.Cell(name='Fission Chamber Moderator')
cells['Guide Tube Moderator']        = openmc.Cell(name='Guide Tube Moderator')
cells['Control Rod Moderator']       = openmc.Cell(name='Control Rod Moderator')
cells['UO2 Unrodded Assembly']       = openmc.Cell(name='UO2 Unrodded Assembly')
cells['UO2 Rodded Assembly']         = openmc.Cell(name='UO2 Rodded Assembly')
cells['MOX Unrodded Assembly']       = openmc.Cell(name='MOX Unrodded Assembly')
cells['MOX Rodded Assembly']         = openmc.Cell(name='MOX Rodded Assembly')
cells['Reflector Unrodded Assembly'] = openmc.Cell(name='Water Unrodded Assembly')
cells['Reflector Rodded Assembly']   = openmc.Cell(name='Water Rodded Assembly')
cells['Core']                        = openmc.Cell(name='Core')
cells['UO2 Pin']                     = openmc.Cell(name='UO2 Pin')

# Use surface half-spaces to define regions
cells['UO2'].region                       = -surfaces['Pin Cell ZCylinder']
cells['MOX 4.3%'].region                  = -surfaces['Pin Cell ZCylinder']
cells['MOX 7.0%'].region                  = -surfaces['Pin Cell ZCylinder']
cells['MOX 8.7%'].region                  = -surfaces['Pin Cell ZCylinder']
cells['Fission Chamber'].region           = -surfaces['Pin Cell ZCylinder']
cells['Guide Tube'].region                = -surfaces['Pin Cell ZCylinder']
cells['Control Rod'].region               = -surfaces['Pin Cell ZCylinder']
cells['UO2 Moderator'].region             = +surfaces['Pin Cell ZCylinder']
cells['MOX 4.3% Moderator'].region        = +surfaces['Pin Cell ZCylinder']
cells['MOX 7.0% Moderator'].region        = +surfaces['Pin Cell ZCylinder']
cells['MOX 8.7% Moderator'].region        = +surfaces['Pin Cell ZCylinder']
cells['Fission Chamber Moderator'].region = +surfaces['Pin Cell ZCylinder']
cells['Guide Tube Moderator'].region      = +surfaces['Pin Cell ZCylinder']
cells['Control Rod Moderator'].region     = +surfaces['Pin Cell ZCylinder']
cells['UO2 Pin'].region                   = +surfaces['Pin Cell ZCylinder'] & \
                                            +surfaces['Pin x-min'] & \
                                            -surfaces['Pin x-max'] & \
                                            +surfaces['Pin y-min'] & \
                                            -surfaces['Pin y-max']

# Register Materials with Cells
cells['UO2'].fill                       = materials['UO2']
cells['MOX 4.3%'].fill                  = materials['MOX 4.3%']
cells['MOX 7.0%'].fill                  = materials['MOX 7.0%']
cells['MOX 8.7%'].fill                  = materials['MOX 8.7%']
cells['Fission Chamber'].fill           = materials['Fission Chamber']
cells['Guide Tube'].fill                = materials['Guide Tube']
cells['Control Rod'].fill               = materials['Control Rod']
cells['UO2 Moderator'].fill             = materials['Water']
cells['MOX 4.3% Moderator'].fill        = materials['Water']
cells['MOX 7.0% Moderator'].fill        = materials['Water']
cells['MOX 8.7% Moderator'].fill        = materials['Water']
cells['Fission Chamber Moderator'].fill = materials['Water']
cells['Guide Tube Moderator'].fill      = materials['Water']
cells['Control Rod Moderator'].fill     = materials['Water']
cells['Reflector'].fill                 = materials['Water']
cells['UO2 Pin'].fill                   = materials['Water']




divisions = "subdiv"

cells['UO2 Pincell']                    = openmc.Cell(name='UO2 Pincell')
cells['UO2 Pincell'].region             = surfaces['Box']
if divisions == "original":
    surfs = [surfaces['Pin Cell ZCylinder']]
    mats  = [materials['UO2'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['UO2 Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
elif divisions == "with mod":
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['UO2'],materials['Water'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['UO2 Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
else:
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['UO2'],materials['Water'],materials['Water']]
    subdivs_r = {
            0 : 3,
            1 : 3
            }
    subdivs_a = {
            0 : 8,
            1 : 8
            }
    cells['UO2 Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)


cells['MOX 4.3% Pincell']                    = openmc.Cell(name='MOX 4.3% Pincell')
cells['MOX 4.3% Pincell'].region             = surfaces['Box']
if divisions == "original":
    surfs = [surfaces['Pin Cell ZCylinder']]
    mats  = [materials['MOX 4.3%'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['MOX 4.3% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
elif divisions == "with mod":
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['MOX 4.3%'],materials['Water'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['MOX 4.3% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
else:
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['MOX 4.3%'],materials['Water'],materials['Water']]
    subdivs_r = {
            0 : 3,
            1 : 3
            }
    subdivs_a = {
            0 : 8,
            1 : 8
            }
    cells['MOX 4.3% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)


cells['MOX 7.0% Pincell']                    = openmc.Cell(name='MOX 7.0% Pincell')
cells['MOX 7.0% Pincell'].region             = surfaces['Box']
if divisions == "original":
    surfs = [surfaces['Pin Cell ZCylinder']]
    mats  = [materials['MOX 7.0%'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['MOX 7.0% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
elif divisions == "with mod":
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['MOX 7.0%'],materials['Water'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['MOX 7.0% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
else:
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['MOX 7.0%'],materials['Water'],materials['Water']]
    subdivs_r = {
            0 : 3,
            1 : 3
            }
    subdivs_a = {
            0 : 8,
            1 : 8
            }
    cells['MOX 7.0% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)


cells['MOX 8.7% Pincell']                    = openmc.Cell(name='MOX 8.7% Pincell')
cells['MOX 8.7% Pincell'].region             = surfaces['Box']
if divisions == "original":
    surfs = [surfaces['Pin Cell ZCylinder']]
    mats  = [materials['MOX 8.7%'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['MOX 8.7% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
elif divisions == "with mod":
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['MOX 8.7%'],materials['Water'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['MOX 8.7% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
else:
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['MOX 8.7%'],materials['Water'],materials['Water']]
    subdivs_r = {
            0 : 3,
            1 : 3
            }
    subdivs_a = {
            0 : 8,
            1 : 8
            }
    cells['MOX 8.7% Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)


cells['Fission Chamber Pincell']                    = openmc.Cell(name='Fission Chamber Pincell')
cells['Fission Chamber Pincell'].region             = surfaces['Box']
if divisions == "original":
    surfs = [surfaces['Pin Cell ZCylinder']]
    mats  = [materials['Fission Chamber'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['Fission Chamber Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
elif divisions == "with mod":
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['Fission Chamber'],materials['Water'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['Fission Chamber Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
else:
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['Fission Chamber'],materials['Water'],materials['Water']]
    subdivs_r = {
            0 : 3,
            1 : 3
            }
    subdivs_a = {
            0 : 8,
            1 : 8
            }
    cells['Fission Chamber Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)


cells['Guide Tube Pincell']                    = openmc.Cell(name='Guide Tube Pincell')
cells['Guide Tube Pincell'].region             = surfaces['Box']
if divisions == "original":
    surfs = [surfaces['Pin Cell ZCylinder']]
    mats  = [materials['Guide Tube'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['Guide Tube Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
elif divisions == "with mod":
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['Guide Tube'],materials['Water'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['Guide Tube Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
else:
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['Guide Tube'],materials['Water'],materials['Water']]
    subdivs_r = {
            0 : 3,
            1 : 3
            }
    subdivs_a = {
            0 : 8,
            1 : 8
            }
    cells['Guide Tube Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)


cells['Control Rod Pincell']                    = openmc.Cell(name='Control Rod Pincell')
cells['Control Rod Pincell'].region             = surfaces['Box']
if divisions == "original":
    surfs = [surfaces['Pin Cell ZCylinder']]
    mats  = [materials['Control Rod'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['Control Rod Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
elif divisions == "with mod":
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['Control Rod'],materials['Water'],materials['Water']]
    subdivs_r = None
    subdivs_a = None
    cells['Control Rod Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)
else:
    surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
    mats  = [materials['Control Rod'],materials['Water'],materials['Water']]
    subdivs_r = {
            0 : 3,
            1 : 3
            }
    subdivs_a = {
            0 : 8,
            1 : 8
            }
    cells['Control Rod Pincell'].fill = openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a)


