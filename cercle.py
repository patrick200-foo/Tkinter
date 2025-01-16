

def draw_circle(radius):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    plt.figure()
    plt.plot(x, y)
    plt.xlim(-radius-1, radius+1)
    plt.ylim(-radius-1, radius+1)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.title(f"cercle de rayon{radius}")
    plt.grid()
    plt.show()

    rayon = 4
    draw_circle(rayon)
