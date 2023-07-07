import openmc
from cells import cells, matsArray, universesArray

###############################################################################
#                     Create a dictionary of all shared universes
###############################################################################

# Instantiate Universes
universes = {}
universes['Root']                        = openmc.Universe(universe_id=10,  name='Root')
universes['UO2']                         = openmc.Universe(universe_id=11,  name='UO2')
universes['MOX 4.3%']                    = openmc.Universe(universe_id=12,  name='MOX 4.3%')
universes['MOX 7.0%']                    = openmc.Universe(universe_id=13,  name='MOX 7.0%')
universes['MOX 8.7%']                    = openmc.Universe(universe_id=14,  name='MOX 8.7%')
universes['Fission Chamber']             = openmc.Universe(universe_id=15,  name='Fission Chamber')
universes['Guide Tube']                  = openmc.Universe(universe_id=16,  name='Guide Tube')
universes['Control Rod']                 = openmc.Universe(universe_id=17,  name='Control Rod')
universes['Reflector']                   = openmc.Universe(universe_id=18,  name='Reflector')
universes['UO2 Unrodded Assembly']       = openmc.Universe(universe_id=19,  name='UO2 Unrodded Assembly')
universes['UO2 Rodded Assembly']         = openmc.Universe(universe_id=20, name='UO2 Rodded Assembly')
universes['MOX Unrodded Assembly']       = openmc.Universe(universe_id=21, name='MOX Unrodded Assembly')
universes['MOX Rodded Assembly']         = openmc.Universe(universe_id=22, name='MOX Rodded Assembly')
universes['Reflector Unrodded Assembly'] = openmc.Universe(universe_id=23, name='Reflector Unrodded Assembly')
universes['Reflector Rodded Assembly']   = openmc.Universe(universe_id=24, name='Reflector Rodded Assembly')


# Register Cells with Universes
universes['Root']                       .add_cell(cells['Core'])


for mat, universe in zip(matsArray, universesArray):
    universes[mat] = universe


universes['Reflector']                  .add_cell(cells['Reflector'])
universes['UO2 Unrodded Assembly']      .add_cell(cells['UO2 Unrodded Assembly'])
universes['UO2 Rodded Assembly']        .add_cell(cells['UO2 Rodded Assembly'])
universes['MOX Unrodded Assembly']      .add_cell(cells['MOX Unrodded Assembly'])
universes['MOX Rodded Assembly']        .add_cell(cells['MOX Rodded Assembly'])
universes['Reflector Unrodded Assembly'].add_cell(cells['Reflector Unrodded Assembly'])
universes['Reflector Rodded Assembly']  .add_cell(cells['Reflector Rodded Assembly'])
