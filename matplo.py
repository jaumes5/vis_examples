import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Change the Size of Graph using
    # Figsize
    fig = plt.figure(figsize=(10, 10))

    # Generating a 3D sine wave
    ax = plt.axes(projection='3d')

    # Create axis
    axes = [5, 5, 5]

    # Create Data
    data = np.ones(axes)

    # Controll Tranperency
    alpha = 0.9

    # Control colour
    colors = np.empty(axes + [4])

    colors[0] = [1, 0, 0, alpha]  # red
    colors[1] = [0, 1, 0, alpha]  # green
    colors[2] = [0, 0, 1, alpha]  # blue
    colors[3] = [1, 1, 0, alpha]  # yellow
    colors[4] = [1, 1, 1, alpha]  # grey

    # trun off/on axis
    plt.axis('off')

    # Voxels is used to customizations of
    # the sizes, positions and colors.
    ax.voxels(data, facecolors=colors, edgecolors='grey')
    plt.show()
    plt.ion()
