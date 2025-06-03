import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import base64
    from io import BytesIO
    from PIL import Image, ImageDraw, ImageFont
    import random
    import marimo as mo
    return BytesIO, Image, ImageDraw, ImageFont, base64, mo, random


@app.cell
def _():
    # Dati carte tarocchi
    tarot_cards = [
        {"name": "The Fool", "color": "lightyellow"},
        {"name": "The Fool Reversed", "color": "lightyellow"},
        {"name": "The Magician", "color": "lightblue"},
        {"name": "The Magician Reversed", "color": "lightblue"},
        {"name": "The High Priestess", "color": "lavender"},
        {"name": "The High Priestess Reversed", "color": "lavender"},
        {"name": "The Empress", "color": "pink"},
        {"name": "The Empress Reversed", "color": "pink"},
        {"name": "The Emperor", "color": "lightgreen"},
        {"name": "The Emperor Reversed", "color": "lightgreen"},
        {"name": "The Hierophant", "color": "khaki"},
        {"name": "The Hierophant Reversed", "color": "khaki"},
        {"name": "The Lovers", "color": "lightcoral"},
        {"name": "The Lovers Reversed", "color": "lightcoral"},
        {"name": "The Chariot", "color": "skyblue"},
        {"name": "The Chariot Reversed", "color": "skyblue"},
        {"name": "Strength", "color": "gold"},
        {"name": "Strength Reversed", "color": "gold"},
        {"name": "The Hermit", "color": "lightgrey"},
        {"name": "The Hermit Reversed", "color": "lightgrey"},
        {"name": "Wheel of Fortune", "color": "peachpuff"},
        {"name": "Wheel of Fortune Reversed", "color": "peachpuff"},
        {"name": "Justice", "color": "lightsteelblue"},
        {"name": "Justice Reversed", "color": "lightsteelblue"},
        {"name": "The Hanged Man", "color": "lightseagreen"},
        {"name": "The Hanged Man Reversed", "color": "lightseagreen"},
        {"name": "Death", "color": "dimgray"},
        {"name": "Death Reversed", "color": "dimgray"},
        {"name": "Temperance", "color": "wheat"},
        {"name": "Temperance Reversed", "color": "wheat"},
        {"name": "The Devil", "color": "firebrick"},
        {"name": "The Devil Reversed", "color": "firebrick"},
        {"name": "The Tower", "color": "indianred"},
        {"name": "The Tower Reversed", "color": "indianred"},
        {"name": "The Star", "color": "lightcyan"},
        {"name": "The Star Reversed", "color": "lightcyan"},
        {"name": "The Moon", "color": "lightblue"},
        {"name": "The Moon Reversed", "color": "lightblue"},
        {"name": "The Sun", "color": "goldenrod"},
        {"name": "The Sun Reversed", "color": "goldenrod"},
        {"name": "Judgement", "color": "lightpink"},
        {"name": "Judgement Reversed", "color": "lightpink"},
        {"name": "The World", "color": "mediumorchid"},
        {"name": "The World Reversed", "color": "mediumorchid"},
    ]
    return (tarot_cards,)


@app.cell
def _(mo):
    # Bottone per pescare
    draw_button = mo.ui.button(label="Pesca nuove carte 🎴")
    return (draw_button,)


@app.cell
def _(BytesIO, Image, ImageDraw, ImageFont, base64, random, tarot_cards):
    # Funzione per creare immagine PIL
    def generate_card_image(card):
        img = Image.new("RGB", (200, 300), color=card["color"])
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        text = card["name"]
        bbox = draw.textbbox((0, 0), text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((200 - w) / 2, (300 - h) / 2), text, fill="black", font=font)
        return img

    # Funzione per convertire PIL img in base64 string
    def pil_to_base64(img):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str

    positions = ["Past", "Present", "Future"]
    selected_cards = random.sample(tarot_cards, 3)
    return generate_card_image, pil_to_base64, positions


@app.cell
def _(
    draw_button,
    generate_card_image,
    mo,
    pil_to_base64,
    positions,
    random,
    tarot_cards,
):
    def show_cards():
        draw_button.value  # trigger re-render
        selected_cards = random.sample(tarot_cards, 3)
        return mo.hstack([
            mo.image(
                src=f"data:image/png;base64,{pil_to_base64(generate_card_image(card))}",
                caption=f"{pos}: {card['name']}"
            ) for pos, card in zip(positions, selected_cards)
        ])

    # Layout: bottone + carte
    mo.vstack([draw_button, show_cards()])
    return


if __name__ == "__main__":
    app.run()
