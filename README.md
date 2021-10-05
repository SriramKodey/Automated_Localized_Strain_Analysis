# Automated_Localized_Strain_Analysis

## Publication
  Pankaj W, ***Kodey S***, Suresh K, Radhika S, “A low cost surface strain measurement system using imageprocessing for sheet metal forming applications”, Journal of the International Measurement Confederation (IMEKO) MEAS-D-21-03391R1 - Accepted

## Overview
   1) Single point surface strain analysis using automated measurement of distortion in Square Gridpattern.  (A novel method was developed)
   2) Quadrilaterals identified from images of grid patterns captured using a microscope.  
   3) Equations of sides of quadrilateral calculated using Hough Transform and K-Means Clustering.  
   4) Corners of quadrilateral calculated from these equations.
   5) Projective Transformation was applied using the calculated corners to inscribe ellipses inside convex quadrilaterals, for single point surface strain analysis.

## Flowchart Description
![Flowchart](/Flowchart/Total_2.jpeg)

<p><br><p>

## Results
### Input
![Test_Images](/Test_Images/test10.jpg)
