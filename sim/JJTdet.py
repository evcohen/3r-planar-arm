import numpy as np
import matplotlib.pyplot as plt

# ── parameters ─────────────────────────────────────────────────────────────────
L1, L2, L3 = 10, 7, 7       # cm — swap in your arm's values
JOINT_LIM   = np.pi / 2      # ±90°
N           = 60_000

# ── vectorized FK ──────────────────────────────────────────────────────────────
def fk_batch(thetas):
    t1, t2, t3 = thetas[:,0], thetas[:,1], thetas[:,2]
    x = L1*np.cos(t1) + L2*np.cos(t1+t2) + L3*np.cos(t1+t2+t3)
    y = L1*np.sin(t1) + L2*np.sin(t1+t2) + L3*np.sin(t1+t2+t3)
    return np.stack([x, y], axis=1)

# ── vectorized manipulability ──────────────────────────────────────────────────
def manipulability_batch(thetas):
    t1, t2, t3 = thetas[:,0], thetas[:,1], thetas[:,2]
    s1,  c1   = np.sin(t1),       np.cos(t1)
    s12, c12  = np.sin(t1+t2),    np.cos(t1+t2)
    s123,c123 = np.sin(t1+t2+t3), np.cos(t1+t2+t3)

    # build J as (N, 2, 3)
    row0 = np.stack([-(L1*s1 + L2*s12 + L3*s123),
                     -(L2*s12 + L3*s123),
                      -L3*s123], axis=1)
    row1 = np.stack([ (L1*c1 + L2*c12 + L3*c123),
                      (L2*c12 + L3*c123),
                       L3*c123], axis=1)
    J   = np.stack([row0, row1], axis=1)       # (N, 2, 3)
    JJT = J @ J.transpose(0, 2, 1)            # (N, 2, 2)
    return np.sqrt(np.maximum(np.linalg.det(JJT), 0))

# ── sample ─────────────────────────────────────────────────────────────────────
rng    = np.random.default_rng(42)
thetas = rng.uniform(-JOINT_LIM, JOINT_LIM, (N, 3))
pos    = fk_batch(thetas)
w      = manipulability_batch(thetas)

# ── plot ───────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 7), facecolor='#0d0d0d')
ax.set_facecolor('#0d0d0d')

sc = ax.scatter(pos[:,0], pos[:,1],
                c=w, cmap='plasma',
                s=0.8, alpha=0.7, linewidths=0)

cbar = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('w  =  √det(JJᵀ)', color='white', fontsize=10)
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')

ax.set_aspect('equal')
ax.set_title('3R arm workspace  —  colored by manipulability',
             color='white', fontsize=12, pad=12)
ax.set_xlabel('x  (cm)', color='#aaa')
ax.set_ylabel('y  (cm)', color='#aaa')
ax.tick_params(colors='#aaa')
for spine in ax.spines.values():
    spine.set_edgecolor('#444')

ax.annotate('dark  →  near singularity\nbright  →  high mobility',
            xy=(0.03, 0.04), xycoords='axes fraction',
            color='#999', fontsize=8.5)

plt.tight_layout()
plt.savefig('manipulability_workspace.png', dpi=150,
            bbox_inches='tight', facecolor='#0d0d0d')
plt.show()