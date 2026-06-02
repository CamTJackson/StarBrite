def build_classification_prompt(
    target_id,
    feature_dict
):

    return f'''
You are an astrophysics researcher.

A Kepler target has been analyzed.

Target ID:
{target_id}

Extracted Light Curve Features:

Mean Flux:
{feature_dict["mean_flux"]}

Flux Standard Deviation:
{feature_dict["std_flux"]}

Minimum Flux:
{feature_dict["min_flux"]}

Maximum Flux:
{feature_dict["max_flux"]}

Number of Observations:
{feature_dict["n_points"]}

Classify the target into ONE category:

- Eclipsing Binary
- False Positive
- Triple Star System
- Multi-Star System
- Unknown

Return:

Classification:
Confidence (1-5):
Scientific Reasoning:
Uncertainty Statement:

Scientific reasoning is required.
'''
