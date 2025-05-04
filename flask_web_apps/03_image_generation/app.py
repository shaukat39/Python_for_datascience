from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Simulate image generation by returning a random placeholder image URL
def generate_image(prompt):
    # List of placeholder images for simulation
    placeholder_images = [
        "https://via.placeholder.com/1024x1024?text=Sample+Image+1",
        "https://via.placeholder.com/1024x1024?text=Sample+Image+2",
        "https://via.placeholder.com/1024x1024?text=Sample+Image+3"
    ]
    # In real use, you'd use the prompt to generate the image; here we simulate it
    return random.choice(placeholder_images)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')

        if prompt:
            image_url = generate_image(prompt)
            return render_template('index.html', image_url=image_url)
        else:
            return render_template('index.html', error='Please enter a description.')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)