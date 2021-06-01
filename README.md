# Remote Sensing Indices

In this repository, eight of the most widely used indices in remote sensing for optical data are provided:

- Normalized Difference Vegetation Index (NDVI)
- Normalized Difference Water Index (NDWI)
- Soil Adjusted Vegetation Index (SAVI)
- Optimized Soil Adjusted Vegetation Index (OSAVI)
- New Built-up Index (NBI)
- Normalized Difference Built-up Index (NDBI)
- Notmalized Burnt Ratio (NBR)
- Difference Normalized Burnt Index (dNBR)

# Use the functions

**Clone the repository**

```
git clone https://github.com/IoannisGkanatsios/Remote_Sensing_Indices.git

cd Remote_Sensing_Indices

```

**Import the fucntions - An example**

```
from src.indices import NDVI


with rasterio.open(path_to_the_image)) as src:
    s2 = src.read()

ndvi = NDVI(s2, sensor='sentinel2')
```

![block_of_code](https://user-images.githubusercontent.com/25709946/120350652-1631b880-c2f7-11eb-9485-0cd7f1ae950b.png)


# Licence
MIT

