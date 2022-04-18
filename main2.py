from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=10)
scene.set_floor(-0.05, (1.0, 1.0, 1.0))
scene.set_background_color((1.0, 1.0, 1.0))
scene.set_directional_light((.8,1.,.8), 0.1, (.3, .3, .3))


@ti.func
def sphere(pos,r):
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        x = i - pos[0]
        y = i - pos[1]
        z = k - pos[2]
        if (x ** 2 + y ** 2 + z ** 2 < r * r):
            scene.set_voxel(vec3(i, j, k), 1, vec3(.1,.1, 1))

@ti.func
def sphere(pos,r):
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        x = i - pos[0]
        y = i - pos[1]
        z = k - pos[2]
        if (x ** 2 + y ** 2 + z ** 2 < r * r):
            scene.set_voxel(vec3(i, j, k), 1, vec3(.2,.1, 1))

@ti.func
def sphere(pos,r):
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        x = i - pos[2]
        y = i - pos[1]
        z = k - pos[0]
        if (x ** 2 + y ** 2 + z ** 2 < r * r):
            scene.set_voxel(vec3(i, j, k), 1, vec3(.1,.1, 1))

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    sphere(vec3(0,0,0),10)
    sphere(vec3(15,0,0),10)
    sphere(vec3(30,0,0),10)
    sphere(vec3(45,0,0),10)
    sphere(vec3(60,0,0),10)
    sphere(vec3(75,0,0),10)
    sphere(vec3(90,0,0),10)


initialize_voxels()

scene.finish()
