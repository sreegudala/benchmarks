import openmc
from materials import materials
from surfaces import surfaces

###############################################################################
#                     Create a dictionary of all shared cells
###############################################################################

# Instantiate Cells
cells = {}
cells['Reflector']                          = openmc.Cell(name='Reflector')
cells['UO2 Unrodded Assembly']              = openmc.Cell(name='UO2 Unrodded Assembly')
cells['UO2 Rodded Assembly']                = openmc.Cell(name='UO2 Rodded Assembly')
cells['MOX Unrodded Assembly']              = openmc.Cell(name='MOX Unrodded Assembly')
cells['MOX Rodded Assembly']                = openmc.Cell(name='MOX Rodded Assembly')
cells['Reflector Unrodded Assembly']        = openmc.Cell(name='Water Unrodded Assembly')
cells['Reflector Rodded Assembly']          = openmc.Cell(name='Water Rodded Assembly')
cells['Fine Moderator Mesh Region']         = openmc.Cell(name='Fine Moderator Mesh Region')
cells['Reflector Unrodded Bottom Assembly'] = openmc.Cell(name='Reflector Unrodded Bottom Assembly')
cells['Reflector Unrodded Side Assembly']   = openmc.Cell(name='Reflector Unrodded Side Assembly')
cells['Reflector Unrodded Corner Assembly'] = openmc.Cell(name='Reflector Unrodded Corner Assembly')
cells['Core']                               = openmc.Cell(name='Core')
cells['UO2 Pin']                            = openmc.Cell(name='UO2 Pin')


cells['UO2 Pin'].region                   = +surfaces['Pin Cell ZCylinder'] & \
                                            +surfaces['Pin x-min'] & \
                                            -surfaces['Pin x-max'] & \
                                            +surfaces['Pin y-min'] & \
                                            -surfaces['Pin y-max']
cells['Reflector'].fill                 = materials['Water']
cells['UO2 Pin'].fill                   = materials['Water']


# Divisions should be set to either "original", "with mod", or "subdiv"
divisions = "subdivide"

rodsArray = ["UO2 Pincell", "MOX 4.3% Pincell", "MOX 7.0% Pincell", "MOX 8.7% Pincell", "Fission Chamber Pincell", "Guide Tube Pincell", "Control Rod Pincell"]
matsArray = ["UO2", "MOX 4.3%", "MOX 7.0%", "MOX 8.7%", "Fission Chamber", "Guide Tube", "Control Rod"]
universesArray = []

for rod, mat in zip(rodsArray, matsArray):
    if divisions == "original":
        surfs = [surfaces['Pin Cell ZCylinder']]
        mats  = [materials[mat],materials['Water']]
        subdivs_r = None
        subdivs_a = None
        rad_div_types = None
    elif divisions == "with mod":
        surfs = [surfaces['Pin Cell ZCylinder'],surfaces['Moderator Cylinder']]
        mats  = [materials[mat],materials['Water'],materials['Water']]
        subdivs_r = None
        subdivs_a = None
        rad_div_types = None
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
        rad_div_types = {
                0 : "area",
                1 : "area"
                }
    universesArray.append(openmc.model.pin_radial_azimuthal(surfs, mats, subdivisions_r=subdivs_r, subdivisions_a=subdivs_a, rad_div_types=rad_div_types))

