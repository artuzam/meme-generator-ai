import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

from meme_topics import get_random_topic

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to generate a meme caption using OpenAI's GPT-3.5-turbo
def generate_meme_caption(topic):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        instructions="You are a funny meme generator",
        input=f"Write a meme caption about {topic}. Avoid using emojis."
        "Use a humorous tone and make it relatable. The caption should be short and punchy."
        "Make sure it fits well with a meme format. The caption should be in English." \
        "Return the caption  in this format: {'top_text': '...', 'bottom_text': '...'}"
        "The top text should be a setup and the bottom text should be the punchline.",
    )
    
    return(response.output_text)

# Function to generate a meme image using OpenAI's DALL-E
def generate_meme_img(caption, topic):
    print(f"Generating meme image...")

    img = client.images.generate(
        model="gpt-image-1",
        prompt=(
            f"A funny meme image for the caption: {caption} and this topic {topic}. "
            "The image should be humorous and visually appealing. Don't include the text. "
            "Take inspiration from popular meme formats."
        ),
        n=1,
        size="1024x1024"
    )

    image_bytes = base64.b64decode(img.data[0].b64_json)
    with open("meme.png", "wb") as f:
        f.write(image_bytes)

# Main function
if __name__ == "__main__":
    topic = get_random_topic()
    print("Selected Topic:", topic)
    caption = generate_meme_caption(topic)
    print("Generated Meme Caption:", caption)
    generate_meme_img(caption, topic)