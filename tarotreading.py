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
    	# Swords - yellow
    	{"name": "Ace of Swords", "color": "yellow", "meaning": "Breakthroughs, mental clarity, truth."},
    	{"name": "Ace of Swords Reversed", "color": "yellow", "meaning": "Confusion, brutality, chaos."},
    	{"name": "Two of Swords", "color": "yellow", "meaning": "Difficult decisions, weighing options."},
    	{"name": "Two of Swords Reversed", "color": "yellow", "meaning": "Indecision, confusion, stalemate."},
    	{"name": "Three of Swords", "color": "yellow", "meaning": "Heartbreak, betrayal, grief."},
    	{"name": "Three of Swords Reversed", "color": "yellow", "meaning": "Recovery, forgiveness, moving on."},
    	{"name": "Four of Swords", "color": "yellow", "meaning": "Rest, contemplation, restoration."},
    	{"name": "Four of Swords Reversed", "color": "yellow", "meaning": "Restlessness, burnout, stress."},
    	{"name": "Five of Swords", "color": "yellow", "meaning": "Conflict, tension, defeat."},
    	{"name": "Five of Swords Reversed", "color": "yellow", "meaning": "Reconciliation, past resentment."},
    	{"name": "Six of Swords", "color": "yellow", "meaning": "Transition, moving on, rite of passage."},
    	{"name": "Six of Swords Reversed", "color": "yellow", "meaning": "Resistance to change, unfinished business."},
    	{"name": "Seven of Swords", "color": "yellow", "meaning": "Deception, strategy, trickery."},
    	{"name": "Seven of Swords Reversed", "color": "yellow", "meaning": "Coming clean, rethinking tactics."},
    	{"name": "Eight of Swords", "color": "yellow", "meaning": "Imprisonment, self-victimization."},
    	{"name": "Eight of Swords Reversed", "color": "yellow", "meaning": "Freedom, release, self-empowerment."},
    	{"name": "Nine of Swords", "color": "yellow", "meaning": "Anxiety, nightmares, fear."},
    	{"name": "Nine of Swords Reversed", "color": "yellow", "meaning": "Inner turmoil, deep fears released."},
    	{"name": "Ten of Swords", "color": "yellow", "meaning": "Painful endings, betrayal."},
    	{"name": "Ten of Swords Reversed", "color": "yellow", "meaning": "Recovery, regeneration, resisting ruin."},
    	{"name": "Page of Swords", "color": "yellow", "meaning": "Curiosity, intellect, new ideas."},
    	{"name": "Page of Swords Reversed", "color": "yellow", "meaning": "Deception, all talk, haste."},
    	{"name": "Knight of Swords", "color": "yellow", "meaning": "Ambition, action, fast-thinking."},
    	{"name": "Knight of Swords Reversed", "color": "yellow", "meaning": "Restless, unfocused, impulsive."},
    	{"name": "Queen of Swords", "color": "yellow", "meaning": "Perceptive, independent, direct."},
    	{"name": "Queen of Swords Reversed", "color": "yellow", "meaning": "Cold-hearted, cruel, bitterness."},
    	{"name": "King of Swords", "color": "yellow", "meaning": "Mental clarity, truth, authority."},
    	{"name": "King of Swords Reversed", "color": "yellow", "meaning": "Manipulative, ruthless, misuse of power."},		
    	# Cups - blue	
    	{"name": "Ace of Cups", "color": "blue", "meaning": "New feelings, spirituality, intuition."},
    	{"name": "Ace of Cups Reversed", "color": "blue", "meaning": "Emotional loss, blocked creativity."},
    	{"name": "Two of Cups", "color": "blue", "meaning": "Unity, partnership, connection."},
    	{"name": "Two of Cups Reversed", "color": "blue", "meaning": "Imbalance, tension, breakup."},
    	{"name": "Three of Cups", "color": "blue", "meaning": "Friendship, celebration, community."},
    	{"name": "Three of Cups Reversed", "color": "blue", "meaning": "Overindulgence, gossip, isolation."},
    	{"name": "Four of Cups", "color": "blue", "meaning": "Apathy, contemplation, disconnection."},
    	{"name": "Four of Cups Reversed", "color": "blue", "meaning": "Sudden awareness, choosing happiness."},
    	{"name": "Five of Cups", "color": "blue", "meaning": "Regret, grief, disappointment."},
    	{"name": "Five of Cups Reversed", "color": "blue", "meaning": "Acceptance, moving on, finding peace."},
    	{"name": "Six of Cups", "color": "blue", "meaning": "Nostalgia, memories, childhood."},
    	{"name": "Six of Cups Reversed", "color": "blue", "meaning": "Stuck in the past, unrealistic."},
    	{"name": "Seven of Cups", "color": "blue", "meaning": "Choices, fantasy, illusion."},
    	{"name": "Seven of Cups Reversed", "color": "blue", "meaning": "Clarity, reality, decisiveness."},
    	{"name": "Eight of Cups", "color": "blue", "meaning": "Withdrawal, introspection, journey."},
    	{"name": "Eight of Cups Reversed", "color": "blue", "meaning": "Fear of change, stagnation."},
    	{"name": "Nine of Cups", "color": "blue", "meaning": "Contentment, satisfaction, success."},
    	{"name": "Nine of Cups Reversed", "color": "blue", "meaning": "Greed, dissatisfaction, smugness."},
    	{"name": "Ten of Cups", "color": "blue", "meaning": "Harmony, marriage, happiness."},
    	{"name": "Ten of Cups Reversed", "color": "blue", "meaning": "Broken relationships, domestic conflict."},
    	{"name": "Page of Cups", "color": "blue", "meaning": "Happy news, sensitivity, dreamer."},
    	{"name": "Page of Cups Reversed", "color": "blue", "meaning": "Insecurity, emotional immaturity."},
    	{"name": "Knight of Cups", "color": "blue", "meaning": "Romance, charm, following heart."},
    	{"name": "Knight of Cups Reversed", "color": "blue", "meaning": "Jealousy, moodiness, unrealistic."},
    	{"name": "Queen of Cups", "color": "blue", "meaning": "Compassionate, nurturing, caring."},
    	{"name": "Queen of Cups Reversed", "color": "blue", "meaning": "Insecurity, co-dependency."},
    	{"name": "King of Cups", "color": "blue", "meaning": "Emotionally balanced, diplomatic."},
    	{"name": "King of Cups Reversed", "color": "blue", "meaning": "Emotional manipulation, moodiness."},		
    	# Wands - red
    	{"name": "Ace of Wands", "color": "red", "meaning": "Inspiration, new opportunities, growth."},
    	{"name": "Ace of Wands Reversed", "color": "red", "meaning": "Delays, lack of direction."},
    	{"name": "Two of Wands", "color": "red", "meaning": "Planning, decisions, discovery."},
    	{"name": "Two of Wands Reversed", "color": "red", "meaning": "Fear of unknown, lack of planning."},
    	{"name": "Three of Wands", "color": "red", "meaning": "Expansion, foresight, progress."},
    	{"name": "Three of Wands Reversed", "color": "red", "meaning": "Obstacles, delays, frustration."},
    	{"name": "Four of Wands", "color": "red", "meaning": "Celebration, home, harmony."},
    	{"name": "Four of Wands Reversed", "color": "red", "meaning": "Conflict at home, instability."},
    	{"name": "Five of Wands", "color": "red", "meaning": "Competition, conflict, tension."},
    	{"name": "Five of Wands Reversed", "color": "red", "meaning": "Avoiding conflict, compromise."},
    	{"name": "Six of Wands", "color": "red", "meaning": "Success, public recognition."},
    	{"name": "Six of Wands Reversed", "color": "red", "meaning": "Ego, lack of recognition."},
    	{"name": "Seven of Wands", "color": "red", "meaning": "Challenge, competition, perseverance."},
    	{"name": "Seven of Wands Reversed", "color": "red", "meaning": "Giving up, overwhelmed."},
    	{"name": "Eight of Wands", "color": "red", "meaning": "Action, movement, fast-paced change."},
    	{"name": "Eight of Wands Reversed", "color": "red", "meaning": "Delays, frustration, resisting change."},
    	{"name": "Nine of Wands", "color": "red", "meaning": "Resilience, persistence, test of faith."},
    	{"name": "Nine of Wands Reversed", "color": "red", "meaning": "Exhaustion, fatigue."},
    	{"name": "Ten of Wands", "color": "red", "meaning": "Burden, responsibility, stress."},
    	{"name": "Ten of Wands Reversed", "color": "red", "meaning": "Relief, release, letting go."},
    	{"name": "Page of Wands", "color": "red", "meaning": "Inspiration, discovery, enthusiasm."},
    	{"name": "Page of Wands Reversed", "color": "red", "meaning": "Lack of direction, procrastination."},
    	{"name": "Knight of Wands", "color": "red", "meaning": "Energy, passion, adventure."},
    	{"name": "Knight of Wands Reversed", "color": "red", "meaning": "Recklessness, anger, delays."},
    	{"name": "Queen of Wands", "color": "red", "meaning": "Confidence, determination, joy."},
    	{"name": "Queen of Wands Reversed", "color": "red", "meaning": "Jealousy, selfishness, insecurity."},
    	{"name": "King of Wands", "color": "red", "meaning": "Leadership, vision, honor."},
    	{"name": "King of Wands Reversed", "color": "red", "meaning": "Impulsiveness, overbearing."},		
    	# Pentacles - green
    	{"name": "Ace of Pentacles", "color": "green", "meaning": "New financial or career opportunity."},
    	{"name": "Ace of Pentacles Reversed", "color": "green", "meaning": "Lost opportunity, lack of planning."},
    	{"name": "Two of Pentacles", "color": "green", "meaning": "Balance, adaptability, time management."},
    	{"name": "Two of Pentacles Reversed", "color": "green", "meaning": "Disorganization, financial instability."},
    	{"name": "Three of Pentacles", "color": "green", "meaning": "Teamwork, collaboration, building."},
    	{"name": "Three of Pentacles Reversed", "color": "green", "meaning": "Lack of teamwork, disorganization."},
    	{"name": "Four of Pentacles", "color": "green", "meaning": "Saving, security, conservatism."},
    	{"name": "Four of Pentacles Reversed", "color": "green", "meaning": "Greed, financial fear, scarcity."},
    	{"name": "Five of Pentacles", "color": "green", "meaning": "Poverty, insecurity, worry."},
    	{"name": "Five of Pentacles Reversed", "color": "green", "meaning": "Recovery, improvement."},
    	{"name": "Six of Pentacles", "color": "green", "meaning": "Giving, receiving, generosity."},
    	{"name": "Six of Pentacles Reversed", "color": "green", "meaning": "Strings attached, debt, inequality."},
    	{"name": "Seven of Pentacles", "color": "green", "meaning": "Patience, hard work, investment."},
    	{"name": "Seven of Pentacles Reversed", "color": "green", "meaning": "Lack of reward, impatience."},
    	{"name": "Eight of Pentacles", "color": "green", "meaning": "Skill development, mastery, diligence."},
    	{"name": "Eight of Pentacles Reversed", "color": "green", "meaning": "Perfectionism, lack of focus."},
    	{"name": "Nine of Pentacles", "color": "green", "meaning": "Abundance, luxury, self-sufficiency."},
    	{"name": "Nine of Pentacles Reversed", "color": "green", "meaning": "Overinvestment, setbacks."},
    	{"name": "Ten of Pentacles", "color": "green", "meaning": "Wealth, legacy, family, establishment."},
    	{"name": "Ten of Pentacles Reversed", "color": "green", "meaning": "Financial failure, instability."},
    	{"name": "Page of Pentacles", "color": "green", "meaning": "Ambition, diligence, financial news."},
    	{"name": "Page of Pentacles Reversed", "color": "green", "meaning": "Laziness, foolishness."},
    	{"name": "Knight of Pentacles", "color": "green", "meaning": "Hard work, productivity, routine."},
    	{"name": "Knight of Pentacles Reversed", "color": "green", "meaning": "Laziness, obsession."},
    	{"name": "Queen of Pentacles", "color": "green", "meaning": "Nurturing, practicality, providing."},
    	{"name": "Queen of Pentacles Reversed", "color": "green", "meaning": "Self-centeredness, imbalance."},
    	{"name": "King of Pentacles", "color": "green", "meaning": "Security, control, leadership."},
    	{"name": "King of Pentacles Reversed", "color": "green", "meaning": "Greed, stubbornness."},
    ]
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
    #def show_cards():
    draw_button.value  # trigger re-render
    selected_cards = random.sample(tarot_cards, 3)

    images = mo.hstack([
        mo.image(
            src=f"data:image/png;base64,{pil_to_base64(generate_card_image(card))}",
            caption=f"{pos}: {card['name']}"
        ) for pos, card in zip(positions, selected_cards)
    ])

    image_stack = mo.vstack([images])


    mo.vstack([draw_button, image_stack])
    return (selected_cards,)


@app.cell
def _(mo, selected_cards):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    with mo.status.spinner(subtitle="Talking with stars ✨ ...") as _spinner:
    
        model_name = "Qwen/Qwen2.5-0.5B-Instruct"
    
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto"
        )
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Act as a tarot reader and fortune teller. Be creative with your response. The user will provide a list of 3 cards and their meanings each referring to past, present or future, respectively. Tell the user a story about them and don't print a list"},
            {"role": "user", "content": f"REFER TO ME IN SECOND PERSON. TELL ME MY FORTUNE AND DO A CREATIVE AND MISTERIOUS READING. HERE ARE THE CARDS I CHOOSE: PAST: Card:{selected_cards[0]["name"]} Meaning:{selected_cards[0]["meaning"]}; PRESENT: Card:{selected_cards[1]["name"]} Meaning:{selected_cards[1]["meaning"]}; FUTURE: Card:{selected_cards[2]["name"]} Meaning:{selected_cards[2]["meaning"]};"   }
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
    
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    
        _spinner.update(subtitle="Channelling spirits 🔮 ...")
    
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
    
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    mo.md(response)
    return


if __name__ == "__main__":
    app.run()
