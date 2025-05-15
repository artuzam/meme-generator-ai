from openai import OpenAI
import os
from dotenv import load_dotenv

from meme_topics import get_random_topic

# Load env variables (in GH Actions, set them as secrets)
load_dotenv()


# Step 1: Generate meme caption
def generate_meme_caption():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Get a random topic for the meme
    topic = get_random_topic()
    print("Selected Topic:", topic)

    response = client.responses.create(
        model="gpt-3.5-turbo",
        instructions="You are a funny meme generator",
        input=f"Write a meme caption about ${topic}. Avoid using emojis.",
    )
    
    return(response.output_text)

# Main function
if __name__ == "__main__":
    caption = generate_meme_caption()
    print("Generated Meme Caption:", caption)

    # TODO:
    # - Turn caption into image prompt
    # - Generate image with DALL·E
    # - Optionally overlay text
    # - Upload to Instagram
