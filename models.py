from dataclasses import dataclass

@dataclass
class BenchmarkTarget:
    item_id: str
    target_id: str
    ground_truth: str
    category: str

@dataclass
class LightCurveFeatures:
    target_id: str
    mean_flux: float
    std_flux: float
    min_flux: float
    max_flux: float
    n_points: int
