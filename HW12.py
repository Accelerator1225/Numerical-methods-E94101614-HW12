import numpy as np

L = 1.0
T_end = 0.1
Nx = 10
dx = L / Nx
dt = 0.01
Nt = int(T_end / dt)
x = np.linspace(0, L, Nx + 1)

c = 1.0
lambda_sq = (c * dt / dx) ** 2

p0 = np.cos(2 * np.pi * x)
v0 = 2 * np.pi * np.sin(2 * np.pi * x)

u_prev = p0
u = np.zeros_like(x)
u[1:-1] = u_prev[1:-1] + dt * v0[1:-1] + 0.5 * lambda_sq * (u_prev[2:] - 2 * u_prev[1:-1] + u_prev[:-2])
u[0], u[-1] = 1, 2

for n in range(2, Nt + 1):
    u_new = np.zeros_like(x)
    u_new[1:-1] = (2 * u[1:-1] - u_prev[1:-1] +
                   lambda_sq * (u[2:] - 2 * u[1:-1] + u[:-2]))
    u_new[0], u_new[-1] = 1, 2
    u_prev, u = u, u_new
    if n * dt in [0.01, 0.05, 0.1]:
        print(f"Time = {n * dt:.3f}")
        for xi, ui in zip(x, u):
            print(f"x = {xi:.2f}, u = {ui:.6f}")
        print()
