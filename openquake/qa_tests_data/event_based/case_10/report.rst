Event Based Bogota
==================

============== ====================
checksum32     13_057_122          
date           2020-11-02T09:36:05 
engine_version 3.11.0-git82b78631ac
============== ====================

num_sites = 5, num_levels = 4, num_rlzs = 100

Parameters
----------
=============================== ======================================
calculation_mode                'preclassical'                        
number_of_logic_tree_samples    100                                   
maximum_distance                {'default': [(1.0, 100), (10.0, 100)]}
investigation_time              1.0                                   
ses_per_logic_tree_path         1                                     
truncation_level                3.0                                   
rupture_mesh_spacing            5.0                                   
complex_fault_mesh_spacing      5.0                                   
width_of_mfd_bin                0.2                                   
area_source_discretization      10.0                                  
pointsource_distance            None                                  
ground_motion_correlation_model None                                  
minimum_intensity               {}                                    
random_seed                     113                                   
master_seed                     0                                     
ses_seed                        42                                    
=============================== ======================================

Input files
-----------
======================== ==================================================================
Name                     File                                                              
======================== ==================================================================
exposure                 `exposure_model.xml <exposure_model.xml>`_                        
gsim_logic_tree          `logic_tree_gmpe_simplified.xml <logic_tree_gmpe_simplified.xml>`_
job_ini                  `job.ini <job.ini>`_                                              
site_model               `site_model_bog.xml <site_model_bog.xml>`_                        
source_model_logic_tree  `logic_tree_source_model.xml <logic_tree_source_model.xml>`_      
structural_vulnerability `vulnerability_model_bog.xml <vulnerability_model_bog.xml>`_      
======================== ==================================================================

Composite source model
----------------------
====== ============================ =================================================================================================================================================================
grp_id gsim                         rlzs                                                                                                                                                             
====== ============================ =================================================================================================================================================================
0      '[AbrahamsonEtAl2015SInter]' [4, 6, 8, 9, 13, 16, 20, 21, 24, 31, 32, 33, 35, 39, 40, 41, 44, 45, 46, 57, 58, 60, 62, 64, 65, 69, 72, 73, 81, 84, 92, 94, 99]                                 
0      '[YoungsEtAl1997SInter]'     [1, 2, 3, 5, 10, 12, 15, 23, 25, 27, 30, 34, 36, 37, 43, 48, 50, 53, 54, 55, 61, 66, 68, 70, 74, 75, 77, 79, 80, 82, 83, 85, 89, 95, 97, 98]                     
0      '[ZhaoEtAl2006SInter]'       [0, 7, 11, 14, 17, 18, 19, 22, 26, 28, 29, 38, 42, 47, 49, 51, 52, 56, 59, 63, 67, 71, 76, 78, 86, 87, 88, 90, 91, 93, 96]                                       
1      '[AkkarCagnan2010]'          [0, 3, 7, 10, 20, 21, 23, 33, 42, 43, 47, 55, 65, 66, 72, 73, 74, 78, 82, 91, 92, 93, 94]                                                                        
1      '[AkkarEtAlRhyp2014]'        [5, 6, 8, 13, 14, 16, 17, 22, 26, 27, 29, 30, 32, 34, 35, 36, 37, 39, 45, 46, 48, 49, 50, 51, 53, 59, 62, 63, 69, 70, 71, 75, 77, 79, 80, 84, 86, 87, 89, 97, 99]
1      '[BindiEtAl2014Rjb]'         [1, 2, 4, 9, 11, 12, 15, 18, 19, 24, 25, 28, 31, 38, 40, 41, 44, 52, 54, 56, 57, 58, 60, 61, 64, 67, 68, 76, 81, 83, 85, 88, 90, 95, 96, 98]                     
====== ============================ =================================================================================================================================================================

Required parameters per tectonic region type
--------------------------------------------
===== ============================================================================ ========= ============ ==============
et_id gsims                                                                        distances siteparams   ruptparams    
===== ============================================================================ ========= ============ ==============
0     '[AkkarCagnan2010]' '[AkkarEtAlRhyp2014]' '[BindiEtAl2014Rjb]'               rhypo rjb vs30         mag rake      
1     '[AbrahamsonEtAl2015SInter]' '[YoungsEtAl1997SInter]' '[ZhaoEtAl2006SInter]' rrup      backarc vs30 hypo_depth mag
===== ============================================================================ ========= ============ ==============

Exposure model
--------------
=========== =
#assets     5
#taxonomies 4
=========== =

===================== ========== ======= ====== === === =========
taxonomy              num_assets mean    stddev min max num_sites
MCF/LWAL+DUC/HBET:3,6 2          1.00000 0%     1   1   2        
MUR/HBET:4,5          1          1.00000 nan    1   1   1        
CR/LDUAL+DUC          1          1.00000 nan    1   1   1        
CR/LFINF+DUC          1          1.00000 nan    1   1   1        
*ALL*                 5          1.00000 0%     1   1   5        
===================== ========== ======= ====== === === =========

Slowest sources
---------------
========= ==== ========= ========= ============
source_id code calc_time num_sites eff_ruptures
========= ==== ========= ========= ============
CC_57_3   P    3.865E-04 5         15          
CC_57_416 P    2.096E-04 5         15          
CC_02_152 P    1.934E-04 5         108         
CC_03_70  P    1.836E-04 5         108         
CC_02_38  P    1.740E-04 5         108         
CC_03_13  P    1.729E-04 5         108         
CC_64_412 P    1.709E-04 3         84          
CC_03_31  P    1.683E-04 5         108         
CC_03_77  P    1.681E-04 5         108         
CC_02_63  P    1.659E-04 5         108         
CC_57_16  P    1.602E-04 5         15          
CC_57_1   P    1.578E-04 5         15          
CC_64_406 P    1.571E-04 3         84          
CC_67_172 P    1.566E-04 5         63          
CC_57_418 P    1.473E-04 5         15          
CC_02_147 P    1.414E-04 5         108         
CC_57_411 P    1.402E-04 5         15          
CC_57_22  P    1.402E-04 5         15          
CC_02_377 P    1.366E-04 5         108         
CC_67_167 P    1.299E-04 2         63          
========= ==== ========= ========= ============

Computation times by source typology
------------------------------------
==== =========
code calc_time
==== =========
C    0.0      
P    0.01356  
==== =========

Information about the tasks
---------------------------
================== ====== ======= ====== ========= =======
operation-duration counts mean    stddev min       max    
preclassical       18     0.00164 62%    9.260E-04 0.00545
read_source_model  2      0.02439 71%    0.00696   0.04181
================== ====== ======= ====== ========= =======

Data transfer
-------------
================= =============================== ========
task              sent                            received
read_source_model converter=664 B fname=221 B     68.02 KB
preclassical      srcs=87.4 KB srcfilter=32.17 KB 9.25 KB 
================= =============================== ========

Slowest operations
------------------
========================= ========= ========= ======
calc_47282, maxmem=1.5 GB time_sec  memory_mb counts
========================= ========= ========= ======
importing inputs          1.71533   0.57422   1     
composite source model    1.66406   0.57422   1     
total read_source_model   0.04877   1.78906   2     
total preclassical        0.02953   0.43359   18    
reading exposure          5.367E-04 0.0       1     
========================= ========= ========= ======