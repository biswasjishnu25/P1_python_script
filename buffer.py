import arcpy

# setting the default workspace
arcpy.env.workspace = r"D:\3rd_semester\Programming_for_GIS_III\P1_python_script\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

# Perform buffer operation

arcpy.analysis.Buffer("Wilson_Schools","Willson_school_buffer", "500 meters")
print("Process complete")