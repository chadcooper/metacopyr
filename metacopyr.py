# Chad Cooper, CAST
# 3/29/2013
#
# Purpose:
# Takes a XML metadata template produced from the EPA Metadata Tool and a shapefile
#   of polygon raster footprints, gets the raster name and bounding box from the
#   shapefile for each record, and creates a XML metadata file from xml_tmeplate,
#   changing only the filename of the XML file and the bounding box coords in the 
#   metadata.
#
# Usage:
# Create a directory called "xml" in the directory that houses this script, the 
#   template XML file, and the QQ shapefile. Run the Python script, watch the 
#   magic happen. Files get output to the xml subdirectory.

import arcpy
from xml.etree.cElementTree import ElementTree
import shutil
import os

# Assumes below are all in same directory as this script
fc = "QQuads24k_UTM16N_names.shp"
xml_template = "Milwaukee_Template.xml"
output_dir = "xml"

rows = arcpy.SearchCursor(fc)
for row in rows:
    geom = row.shape
    ex = geom.extent
    ex_dict = {"westbc" : ex.XMin,
               "southbc" : ex.YMin,
               "eastbc" : ex.XMax,
               "northbc" : ex.YMax}
    # Get the raster name
    quad_name = row.getValue("Name_qquad")
    # <QQ name>_LULC.xml file path and name
    lulc_xml_out = os.path.join(output_dir, str(quad_name) + "_LULC.img.xml")
    
    # Start the XML work
    tree = ElementTree()
    tree.parse(xml_template)
    for k, v in ex_dict.iteritems():
        corner = tree.find("idinfo/spdom/bounding/" + k)
        corner.text = str(v)
    # <QQ name>_LULC.xml
    tree.write(lulc_xml_out)
    # <QQ name>_TREE.xml
    tree_xml_out = lulc_xml_out.replace("_LULC.img", "_TREE.img")
    shutil.copy(lulc_xml_out, tree_xml_out)
    # <QQ name>.xml
    quadname_only_xml_out = os.path.splitext(tree_xml_out)[0][:-9] + "_poly.shp.xml"
    shutil.copy(tree_xml_out, quadname_only_xml_out)
    