selected_cell = 5

volume = (relabeled == regionprops[selected_cell].label).transpose(1, 2, 0)

verts, faces, _, _ = measure.marching_cubes_lewiner(volume, level=0, spacing=tuple(spacing))
surface_area_actual = measure.mesh_surface_area(verts, faces)
print("Surface area (actual): {:0.2f}".format(surface_area_actual))
