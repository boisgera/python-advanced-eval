# %%
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data

# %%
with get_sample_data("grace_hopper.jpg") as file:
    image_array = plt.imread(file)

# %%
image_array

# %%
plt.imshow(image_array)
plt.show()

