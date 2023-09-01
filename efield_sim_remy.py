import os
import numpy as np
from simnibs import sim_struct, run_simnibs, msh

# Set the subjects
subjects = ['sub-011_pre', 'sub-011_post', 'sub-012_pre', 'sub-012_post', 'sub-013_pre', 'sub-013_post', 'sub-014_pre', 'sub-014_post', 'sub-015_pre', 'sub-015_post', 'sub-016_pre', 'sub-016_post']

# Set a TMSLIST structure with the simulation set-up
tmslist = sim_struct.TMSLIST()

# Define coil parameters
coil = tmslist.add_coil()
coil.fnamecoil = 'Magstim_70mm_Fig8.nii.gz'
coil.didt = 1e6
coil.pos = 'C3'
coil.moments = [0, 0, 1]

# Create main results folder
if not os.path.exists('Remy_TBS_group_analysis'):
    os.mkdir('Remy_TBS_group_analysis')

# Run the simulation in each subject
for sub in subjects:
    s = sim_struct.SESSION()
    s.map_to_fsavg = True
    s.map_to_MNI = True
    s.fields = 'eEjJ'
    s.subpath = 'm2m_' + sub
    s.pathfem = os.path.join('Remy_TBS_group_analysis', sub)
    s.open_in_gmsh = False
    s.add_poslist(tmslist)
    run_simnibs(s)

# Collect results and calculate the average and standard deviation of the electric field
results_folder = 'fsavg_overlays'
fsavg_msh_name = '_TMS_1_scalar_fsavg.msh'
field_name = 'E_normal'

fields = []
for sub in subjects:
    results_fsavg = msh.read_msh(
        os.path.join('Remy_TBS_group_analysis', sub, results_folder, sub + fsavg_msh_name)
    )
    fields.append(results_fsavg.field[field_name].value)

fields = np.vstack(fields)
avg_field = np.mean(fields, axis=0)
std_field = np.std(fields, axis=0)

results_fsavg.nodedata = []
results_fsavg.add_node_field(avg_field, 'E_normal_avg')
results_fsavg.add_node_field(std_field, 'E_normal_std')

# Visualize and show the average electric fields on the head mesh
view = results_fsavg.view()
view.show(visible_fields='E_normal_avg')

# Print results
print(f"Average induced electric field (across subjects): {avg_field.mean():.2f} V/m")
print(f"Standard deviation of induced electric field (across subjects): {std_field.mean():.2f} V/m")
