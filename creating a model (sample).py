import bpy
 
# Create a material.
mat = bpy.data.materials.new(name = 'my_material')
 
# Set some properties of the material.
mat.diffuse_color = (1., 0., 0.)
mat.diffuse_shader = 'LAMBERT' 
mat.diffuse_intensity = 1.0 
mat.specular_color = (1., 1., 1.)
mat.specular_shader = 'COOKTORR'
mat.specular_intensity = 0.5
mat.alpha = 1
mat.ambient = 1
 
# Create a basic cube.
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.object
 
# Assign the material to the cube.
mesh = cube.data
mesh.materials.append(mat