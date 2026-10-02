# Restaurant Name & Menu Generator

A mini Generative AI application that generates a creative restaurant name based on the selected cuisine and then creates 5 menu items for the generated restaurant.

The project was built as part of my learning journey in **Generative AI and LangChain**.

## Features

- Select a cuisine from the available options
- Generate a creative restaurant name using an LLM
- Generate 5 menu items based on the generated restaurant name
- Simple and interactive Streamlit interface
- Uses LangChain Sequential Chains to connect multiple LLM tasks

## Tech Stack

- **Python**
- **LangChain**
- **LangChain Classic**
- **Groq**
- **Streamlit**
- **python-dotenv**
- **LLM:** `openai/gpt-oss-20b`

## 🔄 How It Works

The application uses a two-step sequential chain:

User selects cuisine
        ↓
Restaurant Name Generation
        ↓
Generated Restaurant Name
        ↓
Menu Item Generation
        ↓
5 Menu Items
Chain 1 — Restaurant Name

The selected cuisine is passed to an LLM through a LangChain prompt template.

Example:

Cuisine → Italian
       ↓
Restaurant Name → Sogno d'Oro
Chain 2 — Menu Items

The generated restaurant name is then passed to a second LLM chain to generate menu items.

Restaurant Name → Sogno d'Oro
       ↓
Menu Items
       ↓
5 suggested dishes

📁 Project Structure
restaurant-name-generator/
│
├── main.py
├── langchain_helper.py
├── requirements.txt
├── .gitignore
└── README.md

The .env file containing the Groq API key is not included in the repository for security reasons.

⚙️ Installation
1. Clone the repository
git clone https://github.com/Srividhya1909/restaurant-name-generator.git
2. Navigate to the project directory
cd restaurant-name-generator
3. Install the required packages
pip install -r requirements.txt
4. Set up the Groq API key

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key

Replace your_groq_api_key with your actual Groq API key.

5. Run the application
streamlit run main.py

The application will open in your browser.

Example

Select a cuisine such as:

Italian

The application generates:

Restaurant Name:
Sogno d'Oro

Menu Items:
Pizza
Pasta
Risotto
Tiramisu
Bruschetta

The generated results may vary because they are produced by an LLM.

 What I Learned

Through this project, I gained hands-on experience with:

Generative AI concepts
Working with LLMs
LangChain
PromptTemplate
LLMChain
SequentialChain
Connecting multiple LLM tasks
Groq API integration
Environment variables and API key security
Building a simple AI application with Streamlit

 Future Improvements
Add restaurant description generation
Generate menu items based on vegetarian/non-vegetarian preferences
Add menu item descriptions and pricing
Improve UI design
Add downloadable menu generation
Add more customization options

 Author
Srividhya
B.Sc. Computer Science with Artificial Intelligence
Interested in Generative AI, Data Science, Machine Learning, and AI Applic
