# 3R Planar Robotic Arm

A 3-revolute-joint planar robotic arm built to apply concepts from
Calculus III and Linear Algebra. Includes a Python simulation and
a physical hardware build.

**Link lengths:** L1 = 10cm, L2 = 7cm, L3 = 7cm  
**Joint limits:** ±90° on all three joints

## Progress
- [x] Forward kinematics + matplotlib arm animator
- [x] Analytical Jacobian, numerical verification
- [ ] Workspace boundary + singularity analysis
- [ ] Null space demo
- [ ] SVD + manipulability ellipsoid
- [ ] Physical build + Arduino serial comms

## Run the simulation
```bash
pip install -r requirements.txt
python sim/arm.py
```

## Hardware
Arduino R4, MG90D servos ×3, 3D printed links (Fusion 360 → Ender 3)