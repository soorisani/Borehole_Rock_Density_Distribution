import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Load borehole data
df = pd.read_csv("borehole_data.csv")

# Filter rocks with high density
high_density = df[df["Density (g/cm³)"] > 2.5]

# Plot density vs. depth
plt.figure(figsize=(6,4))
plt.bar(df["Depth (m)"], df["Density (g/cm³)"], color="brown")
plt.xlabel("Depth (m)")
plt.ylabel("Density (g/cm³)")
plt.title("Borehole Rock Density")
plt.show()

# Load a geological shapefile
gdf = gpd.read_file("geology_map.shp")

# Plot geological map
fig, ax = plt.subplots(figsize=(10, 6))
gdf.plot(ax=ax, color="lightgrey")
plt.title("Geological Map Overlay")
plt.show()

# Save high-density rocks to CSV
high_density.to_csv("high_density_rocks.csv", index=False)
print("Project completed! Data exported.")
