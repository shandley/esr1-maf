# ESR1 residue 190 vs estradiol — PyMOL visualization
# Loads 3UUD (LBD + estradiol) and AlphaFold full-length model,
# superimposes on the shared LBD region, then shows residue 190 and EST.

reinitialize

# Load structures
load structure_data/3UUD.pdb, crystal
load structure_data/AF-P03372-F1.pdb, alphafold

# Superimpose AlphaFold onto crystal using LBD backbone (residues 305-549)
align alphafold and chain A and resi 305-549 and name CA, crystal and chain A and resi 305-549 and name CA

# Visual style
hide everything
bg_color white

# Crystal: show LBD as cartoon (light gray), EST as sticks
show cartoon, crystal and chain A
color gray80, crystal and chain A
show sticks, crystal and resn EST
color tv_yellow, crystal and resn EST
show spheres, crystal and resn EST
set sphere_scale, 0.25, crystal and resn EST

# AlphaFold: show full protein as cartoon (light blue)
show cartoon, alphafold
color lightblue, alphafold

# Highlight residue 190 in AlphaFold as sticks
show sticks, alphafold and resi 190
color tv_red, alphafold and resi 190
show spheres, alphafold and resi 190
set sphere_scale, 0.25, alphafold and resi 190

# Label the key residue and ligand
label alphafold and resi 190 and name CA, "Res 190"
label crystal and resn EST and name C1, "Estradiol"

# Measure and display distance (closest heavy atom to EST)
distance d_190_EST, alphafold and resi 190, crystal and resn EST, cutoff=999, mode=0

# Zoom to show both residue 190 and EST with context
select region_of_interest, (alphafold and resi 190) or (crystal and resn EST)
zoom region_of_interest, 20
deselect

# Show the distance label clearly
set label_size, 14
set label_color, black

# Orient nicely
orient region_of_interest

print "ESR1 structure loaded."
print "Red sticks = residue 190 (DBD, AlphaFold model)"
print "Yellow sticks = estradiol (LBD, 3UUD crystal structure)"
print "Distance object 'd_190_EST' shows closest atom pair."
