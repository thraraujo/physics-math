from vpython import *
# Web VPython 3.2

scene.camera.pos = vector(8,8,8)
scene.camera.axis = vector(-1,-1,-1)

f1 = gcurve(color=color.blue)

t  =0
dt = 0.01

u = vector(2 * cos(2 * t), 2 * sin(2 * t),0)
v = vector(-3 * sin(3 * t), 3 * cos(3 * t),0)
w = cross(u,v)

uarr = arrow(pos=vector(0,0,0), axis=u, shaftwidth=0.3, round = True, color = vector(1,0,0))
varr = arrow(pos=vector(0,0,0), axis=v, shaftwidth=0.3, round = True, color = vector(0,1,0))
warr = arrow(pos=vector(0,0,0), axis=w, shaftwidth=0.3, round = True, color = vector(1,1,0))

while t < 5:
  rate(100)
  
  u = vector(2 * cos(2 * t), 2 * sin(2 * t),0)
  v = vector(-3 * sin(2 * t), 3 * cos(2 * t),0)
  w = cross(u,v)
  f1.plot(t, mag(u))
  
  uarr.axis = u
  varr.axis = v
  warr.axis = w
  t = t + dt
  
while t < 10:
  rate(100)
  
  u = vector(2 * cos(2 * t), 2 * sin(2 * t),0)
  v = vector(3 * sin(2 * t), 3 * cos(2 * t),0)
  w = cross(u,v)
  
  uarr.axis = u
  varr.axis = v
  warr.axis = w
  t = t + dt  
