#!/bin/bash

procs=4

foamCleanTutorials
rm -rf 0 	> /dev/null 2>&1

surfaceFeatureExtract > log.surfaceFeatureExtract
blockMesh > log.blockMesh



##serial mesh and autopatch at mesh level

#snappyHexMesh -overwrite > log.snappyHexMesh
#checkMesh > log.checkMesh
##autoPatch 60 -overwrite > log.autoPatch
##createPatch -overwrite > log.createPatch
#snappyHexMesh -dict system/snappyHexMeshDict_bl -overwrite > log.snappyHexMesh_bl



decomposePar
mpirun -np $procs snappyHexMesh -overwrite -parallel > log.snappyHexMesh
#mpirun -np $procs checkMesh -parallel > log.checkmesh

#mpirun -np $procs snappyHexMesh -dict system/snappyHexMeshDict_bl -overwrite -parallel > log.snappyHexMesh

reconstructParMesh -constant

rm -rf 0 	> /dev/null 2>&1
cp -r 0_org 0 	> /dev/null 2>&1

#decomposePar -force
decomposePar -fields
mpirun -np $procs checkMesh -parallel > log.checkmesh

#decomposePar
mpirun -np $procs simpleFoam -parallel > log.solver
reconstructPar -latestTime
