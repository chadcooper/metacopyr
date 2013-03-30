metacopyr
=========

Takes a template metadata XML file and a polygon footprints shapefile and lets you create a new XML metadata file for every record in the shapefile. Changes some attributes in the target XML file.

This was a one-off for a co-worker that had 80 rasters he needed to really quickly build metadata for, as in he needed them by COB of that day and there was no way he could manually generate them all in ArcCatalog of with the EPA Metadata Tool. All that needed to be different on each metadata file was the filename and the bounding box of the raster. 

He had a shapefile of the bounding boxes of all the rasters that had a field with the raster name in it. This code simply iterates through each record of the shapefile (1 for each of the 80 rasters), gets the bounding box of the polygon and name from a attribute field, inserts the bounding box into a template XML file he created, and saves out the XML with the raster name we acquired from the shapefile attribute table.
