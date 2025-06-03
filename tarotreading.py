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
        # Major Arcana - purple
        {"name": "The Fool", "color": "purple", "meaning": "New beginnings, spontaneity, a free spirit."},
        {"name": "The Fool Reversed", "color": "purple", "meaning": "Recklessness, risk-taking, holding back."},
        {"name": "The Magician", "color": "purple", "meaning": "Manifestation, resourcefulness, power."},
        {"name": "The Magician Reversed", "color": "purple", "meaning": "Manipulation, poor planning, untapped talents."},
        {"name": "The High Priestess", "color": "purple", "meaning": "Intuition, divine feminine, mystery."},
        {"name": "The High Priestess Reversed", "color": "purple", "meaning": "Secrets, withdrawal, silence."},
        {"name": "The Empress", "color": "purple", "meaning": "Fertility, beauty, nature, abundance."},
        {"name": "The Empress Reversed", "color": "purple", "meaning": "Creative block, dependence on others."},
        {"name": "The Emperor", "color": "purple", "meaning": "Authority, structure, control, fatherhood."},
        {"name": "The Emperor Reversed", "color": "purple", "meaning": "Domination, excessive control, rigidity."},
        {"name": "The Hierophant", "color": "purple", "meaning": "Tradition, conformity, morality."},
        {"name": "The Hierophant Reversed", "color": "purple", "meaning": "Rebellion, personal beliefs."},
        {"name": "The Lovers", "color": "purple", "meaning": "Love, harmony, relationships, values alignment."},
        {"name": "The Lovers Reversed", "color": "purple", "meaning": "Imbalance, conflict, disconnection."},
        {"name": "The Chariot", "color": "purple", "meaning": "Determination, success, control, willpower."},
        {"name": "The Chariot Reversed", "color": "purple", "meaning": "Aggression, lack of control, self-doubt."},
        {"name": "Strength", "color": "purple", "meaning": "Courage, persuasion, influence, compassion."},
        {"name": "Strength Reversed", "color": "purple", "meaning": "Self-doubt, weakness, insecurity."},
        {"name": "The Hermit", "color": "purple", "meaning": "Soul-searching, introspection, being alone."},
        {"name": "The Hermit Reversed", "color": "purple", "meaning": "Isolation, loneliness, withdrawal."},
        {"name": "Wheel of Fortune", "color": "purple", "meaning": "Good luck, karma, life cycles, destiny."},
        {"name": "Wheel of Fortune Reversed", "color": "purple", "meaning": "Bad luck, resistance to change."},
        {"name": "Justice", "color": "purple", "meaning": "Fairness, truth, law, cause and effect."},
        {"name": "Justice Reversed", "color": "purple", "meaning": "Dishonesty, unfairness, lack of accountability."},
        {"name": "The Hanged Man", "color": "purple", "meaning": "Pause, surrender, letting go, new perspective."},
        {"name": "The Hanged Man Reversed", "color": "purple", "meaning": "Delays, resistance, stalling."},
        {"name": "Death", "color": "purple", "meaning": "Endings, transformation, transition."},
        {"name": "Death Reversed", "color": "purple", "meaning": "Resistance to change, personal transformation."},
        {"name": "Temperance", "color": "purple", "meaning": "Balance, moderation, purpose, patience."},
        {"name": "Temperance Reversed", "color": "purple", "meaning": "Imbalance, excess, lack of long-term vision."},
        {"name": "The Devil", "color": "purple", "meaning": "Addiction, materialism, playfulness."},
        {"name": "The Devil Reversed", "color": "purple", "meaning": "Freedom, release, restoring control."},
        {"name": "The Tower", "color": "purple", "meaning": "Sudden change, upheaval, chaos."},
        {"name": "The Tower Reversed", "color": "purple", "meaning": "Fear of change, averting disaster."},
        {"name": "The Star", "color": "purple", "meaning": "Hope, faith, renewal, purpose."},
        {"name": "The Star Reversed", "color": "purple", "meaning": "Despair, disconnection, lack of faith."},
        {"name": "The Moon", "color": "purple", "meaning": "Illusion, fear, anxiety, intuition."},
        {"name": "The Moon Reversed", "color": "purple", "meaning": "Release of fear, confusion, clarity."},
        {"name": "The Sun", "color": "purple", "meaning": "Positivity, fun, success, joy."},
        {"name": "The Sun Reversed", "color": "purple", "meaning": "Negativity, depression, false impressions."},
        {"name": "Judgement", "color": "purple", "meaning": "Reflection, reckoning, awakening."},
        {"name": "Judgement Reversed", "color": "purple", "meaning": "Self-doubt, refusal of self-examination."},
        {"name": "The World", "color": "purple", "meaning": "Completion, integration, travel, accomplishment."},
        {"name": "The World Reversed", "color": "purple", "meaning": "Unfinished goals, lack of closure."},
    ]

    # Arcani Minori
    suits = {
        "Swords": {
            "color": "yellow",
            "meanings": {
                "Ace": ("Breakthroughs, mental clarity, truth.", "Confusion, brutality, chaos."),
                "Two": ("Difficult decisions, weighing options.", "Indecision, confusion, stalemate."),
                "Three": ("Heartbreak, betrayal, grief.", "Recovery, forgiveness, moving on."),
                "Four": ("Rest, contemplation, restoration.", "Restlessness, burnout, stress."),
                "Five": ("Conflict, tension, defeat.", "Reconciliation, past resentment."),
                "Six": ("Transition, moving on, rite of passage.", "Resistance to change, unfinished business."),
                "Seven": ("Deception, strategy, trickery.", "Coming clean, rethinking tactics."),
                "Eight": ("Imprisonment, self-victimization.", "Freedom, release, self-empowerment."),
                "Nine": ("Anxiety, nightmares, fear.", "Inner turmoil, deep fears released."),
                "Ten": ("Painful endings, betrayal.", "Recovery, regeneration, resisting ruin."),
                "Page": ("Curiosity, intellect, new ideas.", "Deception, all talk, haste."),
                "Knight": ("Ambition, action, fast-thinking.", "Restless, unfocused, impulsive."),
                "Queen": ("Perceptive, independent, direct.", "Cold-hearted, cruel, bitterness."),
                "King": ("Mental clarity, truth, authority.", "Manipulative, ruthless, misuse of power."),
            },
        },
        "Cups": {
            "color": "blue",
            "meanings": {
                "Ace": ("New feelings, spirituality, intuition.", "Emotional loss, blocked creativity."),
                "Two": ("Unity, partnership, connection.", "Imbalance, tension, breakup."),
                "Three": ("Friendship, celebration, community.", "Overindulgence, gossip, isolation."),
                "Four": ("Apathy, contemplation, disconnection.", "Sudden awareness, choosing happiness."),
                "Five": ("Regret, grief, disappointment.", "Acceptance, moving on, finding peace."),
                "Six": ("Nostalgia, memories, childhood.", "Stuck in the past, unrealistic."),
                "Seven": ("Choices, fantasy, illusion.", "Clarity, reality, decisiveness."),
                "Eight": ("Withdrawal, introspection, journey.", "Fear of change, stagnation."),
                "Nine": ("Contentment, satisfaction, success.", "Greed, dissatisfaction, smugness."),
                "Ten": ("Harmony, marriage, happiness.", "Broken relationships, domestic conflict."),
                "Page": ("Happy news, sensitivity, dreamer.", "Insecurity, emotional immaturity."),
                "Knight": ("Romance, charm, following heart.", "Jealousy, moodiness, unrealistic."),
                "Queen": ("Compassionate, nurturing, caring.", "Insecurity, co-dependency."),
                "King": ("Emotionally balanced, diplomatic.", "Emotional manipulation, moodiness."),
            },
        },
        "Wands": {
            "color": "red",
            "meanings": {
                "Ace": ("Inspiration, new opportunities, growth.", "Delays, lack of direction."),
                "Two": ("Planning, decisions, discovery.", "Fear of unknown, lack of planning."),
                "Three": ("Expansion, foresight, progress.", "Obstacles, delays, frustration."),
                "Four": ("Celebration, home, harmony.", "Conflict at home, instability."),
                "Five": ("Competition, conflict, tension.", "Avoiding conflict, compromise."),
                "Six": ("Success, public recognition.", "Ego, lack of recognition."),
                "Seven": ("Challenge, competition, perseverance.", "Giving up, overwhelmed."),
                "Eight": ("Action, movement, fast-paced change.", "Delays, frustration, resisting change."),
                "Nine": ("Resilience, persistence, test of faith.", "Exhaustion, fatigue."),
                "Ten": ("Burden, responsibility, stress.", "Relief, release, letting go."),
                "Page": ("Inspiration, discovery, enthusiasm.", "Lack of direction, procrastination."),
                "Knight": ("Energy, passion, adventure.", "Recklessness, anger, delays."),
                "Queen": ("Confidence, determination, joy.", "Jealousy, selfishness, insecurity."),
                "King": ("Leadership, vision, honor.", "Impulsiveness, overbearing."),
            },
        },
        "Pentacles": {
            "color": "green",
            "meanings": {
                "Ace": ("New financial or career opportunity.", "Lost opportunity, lack of planning."),
                "Two": ("Balance, adaptability, time management.", "Disorganization, financial instability."),
                "Three": ("Teamwork, collaboration, building.", "Lack of teamwork, disorganization."),
                "Four": ("Saving, security, conservatism.", "Greed, financial fear, scarcity."),
                "Five": ("Poverty, insecurity, worry.", "Recovery, improvement."),
                "Six": ("Giving, receiving, generosity.", "Strings attached, debt, inequality."),
                "Seven": ("Patience, hard work, investment.", "Lack of reward, impatience."),
                "Eight": ("Skill development, mastery, diligence.", "Perfectionism, lack of focus."),
                "Nine": ("Abundance, luxury, self-sufficiency.", "Overinvestment, setbacks."),
                "Ten": ("Wealth, legacy, family, establishment.", "Financial failure, instability."),
                "Page": ("Ambition, diligence, financial news.", "Laziness, foolishness."),
                "Knight": ("Hard work, productivity, routine.", "Laziness, obsession."),
                "Queen": ("Nurturing, practicality, providing.", "Self-centeredness, imbalance."),
                "King": ("Security, control, leadership.", "Greed, stubbornness."),
            },
        },
    }

    # Aggiunta automatica delle carte minori al mazzo
    for suit, data in suits.items():
        for rank, (upright, reversed_meaning) in data["meanings"].items():
            tarot_cards.append({"name": f"{rank} of {suit}", "color": data["color"], "meaning": upright})
            tarot_cards.append({"name": f"{rank} of {suit} Reversed", "color": data["color"], "meaning": reversed_meaning})

    return (tarot_cards,)


@app.cell
def _(mo):
    # Bottone per pescare
    draw_button = mo.ui.button(label="Pesca nuove carte 🎴")
    return (draw_button,)


@app.cell
def _(BytesIO, Image, ImageDraw, ImageFont, base64):
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

        images = mo.hstack([
            mo.image(
                src=f"data:image/png;base64,{pil_to_base64(generate_card_image(card))}",
                caption=f"{pos}: {card['name']}"
            ) for pos, card in zip(positions, selected_cards)
        ])

        return mo.vstack([images])

    mo.vstack([draw_button, show_cards()])
    return


if __name__ == "__main__":
    app.run()
