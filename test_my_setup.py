# Note: This is just my test file to make sure the dependencies are working correctly. 
# It is not meant to be a comprehensive test suite. You can run this file with `python test.py` to see the results. 
# If you see any errors, please check your installation and try again. 

from lightkurve import search_lightcurve
from openai import OpenAI
import os

def test_kepler():
    print("\nTesting Kepler...")
    target = "KIC 3863594"
    result = search_lightcurve(target, mission="Kepler")
    print(f"Found {len(result)} Kepler records.")

def test_tess():
    print("\nTesting TESS...")
    target = "TIC 290061484"
    result = search_lightcurve(target, mission="TESS")
    print(f"Found {len(result)} TESS records.")

def test_openai():
    print("\nTesting OpenAI...")
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-5-mini",
        input="Say hello."
    )
    print(response.output_text)

if __name__ == "__main__":
    test_kepler()
    test_tess()
    test_openai()
    print("\nAll tests completed successfully.")
    