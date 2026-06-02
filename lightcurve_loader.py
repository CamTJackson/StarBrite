import lightkurve as lk
import numpy as np

def download_kepler_lightcurve(target_id):
    search = lk.search_lightcurve(
        f"{target_id}",
        mission="Kepler"
    )

    if len(search) == 0:
        raise ValueError(f"No Kepler data found for {target_id}")

    lc = search.download().remove_nans()
    return lc

def extract_features(lightcurve):
    flux = np.array(lightcurve.flux.value)

    return {
        "mean_flux": float(np.mean(flux)),
        "std_flux": float(np.std(flux)),
        "min_flux": float(np.min(flux)),
        "max_flux": float(np.max(flux)),
        "n_points": int(len(flux))
    }
