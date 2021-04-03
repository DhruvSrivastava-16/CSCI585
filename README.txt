NOTE: While checking the Q1_Starter_file.kml for displaying the 4 nearest neighbours and 
the convex hull polygon, do tick and untick the folders in the drop down menu on the left side
to see the 4NN and polygon individually. You can see the outputs in screenshots for Query1 and 
Query2.

1.) Creating Table:
CREATE TABLE placemarks_2
	(
	  label_id character varying(50),
	  lat numeric,
	  lon numeric
	);

2.) Inserting into Table:
Insert into placemarks_2 values('Home',-118.28517323153733,34.030708842995864);	
Insert into placemarks_2 values('USC Lawn', -118.28527792518429,34.02695268409571);	 						
Insert into placemarks_2 values('Trader joes', -118.28468101586195,34.02614679285783);							
Insert into placemarks_2 values('BoFA',-118.28412806527946,34.024980456260565);							
Insert into placemarks_2 values('USC Marshall',-118.28542375665306,34.0188810038387);							
Insert into placemarks_2 values('School of Cinema',-118.28651195557973,34.023636647683084);							
Insert into placemarks_2 values('USC Annenberg',-118.28613059452506,34.02217091637391);							
Insert into placemarks_2 values('Cromwell Field',-118.28789253111098,34.02215811478172);							
Insert into placemarks_2 values('USC Thorton',-118.28549331734864,34.02329551559096);							
Insert into placemarks_2 values('Dedeaux Stadium',-118.2895380885991,34.0233844372443);							
Insert into placemarks_2 values('USC Viterbi',-118.28931278303689,34.02073453255963);							
Insert into placemarks_2 values('USC Dornsife',-118.28555769036691,34.02108133686649);							
Insert into placemarks_2 values('Lovine-Young Academy',-118.28866236866935,34.01903767982044);							


3.) Create the geom field:
ALTER TABLE placemarks_2
	ADD COLUMN geom geometry(POINT,4326);


4.) Populating Geom Field
UPDATE placemarks_2 SET geom = ST_SetSRID(ST_MakePoint(lat,lon),4326);


5.) QUERY1:
SELECT ST_AsText(ST_ConvexHull(ST_Collect(geom))) FROM placemarks_2;

OUTPUT:
POLYGON((-118.28542375665306 34.0188810038387,-118.28866236866935 34.01903767982044,-118.28931278303689 34.02073453255963,-118.2895380885991 34.0233844372443,-118.28517323153733 34.030708842995864,-118.28412806527946 34.024980456260565,-118.28542375665306 34.0188810038387))


6.) QUERY2:
SELECT label_id, lon, lat FROM placemarks_2 where label_id != 'Home' ORDER BY geom <-> ST_SetSRID(ST_MakePoint(-118.28517323153733,34.030708842995864),4326) LIMIT 4;


OUTPUT:
"USC Lawn"	34.02695268409571	-118.28527792518429
"Trader joes"	34.02614679285783	-118.28468101586195
"BoFA"	34.024980456260565	-118.28412806527946
"School of Cinema"	34.023636647683084	-118.28651195557973
