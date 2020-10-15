FROM quay.io/fenicsproject/stable:current

WORKDIR /home/fenics/shared

#ADD murtazo.tgz /home/fenics/shared

#RUN cd /home/fenics/shared/murtazo && tar xvf cloudnaca.tgz

ADD cloudnaca.tgz /home/fenics/shared 

ADD navier_stokes_solver.tar /home/fenics/shared 

RUN cd navier_stokes_solver/src && sudo ./compile_forms 
RUN cd /home/fenics/shared/navier_stokes_solver && sudo cmake . && sudo  make -j 1

#RUN apt-get update

#RUN cd cloudnaca && apt-get install -y gmsh

#ADD runme.sh /home/fenics/shared/cloudnaca

#RUN apt-get install -y python-numpy

