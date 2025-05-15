import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

from meme_topics import get_random_topic

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to generate a meme caption using OpenAI's GPT-3.5-turbo
def generate_meme_caption():
    # Get a random topic for the meme
    topic = get_random_topic()
    print("Selected Topic:", topic)

    response = client.responses.create(
        model="gpt-3.5-turbo",
        instructions="You are a funny meme generator",
        input=f"Write a meme caption about {topic}. Avoid using emojis.",
    )
    
    return(response.output_text)

# Function to generate a meme image using OpenAI's DALL-E
def generate_meme_img(caption):
    print(f"Generating meme image...")

    img = client.images.generate(
        model="gpt-image-1",
        prompt="A funny meme image with the caption: " + caption,
        n=1,
        size="1024x1024"
    )

    image_bytes = base64.b64decode(img.data[0].b64_json)
    with open("output.png", "wb") as f:
        f.write(image_bytes)

# Main function
if __name__ == "__main__":
    caption = generate_meme_caption()
    print("Generated Meme Caption:", caption)
    generate_meme_img(caption)