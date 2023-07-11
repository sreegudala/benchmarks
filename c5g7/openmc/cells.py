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


cells['UO2 Pin'].region                   = +surfaces['Pin Cell ZCylinder'] & \
                                            +surfaces['Pin x-min'] & \
                                            -surfaces['Pin x-max'] & \
                                            +surfaces['Pin y-min'] & \
                                            -surfaces['Pin y-max']
cells['Reflector'].fill                 = materials['Water']
cells['UO2 Pin'].fill                   = materials['Water']

'''
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
'''



# Divisions should be set to either "original", "with mod", or "subdiv"
divisions = "subdiv"

rodsArray = ["UO2 Pincell", "MOX 4.3% Pincell", "MOX 7.0% Pincell", "MOX 8.7% Pincell", "Fission Chamber Pincell", "Guide Tube Pincell", "Control Rod Pincell"]
matsArray = ["UO2", "MOX 4.3%", "MOX 7.0%", "MOX 8.7%", "Fission Chamber", "Guide Tube", "Control Rod"]
universesArray = []

for rod, mat in zip(rodsArray, matsArray):
    if divisions == "original":
        surfs = [surfaces['Pin Cell ZCylinder']]
        mats  = [materials[mat],materials['Water']]
        subdivs_r = None
        subdivs_a = None
    elif divisions == "with mod":
        surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
        mats  = [materials[mat],materials['Water'],materials['Water']]
        subdivs_r = None
        subdivs_a = None
    else:
        surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
        mats  = [materials[mat],materials['Water'],materials['Water']]
        subdivs_r = {
                0 : 3,
                1 : 3
                }
        subdivs_a = {
                0 : 8,
                1 : 8
                }
    universesArray.append(openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a, rad_div_type=0))

