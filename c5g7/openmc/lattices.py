import openmc
import openmc.mgxs
from universes import universes, cells

###############################################################################
#                     Create a dictionary of the assembly lattices
###############################################################################

# Instantiate the Lattices
lattices = {}
lattices['UO2 Unrodded Assembly'] = \
    openmc.RectLattice(lattice_id=101, name='UO2 Unrodded Assembly')
lattices['UO2 Unrodded Assembly'].dimension = [17, 17]
lattices['UO2 Unrodded Assembly'].lower_left = [-10.71, -10.71]
lattices['UO2 Unrodded Assembly'].pitch = [1.26, 1.26]
u = universes['UO2']
g = universes['Guide Tube']
f = universes['Fission Chamber']
lattices['UO2 Unrodded Assembly'].universes = \
    [[u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, g, u, u, g, u, u, g, u, u, u, u, u],
     [u, u, u, g, u, u, u, u, u, u, u, u, u, g, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, g, u, u, g, u, u, g, u, u, g, u, u, g, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, g, u, u, g, u, u, f, u, u, g, u, u, g, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, g, u, u, g, u, u, g, u, u, g, u, u, g, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, g, u, u, u, u, u, u, u, u, u, g, u, u, u],
     [u, u, u, u, u, g, u, u, g, u, u, g, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]]

lattices['UO2 Rodded Assembly'] = \
    openmc.RectLattice(lattice_id=102, name='UO2 Rodded Assembly')
lattices['UO2 Rodded Assembly'].dimension = [17, 17]
lattices['UO2 Rodded Assembly'].lower_left = [-10.71, -10.71]
lattices['UO2 Rodded Assembly'].pitch = [1.26, 1.26]
u = universes['UO2']
r = universes['Control Rod']
f = universes['Fission Chamber']
lattices['UO2 Rodded Assembly'].universes = \
    [[u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
     [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, r, u, u, r, u, u, f, u, u, r, u, u, r, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
     [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]]

lattices['MOX Unrodded Assembly'] = \
    openmc.RectLattice(lattice_id=103, name='MOX Unrodded Assembly')
lattices['MOX Unrodded Assembly'].dimension = [17, 17]
lattices['MOX Unrodded Assembly'].lower_left = [-10.71, -10.71]
lattices['MOX Unrodded Assembly'].pitch = [1.26, 1.26]
m = universes['MOX 4.3%']
n = universes['MOX 7.0%']
o = universes['MOX 8.7%']
g = universes['Guide Tube']
f = universes['Fission Chamber']
lattices['MOX Unrodded Assembly'].universes = \
    [[m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
     [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
     [m, n, n, n, n, g, n, n, g, n, n, g, n, n, n, n, m],
     [m, n, n, g, n, o, o, o, o, o, o, o, n, g, n, n, m],
     [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
     [m, n, g, o, o, g, o, o, g, o, o, g, o, o, g, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, g, o, o, g, o, o, f, o, o, g, o, o, g, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, g, o, o, g, o, o, g, o, o, g, o, o, g, n, m],
     [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
     [m, n, n, g, n, o, o, o, o, o, o, o, n, g, n, n, m],
     [m, n, n, n, n, g, n, n, g, n, n, g, n, n, n, n, m],
     [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
     [m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]]

lattices['MOX Rodded Assembly'] = \
    openmc.RectLattice(lattice_id=104, name='MOX Rodded Assembly')
lattices['MOX Rodded Assembly'].dimension = [17, 17]
lattices['MOX Rodded Assembly'].lower_left = [-10.71, -10.71]
lattices['MOX Rodded Assembly'].pitch = [1.26, 1.26]
m = universes['MOX 4.3%']
n = universes['MOX 7.0%']
o = universes['MOX 8.7%']
r = universes['Control Rod']
f = universes['Fission Chamber']
lattices['MOX Rodded Assembly'].universes = \
    [[m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
     [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
     [m, n, n, n, n, r, n, n, r, n, n, r, n, n, n, n, m],
     [m, n, n, r, n, o, o, o, o, o, o, o, n, r, n, n, m],
     [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
     [m, n, r, o, o, r, o, o, r, o, o, r, o, o, r, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, r, o, o, r, o, o, f, o, o, r, o, o, r, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
     [m, n, r, o, o, r, o, o, r, o, o, r, o, o, r, n, m],
     [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
     [m, n, n, r, n, o, o, o, o, o, o, o, n, r, n, n, m],
     [m, n, n, n, n, r, n, n, r, n, n, r, n, n, n, n, m],
     [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
     [m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]]


lattices['Reflector Unrodded Assembly'] = \
    openmc.RectLattice(lattice_id=105, name='Reflector Unrodded Assembly')
lattices['Reflector Unrodded Assembly'].dimension = [1, 1]
lattices['Reflector Unrodded Assembly'].lower_left = [-10.71, -10.71]
lattices['Reflector Unrodded Assembly'].pitch = [21.42, 21.42]
w = universes['Reflector']
lattices['Reflector Unrodded Assembly'].universes = [[w]]


lattices['Reflector Rodded Assembly'] = \
    openmc.RectLattice(lattice_id=106, name='Reflector Rodded Assembly')
lattices['Reflector Rodded Assembly'].dimension = [17, 17]
lattices['Reflector Rodded Assembly'].lower_left = [-10.71, -10.71]
lattices['Reflector Rodded Assembly'].pitch = [1.26, 1.26]
u = universes['Reflector']
r = universes['Control Rod']
lattices['Reflector Rodded Assembly'].universes = \
    [[u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
     [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, r, u, u, r, u, u, u, u, u, r, u, u, r, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
     [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
     [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]]


fine_mod_dim = 10
lattices['Fine Moderator Mesh Lattice'] = \
        openmc.RectLattice(lattice_id=107, name='Fine Moderator Mesh Lattice')
lattices['Fine Moderator Mesh Lattice'].dimension = [fine_mod_dim, fine_mod_dim]
lattices['Fine Moderator Mesh Lattice'].lower_left = [-0.63, -0.63]
lattices['Fine Moderator Mesh Lattice'].pitch = [1.26/fine_mod_dim, 1.26/fine_mod_dim]
w = universes['Reflector']
lattices['Fine Moderator Mesh Lattice'].universes = [[w]*fine_mod_dim]*fine_mod_dim
lattices['Fine Moderator Mesh Lattice'].outer = w
cells['Fine Moderator Mesh Region'].fill            = lattices['Fine Moderator Mesh Lattice']
universes['Fine Moderator Mesh Region']         = openmc.Universe(universe_id=18, name='Fine Moderator Mesh Region')
universes['Fine Moderator Mesh Region']         .add_cell(cells['Fine Moderator Mesh Region'])


lattices['Reflector Unrodded Bottom/Side Assembly Lattice'] = \
        openmc.RectLattice(lattice_id=108, name='Reflector Unrodded Bottom/Side Assembly Lattice')
lattices['Reflector Unrodded Bottom/Side Assembly Lattice'].dimension = [17, 17]
lattices['Reflector Unrodded Bottom/Side Assembly Lattice'].lower_left = [-10.71, -10.71]
lattices['Reflector Unrodded Bottom/Side Assembly Lattice'].pitch = [1.26, 1.26]
w = universes['Reflector']
f = universes['Fine Moderator Mesh Region']
lattices['Reflector Unrodded Bottom/Side Assembly Lattice'].universes = \
    [[f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]


lattices['Reflector Unrodded Corner Assembly Lattice'] = \
        openmc.RectLattice(lattice_id=109, name='Reflector Unrodded Corner Assembly Lattice')
lattices['Reflector Unrodded Corner Assembly Lattice'].dimension = [17, 17]
lattices['Reflector Unrodded Corner Assembly Lattice'].lower_left = [-10.71, -10.71]
lattices['Reflector Unrodded Corner Assembly Lattice'].pitch = [1.26, 1.26]
w = universes['Reflector']
f = universes['Fine Moderator Mesh Region']
lattices['Reflector Unrodded Corner Assembly Lattice'].universes = \
    [[f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [f, f, f, f, f, f, f, f, f, f, f, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
     [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]



# Add lattice to cells
cells['UO2 Unrodded Assembly'].fill                 = lattices['UO2 Unrodded Assembly']
cells['UO2 Rodded Assembly'].fill                   = lattices['UO2 Rodded Assembly']
cells['MOX Unrodded Assembly'].fill                 = lattices['MOX Unrodded Assembly']
cells['MOX Rodded Assembly'].fill                   = lattices['MOX Rodded Assembly']
cells['Reflector Unrodded Assembly'].fill           = lattices['Reflector Unrodded Assembly']
cells['Reflector Rodded Assembly'].fill             = lattices['Reflector Rodded Assembly']
cells['Reflector Unrodded Bottom Assembly'].fill    = lattices['Reflector Unrodded Bottom/Side Assembly Lattice']
cells['Reflector Unrodded Side Assembly'].fill      = lattices['Reflector Unrodded Bottom/Side Assembly Lattice']
cells['Reflector Unrodded Side Assembly'].rotation  = [0, 0, 90]
cells['Reflector Unrodded Corner Assembly'].fill    = lattices['Reflector Unrodded Corner Assembly Lattice']
