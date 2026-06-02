import re


def parse_gpt_response(text):

    result = {
        "gpt_classification": None,
        "gpt_confidence": None,
        "gpt_reasoning": None,
        "gpt_uncertainty": None
    }

    if not isinstance(text, str):
        return result

    classification = re.search(
        r"Classification:\s*(.+)",
        text,
        re.IGNORECASE
    )

    confidence = re.search(
        r"Confidence.*?:\s*([0-9.]+)",
        text,
        re.IGNORECASE
    )

    reasoning = re.search(
        r"Scientific Reasoning:\s*(.+?)(?:Uncertainty Statement:|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    uncertainty = re.search(
        r"Uncertainty Statement:\s*(.+)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if classification:
        result["gpt_classification"] = classification.group(1).strip()

    if confidence:
        try:
            result["gpt_confidence"] = float(confidence.group(1))
        except ValueError:
            pass

    if reasoning:
        result["gpt_reasoning"] = reasoning.group(1).strip()

    if uncertainty:
        result["gpt_uncertainty"] = uncertainty.group(1).strip()

    return result
