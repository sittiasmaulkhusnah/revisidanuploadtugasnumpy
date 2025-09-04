# menampilkan citra gambar sebagai array numpy + heatmap

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# membaca gambar asli
img = Image.open("foto.png")

# konversi gambar ke array numpy
img_array=np.array(img)

# tampilkan gambar asli
plt.imshow(img_array)
plt.title("Gambar Asli")
plt.axis("off")
plt.show()

# visualisasi channel RGB dengan heatmap
fig, axes=plt.subplots(1, 3, figsize=(12, 4))
channels=["Red","Green", "Blue"]

for i, ax in enumerate(axes):
    ax.imshow(img_array[:, :, i], cmap="inferno")
    ax.set_title(f"Channel {channels[i]}")
    ax.axis("off")

plt.suptitle("Heatmap Array NumPy dari Channel RGB", fontsize=14)
plt.show()