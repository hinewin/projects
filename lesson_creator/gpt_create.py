from openai import OpenAI

client = OpenAI() # default is `OPENAI_APIKEY`

def lesson_structure(topic, custom_content=""):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an educational assistant skilled in structuring informative textbook content.\
             Ensure the output is in well-organized Markdown format with a clear title and table of contents."},
            {
                "role": "user",
                "content": (
                    f"Create a detailed lesson structure for the topic '{topic}'. "
                    "Feel free to determine the number of chapters and sub-chapters as needed. "
                    "Include clear headings, explanations, practical examples, and relevant insights. "
                    "Make sure to provide a cohesive flow of information that enhances understanding and encourages exploration."
                    f"{custom_content}"
                )
            }
        ]
    )

    return completion.choices[0].message.content

def chapter_content(topic, custom_content=""):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an educational assistant dedicated to developing informative and engaging textbook content.\
            Ensure the output is structured in Markdown format. Tittle will always be in this format: Chapter #: Topic and create table of content"},
            {
                "role": "user",
                "content": (
                    f"Create a comprehensive chapter on '{topic}'. "
                    "Focus on providing clear explanations, practical examples, and relevant insights that facilitate understanding. "
                    "Include background information to contextualize the topic, elaborate on key concepts, and discuss real-world applications. "
                    "Conclude with thought-provoking remarks to encourage further exploration of the subject."
                    f"{custom_content}"
                )
            }
        ]
    )

    return (completion.choices[0].message.content)


