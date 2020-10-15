# Container
* run docker_shell.sh and automatically runs the whole procedure of creating the docker installing the neccesary packages and the solver with the help of commands_container.sh which run the commands inside the container.
* build dockerfile problem :
-- Checking for one of the modules 'craypetsc_real;PETSc'
CMake Error at /usr/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  PETSc could not be found.  Be sure to set PETSC_DIR.  (missing:
  PETSC_FOUND)
Call Stack (most recent call first):
  /usr/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  /usr/local/share/dolfin/cmake/FindPETSc.cmake:226 (find_package_handle_standard_args)
  /usr/local/share/dolfin/cmake/UseDOLFIN.cmake:40 (find_package)
  CMakeLists.txt:14 (include)


