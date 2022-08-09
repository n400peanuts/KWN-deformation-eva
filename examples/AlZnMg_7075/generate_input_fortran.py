# Generates the input file in the right order for KWN model
import yaml
a_yaml_file = open("input.yaml")
parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)




with open('input.dat', 'w') as f:
		f.write( "%.3e \n" % parsed_yaml_file['kwn_step0'])
		f.write( "%.3e \n" % parsed_yaml_file['kwn_stepsize'])
		f.write( "%d \n" % parsed_yaml_file['kwn_nsteps'])
		f.write( "%f \n" % parsed_yaml_file['T'])
		f.write( "%.3e \n" % parsed_yaml_file['strain_rate'])
		f.write( "%.1e \n" % parsed_yaml_file['lattice_parameter'])
		f.write( "%.1e \n" % parsed_yaml_file['atomic_volume'])
		f.write( "%.1e \n" % parsed_yaml_file['molar_volume'])
		f.write( "%.1e \n" % parsed_yaml_file['misfit_energy'])
		f.write( "%.3f \n" % parsed_yaml_file['gamma_coherent'])
		f.write( "%.4e \n" % parsed_yaml_file['solute_diffusion0'][0])
		f.write( "%.4e \n" % parsed_yaml_file['solute_diffusion0'][1])
		f.write( "%.4e \n" % parsed_yaml_file['solute_migration_energy'][0])
		f.write( "%.4e \n" % parsed_yaml_file['solute_migration_energy'][1])
		f.write( "%.4e \n" % parsed_yaml_file['c0_matrix'][0])
		f.write( "%.4e \n" % parsed_yaml_file['c0_matrix'][1])
		f.write( "%.d \n" % parsed_yaml_file['stoichiometry'][0])
		f.write( "%.d \n" % parsed_yaml_file['stoichiometry'][1])
		f.write( "%.d \n" % parsed_yaml_file['stoichiometry'][2])
		f.write( "%.3e \n" % parsed_yaml_file['vacancy_sink_spacing'])
		f.write( "%.3e \n" % parsed_yaml_file['vacancy_diffusion0'])
		f.write( "%.3e \n" % parsed_yaml_file['jog_formation_energy'])
		f.write( "%.3e \n" % parsed_yaml_file['activation_energy_pipe_diffusion'])
		f.write( "%.3e \n" % parsed_yaml_file['vacancy_formation_energy'])
		f.write( "%.3e \n" % parsed_yaml_file['vacancy_migration_energy'])
		f.write( "%.3e \n" % parsed_yaml_file['dislocation_arrangement'])
		f.write( "%.3e \n" % parsed_yaml_file['vacancy_generation'])
		f.write( "%.3e \n" % parsed_yaml_file['initial_dislocation_density'])
		f.write( "%.3e \n" % parsed_yaml_file['saturation_dislocation_density'])
		f.write( "%.4e \n" % parsed_yaml_file['burgers_vector'])
		f.write( "%.4e \n" % parsed_yaml_file['initial_mean_radius'])
		f.write( "%.4e \n" % parsed_yaml_file['initial_volume_fraction'])
		f.write( "%.4e \n" % parsed_yaml_file['dispersion_parameter'])
		f.write( "%.4e \n" % parsed_yaml_file['time'])
		f.write( "%.4e \n" % parsed_yaml_file['dt_max'])
		f.write( "%.4e \n" % parsed_yaml_file['output_time_step'])
		f.write( "%.4e \n" % parsed_yaml_file['sigma_r'])
		f.write( "%.4e \n" % parsed_yaml_file['A'])
		f.write( "%.4e \n" % parsed_yaml_file['Q_stress'])
		f.write( "%.4e \n" % parsed_yaml_file['n'])
		f.write( "%.4e \n" % parsed_yaml_file['c_eq'][0])
		f.write( "%.4e \n" % parsed_yaml_file['c_eq'][1])
		
		




		
		
		
		
		

		
		

