from langchain_groq import ChatGroq
from langchain_classic import LLMChain
from langchain_classic.chains import SequentialChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.6
)


def generate_name(cuisine):

    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest me a fancy name. Give me only one name"
    )

    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="restaurant_name"
    )

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""
        I want to open a restaurant named {restaurant_name}.
        Suggest 5 menu items for this restaurant.
        Return ONLY the menu item names.
        Put each menu item on a separate line.
        Do not use numbers, bullets, headings, tables, markdown, descriptions, or special characters.
""")

    food_items_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_items,
        output_key="menu_items"
    )

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )

    response = chain.invoke({"cuisine": cuisine})

    return response


if __name__ == "__main__":
    print(generate_name("Italian"))