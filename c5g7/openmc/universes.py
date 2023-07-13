import openmc
from cells import cells, matsArray, universesArray

###############################################################################
#                     Create a dictionary of all shared universes
###############################################################################

universes = {}
universes['Root']                               = openmc.Universe(universe_id=10,  name='Root')
universes['Root']                               .add_cell(cells['Core'])

for mat, universe in zip(matsArray, universesArray):
    universes[mat] = universe

# Instantiate Universes
universes['Reflector']                          = openmc.Universe(universe_id=11, name='Reflector')
universes['UO2 Unrodded Assembly']              = openmc.Universe(universe_id=12, name='UO2 Unrodded Assembly')
universes['UO2 Rodded Assembly']                = openmc.Universe(universe_id=13, name='UO2 Rodded Assembly')
universes['MOX Unrodded Assembly']              = openmc.Universe(universe_id=14, name='MOX Unrodded Assembly')
universes['MOX Rodded Assembly']                = openmc.Universe(universe_id=15, name='MOX Rodded Assembly')
universes['Reflector Unrodded Assembly']        = openmc.Universe(universe_id=16, name='Reflector Unrodded Assembly')
universes['Reflector Rodded Assembly']          = openmc.Universe(universe_id=17, name='Reflector Rodded Assembly')
universes['Reflector Unrodded Bottom Assembly'] = openmc.Universe(universe_id=19, name='Reflector Unrodded Bottom Assembly')
universes['Reflector Unrodded Side Assembly']   = openmc.Universe(universe_id=20, name='Reflector Unrodded Side Assembly')
universes['Reflector Unrodded Corner Assembly'] = openmc.Universe(universe_id=21, name='Reflector Unrodded Corner Assembly')

# Register Cells with Universes
universes['Reflector']                          .add_cell(cells['Reflector'])
universes['UO2 Unrodded Assembly']              .add_cell(cells['UO2 Unrodded Assembly'])
universes['UO2 Rodded Assembly']                .add_cell(cells['UO2 Rodded Assembly'])
universes['MOX Unrodded Assembly']              .add_cell(cells['MOX Unrodded Assembly'])
universes['MOX Rodded Assembly']                .add_cell(cells['MOX Rodded Assembly'])
universes['Reflector Unrodded Assembly']        .add_cell(cells['Reflector Unrodded Assembly'])
universes['Reflector Rodded Assembly']          .add_cell(cells['Reflector Rodded Assembly'])
universes['Reflector Unrodded Bottom Assembly'] .add_cell(cells['Reflector Unrodded Bottom Assembly'])
universes['Reflector Unrodded Side Assembly']   .add_cell(cells['Reflector Unrodded Side Assembly'])
universes['Reflector Unrodded Corner Assembly'] .add_cell(cells['Reflector Unrodded Corner Assembly'])
