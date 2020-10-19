import subprocess
import pandas as pd
from glob import glob
from celery import Celery

app = Celery('tasks', broker='amqp://js:js@192.168.2.162/jsvhost', backend='redis://:js@192.168.2.162/0')

WORK_DIR = '/home/fenics/shared/murtazo'
GMSH_DIR = WORK_DIR + '/cloudnaca'
AIRFOIL_DIR = WORK_DIR + '/navier_stokes_solver'

@app.task
def test():
    return "this is a test"

@app.task
def airfoil_task(angle, n_nodes, n_levels, speed, time):
    mesh_xml_file = f'{GMSH_DIR}/msh/r{n_levels}a{angle}n{n_nodes}.xml'
    if not glob(mesh_xml_file):
        subprocess.run([
            f'{GMSH_DIR}/runme.sh', 
            f'{angle} {angle} 1 {n_nodes} {n_levels}'], cwd=GMSH_DIR)
        subprocess.run([
            f'dolfin-convert', 
            f'{GMSH_DIR}/msh/r{n_levels}a{angle}n{n_nodes}.msh', mesh_xml_file], cwd=GMSH_DIR)
    subprocess.run([
        f'{AIRFOIL_DIR}/airfoil',
        f'0 0.0001 {speed} {time}', mesh_xml_file], shell=True, cwd=AIRFOIL_DIR)
    forces = pd.read_csv(f'{AIRFOIL_DIR}/results/drag_ligt.m', sep='\t')
    return {'angle': angle, 'lift': list(forces.lift), 'drag': list(forces.drag)}

def get_task(task_id):
    res = airfoil_task.AsyncResult(task_id, app=app)
    return res
