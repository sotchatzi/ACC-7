#!/bin/bash
tar xzvf murtazo.tgz
cd /home/fenics/shared/murtazo
tar xvf cloudnaca.tgz
tar xvf navier_stokes_solver.tar
cd /home/fenics/shared/murtazo/navier_stokes_solver/src/
sudo ./compile_forms
cd ..
sudo cmake .
sudo make -j 1
cd /home/fenics/shared/murtazo/cloudnaca
sudo apt-get update
sudo apt-get install -y gmsh
cp /home/fenics/shared/runme.sh /home/fenics/shared/murtazo/cloudnaca
sudo apt-get install -y python-numpy
cd /home/fenics/shared/murtazo/cloudnaca
sudo ./runme.sh 0 30 10 200 3
cd /home/fenics/shared/murtazo/cloudnaca/msh
sudo dolfin-convert r2a15n200.msh r2a15n200.xml
cd /home/fenics/shared/murtazo/navier_stokes_solver
sudo ./airfoil  10 0.0001 10. 1 /home/fenics/shared/murtazo/cloudnaca/msh/r2a15n200.xml

