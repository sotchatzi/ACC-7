FROM quay.io/fenicsproject/stable:current
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y gmsh
RUN apt install -y python-numpy
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install celery==4.1.1
RUN pip3 install celery[redis]
RUN pip3 install pandas
ADD ./murtazo.tar.gz /home/fenics/shared/
# RUN /home/fenics/shared/murtazo/navier_stokes_solver/src/ && ./compile_forms
# RUN /home/fenics/shared/murtazo/navier_stokes_solver/ && cmake . && make -j 1 


