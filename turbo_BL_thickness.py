# Calculate the bounardy layer thickness along the blades of a turbomachine.

def bl_thickness(TurboType)"
	"""
	Function to calculate the boundary layer thickness for either a compressor or turbine blade.
	
	Arguments
	:param TurboType: str indicating either 'Turbine' or 'Compressor'

	if TurboType == 'Turbine':
		bl_thickness = 'Thick'
	elif TurboType == 'Compressor':
		bl_thickness = 'Thicker'
	else:
		raise ValueError('That is not even a valid turbomachine type.')
	
	return bl_thickness
