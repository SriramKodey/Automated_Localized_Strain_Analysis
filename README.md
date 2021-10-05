# Automated_Localized_Strain_Analysis
  A novel method was developed to perform automatic surface strain analysis. The algorithm could overcome the shortcomings of Harris corner detection and Shi Tomasi algorithm when used with images having noise. The developed software system was deployed on low-cost hardware (generic USB Microscope) and was capable of measuring strain with a maximum error of 1.22%, which is within the limits of ASTM-2218-02 standard.
 
## Publication
  Pankaj W, ***Kodey S***, Suresh K, Radhika S, “A low cost surface strain measurement system using imageprocessing for sheet metal forming applications”, Journal of the International Measurement Confederation (IMEKO) MEAS-D-21-03391R1 - Accepted

## Overview
   1) Single point surface strain analysis using automated measurement of distortion in Square Grid pattern.
   2) Quadrilaterals identified from images of grid patterns captured using a microscope.  
   3) Equations of sides of quadrilateral calculated using Hough Transform and K-Means Clustering.  
   4) Corners of quadrilateral calculated from these equations.
   5) Projective Transformation was applied using the calculated corners to inscribe ellipses inside convex quadrilaterals, for single point surface strain analysis.

## Flowchart Description
<p align="center">
  <img src="/Flowchart/Total_2.jpeg" alt="Flowchart" width="800"/>
</p>


## Results

  ### Output
  <img align="left" src="/Results/result10.jpg" alt="Result" width="400"/>
  
  ### Dimensions
  #### *Major Axis: 419.257 Pixels* 
  #### *Minor Axis: 196.775 Pixels*
   Converted to standard units (mm, cm etc.) by calibrating the setup.
  
  
  
