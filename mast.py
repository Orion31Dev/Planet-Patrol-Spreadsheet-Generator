import numpy as np
from astroquery.mast import Catalogs

cols = ['ID', 'ra', 'dec', 'Tmag', 'GAIAmag', 'Vmag', 'Jmag', 'Kmag', 'Teff', 'logg', 'MH','lumclass', 'rad', 'e_rad', 'mass', 'numcont', 'contratio', 'pmRA', 'pmDEC']

def get_catalog_info(tic_id):
    catalogData = Catalogs.query_object('TIC' + str(tic_id), radius = 0.002, catalog='TIC', pagesize=1).to_pandas()

    for _, row in catalogData.iterrows():
        if row['ID'] == tic_id:
            print("Found.")
            return row[cols].to_numpy()

    return None