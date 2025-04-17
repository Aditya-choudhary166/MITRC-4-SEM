import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from stability_sdk import client
import os

# Set up API key
os.environ["STABILITY_API_KEY"] = "sk-Cp8rwjh4wkjjazYCH72CoRTRWbQDGUK6QeQjwzh73Vu2bH6x"

# Create Stability AI client
stability_api = client.StabilityInference(
    key=os.environ["STABILITY_API_KEY"],
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0"  # Choose model version
)

def generate_image(prompt):
    answers = stability_api.generate(
        prompt=prompt,
        width=1024,
        height=1024,
        steps=50  # More steps = better quality but slower
    )

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                with open("generated_image.png", "wb") as f:
                    f.write(artifact.binary)
                print("Image saved as generated_image.png")

# Example usage
promt=input("Please enter Promt to Generate Image:")
generate_image(promt)