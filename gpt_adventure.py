import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("❌ Missing environment variable: OPENAI_API_KEY")

client = openai.OpenAI(
    api_key=api_key
)

def get_setup():
    print("🎮 Welcome to GPT Adventure — Your Story Begins!\n")
    language = input("🌐 Choose a language (e.g., English, Korean, Spanish): ")
    genre = input("📚 Choose a genre (fantasy, sci-fi, horror, etc.): ")
    system_prompt = {
        "role": "system",
        "content": f"You are a creative and descriptive storyteller who writes in the genre of {genre} and responds in {language}. Speak like a wise narrator guiding the player through a text-based adventure. Keep it vivid and immersive."
    }
    return language, genre, [system_prompt]

def show_help():
    print("""
🆘 Available commands:
/help     → Show this help menu
/restart  → Restart the story from the beginning
/save     → Save story so far to story_log.txt
/quit     → Exit the game
""")

language, genre, conversation = get_setup()
turn_count = 0
chapter = 1

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ['/quit', 'q']:
        print("👋 Story ended. Thanks for playing!")
        break
    elif user_input.lower() == '/help':
        show_help()
        continue
    elif user_input.lower() == '/restart':
        print("🔄 Restarting story...")
        language, genre, conversation = get_setup()
        turn_count = 0
        chapter = 1
        continue
    elif user_input.lower() == '/save':
        print("💾 Story manually saved to story_log.txt.")
        with open("story_log.txt", "a", encoding="utf-8") as f:
            f.write("🔄 --- Manual Save Point ---\n\n")
        continue

    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        reply = response.choices[0].message.content
    except Exception as e:
        print("❌ Error from GPT:", e)
        break

    print(f"\nGPT (Chapter {chapter}):", reply)

    conversation.append({"role": "assistant", "content": reply})
    turn_count += 1

    with open("story_log.txt", "a", encoding="utf-8") as f:
        f.write("You: " + user_input + "\n")
        f.write("GPT: " + reply + "\n\n")

    if turn_count == 10:
        print(f"\n📘 Chapter {chapter} complete.")
        next_chapter = input("Type 'next' to continue or '/quit' to exit: ")

        if next_chapter.lower() == 'next':
            chapter += 1
            turn_count = 0
            print(f"\n📖 Chapter {chapter} begins...\n")
        else:
            print("📕 Adventure closed.")
            break
