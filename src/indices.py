import numpy as np


def exception(sensor):
    if sensor not in ['sentinel2', 'landsat8']:
        raise Exception(
            'Please provide a valid sensor (landsat8 or sentinel2)')


def NDVI(raster, sensor=None):
    """Vegetation index

    parameters
    ----------
    nir: NIR band as input
    red: RED band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        red = raster[3, :, :]
        nir = raster[7, :, :]
        ndvi = (nir.astype('float') - red.astype('float')) / \
            (nir.astype('float') + red.astype('float'))

    elif sensor == 'landsat8':
        red = raster[3, :, :]
        nir = raster[4, :, :]
        ndvi = (nir.astype('float') - red.astype('float')) / \
            (nir.astype('float') + red.astype('float'))
    return ndvi


def SAVI(raster, L=0.3, sensor=None):
    """It is used where vegetation cover is low and the soil is exposed. NDVI can be influenced by soil reflectance.
    The value of L is adjusted based on the amount of vegetation. L=0.3 is the default value 
    and works well in most situations. With L=0, NDVI=SAVI.

    parameters
    ----------
    green: green band as input
    swir: SWIR band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        red = raster[3, :, :]
        nir = raster[7, :, :]
        savi = ((nir.astype('float') - red.astype('float')) /
                (nir.astype('float') + red.astype('float'))) * (1+L)

    elif sensor == 'landsat8':
        red = raster[3, :, :]
        nir = raster[4, :, :]
        savi = ((nir.astype('float') - red.astype('float')) /
                (nir.astype('float') + red.astype('float'))) * (1+L)
    return savi


def OSAVI(raster, sensor=None):
    """In general, OSAVI is more sensitive to vegetation and shows differences in vegetation better than SAVI. 
    OSAVI works well in areas where the vegetation density is high

    parameters
    ----------
    green: green band as input
    swir: SWIR band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        red = raster[3, :, :]
        nir = raster[7, :, :]
        osavi = (nir.astype('float') - red.astype('float')) / \
            (nir.astype('float') + red.astype('float') + 0.16)

    elif sensor == 'landsat8':
        red = raster[3, :, :]
        nir = raster[4, :, :]
        osavi = (nir.astype('float') - red.astype('float')) / \
            (nir.astype('float') + red.astype('float') + 0.16)
    return osavi


def NDWI(raster, sensor=None):
    """Water index. Detects water bodies

    parameters
    ----------
    green: green band as input
    nir: NIR band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        green = raster[2, :, :]
        nir = raster[7, :, :]
        ndwi = (green.astype('float') - nir.astype('float')) / \
            (green.astype('float') + nir.astype('float'))

    elif sensor == 'landsat8':
        green = raster[2, :, :]
        nir = raster[4, :, :]
        ndwi = (green.astype('float') - nir.astype('float')) / \
            (green.astype('float') + nir.astype('float'))
    return ndwi


def NDSI(raster, sensor=None):
    """Snow index. Detects areas of snow

    parameters
    ----------
    green: green band as input
    swir: SWIR band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        green = raster[2, :, :]
        swir = raster[9, :, :]
        ndsi = (green.astype('float') - swir.astype('float')) / \
            (green.astype('float') + swir.astype('float'))

    elif sensor == 'landsat8':
        green = raster[2, :, :]
        swir = raster[5, :, :]
        ndsi = (green.astype('float') - swir.astype('float')) / \
            (green.astype('float') + swir.astype('float'))
    return ndsi


def NBR(raster, sensor=None):
    """Burnt index. Highlights areas that got burned

    parameters
    ----------
    nir: NIR band as input
    swir: SWIR band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        nir = raster[7, :, :]
        swir = raster[9, :, :]
        nbr = (nir.astype('float') - swir.astype('float')) / \
            (nir.astype('float') + swir.astype('float'))

    elif sensor == 'landsat8':
        nir = raster[4, :, :]
        swir = raster[5, :, :]
        nbr = (nir.astype('float') - swir.astype('float')) / \
            (nir.astype('float') + swir.astype('float'))
    return nbr


def dNBR(raster_pre, raster_post, sensor=None):
    """Difference Burnt index based on pre and post fire event

    parameters
    ----------
    pre: nbr results on the image acquired before fire
    post: nbr results on the image acquired after fire
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        nbr_pre = NBR(raster_pre, sensor='sentinel2')
        nbr_post = NBR(raster_post, sensor='sentinel2')
        d_nbr = nbr_pre - nbr_post

    elif sensor == 'landsat8':
        nbr_pre = NBR(raster_pre, sensor='landsat8')
        nbr_post = NBR(raster_post, sensor='landsat8')
        d_nbr = nbr_pre - nbr_post
    return d_nbr


def NBI(raster, sensor=None):
    """New Built-up Index. Extracts urban environment

    parameters
    ----------
    red: RED band as input
    nir: NIR band as input
    swir: SWIR band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        red = raster[3, :, :]
        nir = raster[7, :, :]
        swir = raster[9, :, :]
        nbi = (red.astype('float') * swir.astype('float')) / \
            (nir.astype('float'))

    elif sensor == 'landsat8':
        red = raster[3, :, :]
        nir = raster[4, :, :]
        swir = raster[5, :, :]
        nbi = (red.astype('float') * swir.astype('float')) / \
            (nir.astype('float'))
    return nbi


def NDBI(raster, sensor=None):
    """Normalized Difference Built-up Index. Extracts urban environment

    parameters
    ----------
    nir: NIR band as input
    swir: SWIR band as input
    """
    error = exception(sensor)

    if sensor == 'sentinel2':
        nir = raster[7, :, :]
        swir = raster[9, :, :]
        ndbi = (swir.astype('float') - nir.astype('float')) / \
            (swir.astype('float') + nir.astype('float'))

    elif sensor == 'landsat8':
        nir = raster[4, :, :]
        swir = raster[5, :, :]
        ndbi = (swir.astype('float') - nir.astype('float')) / \
            (swir.astype('float') + nir.astype('float'))
    return ndbi
