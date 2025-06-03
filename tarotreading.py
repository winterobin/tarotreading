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
        {"name": "The Magician", "color": "lightblue"},
        {"name": "The High Priestess", "color": "lavender"},
        {"name": "The Empress", "color": "pink"},
        {"name": "The Emperor", "color": "lightgray"},
        {"name": "The Lovers", "color": "lightcoral"},
        {"name": "The Chariot", "color": "lightgreen"},
        {"name": "Strength", "color": "peachpuff"},
        {"name": "The Hermit", "color": "lightcyan"},
        {"name": "Wheel of Fortune", "color": "gold"},
    ]
    return (tarot_cards,)


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
    return generate_card_image, pil_to_base64, positions, selected_cards


@app.cell
def _(generate_card_image, mo, pil_to_base64, positions, selected_cards):
    [mo.image(
        src=f"data:image/png;base64,{pil_to_base64(generate_card_image(card))}",
        caption=f"{pos}: {card['name']}"
    ) for pos, card in zip(positions, selected_cards)]
    return


if __name__ == "__main__":
    app.run()
