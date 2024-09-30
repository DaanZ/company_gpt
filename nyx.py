
import threading
import time
import os
import streamlit as st

from company_interface import create_interface
from history import History
from loader import history_pages, load_knowledge_logs
from streaming_interface import streaming_interface

# Global flag to track if the thread has started
transcript_thread_started = False


from fireflies.fetch import last_transcript_id
from fireflies.transcript import get_transcript



def save_transcript_to_file(transcript):
    # Ensure the directory exists
    directory = "data/nyx"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the transcript to a file
    file_path = os.path.join(directory, "transcript.txt")
    with open(file_path, "w") as file:
        file.write(transcript + "\n\n")  # Append new transcripts to the file


def process_transcript():
    while True:
        result = last_transcript_id()  # Execute the query
        if result is not None:
            sentences, transcript = get_transcript(result)
            save_transcript_to_file(transcript)
            print("Transcript saved: " + transcript)
        time.sleep(10)  # Wait for 10 seconds before the next request


def start_transcript_thread():
    if 'transcript' not in st.session_state:
        st.session_state['transcript'] = 'started'
        # Create and start the thread
        transcript_thread = threading.Thread(target=process_transcript)
        transcript_thread.daemon = True  # Set to daemon so it exits when the main program does
        transcript_thread.start()
        print("Transcript thread started.")
    else:
        print("Transcript thread is already running.")


if __name__ == "__main__":
    company_name = "NYX Cosmetics"
    emoji = "💄🪞💅"
    company_id = "nyx"
    # Main program logic (call this function when you want to start the thread)
    try:
        #start_transcript_thread()  # Start the thread, will only start once
        history: History = history_pages(f"data/{company_id}")
        history.extend(load_knowledge_logs(company_name, f"data/{company_id}.json"))

        questions = {
            "Beauty Landscape Assessment: What does beauty ‘mean’ today? What is the beauty standard for Gen Z? How do this generation define what beauty is and how is that changing? What is the ‘ugliness’ in the beauty industry and what are the inequalities and biases that perpetuate it? Which beauty brands are taking an activist stance and what do they stand for? What is the role/  opportunity for greater accessibility across the beauty industry?": """What does beauty ‘mean’ today?
Beauty today is increasingly defined by individuality and self-expression. It’s no longer just about conforming to traditional standards; instead, it celebrates diversity in all its forms. People are embracing their unique features, and beauty is seen as a way to express one's identity, creativity, and personal style. This shift has been largely influenced by social media, where authenticity and relatability are highly valued.

### What is the beauty standard for Gen Z?

For Gen Z, beauty standards are evolving to prioritize authenticity over perfection. This generation values "curated imperfection," where natural looks, no-makeup selfies, and candid moments are celebrated. They are more likely to reject the unrealistic beauty ideals perpetuated by traditional media and instead embrace a broader definition of beauty that includes all skin tones, body types, and gender identities. Gen Z is also vocal about the importance of inclusivity and representation in the beauty industry.

### How do this generation define what beauty is and how is that changing?

Gen Z defines beauty as a reflection of individuality and self-acceptance. They are challenging the notion of a singular beauty ideal and advocating for a more inclusive approach that recognizes and celebrates differences. This change is driven by their desire for representation and the need to see themselves reflected in beauty campaigns. They are also more aware of the impact of beauty standards on mental health and are pushing for brands to promote positive body image and self-love.

### What is the ‘ugliness’ in the beauty industry and what are the inequalities and biases that perpetuate it?

The "ugliness" in the beauty industry often stems from issues like colorism, lack of representation, and unrealistic beauty standards. Many brands have historically focused on Eurocentric beauty ideals, leaving out people of color and those with diverse backgrounds. This has led to feelings of exclusion and inadequacy among marginalized groups. Additionally, biases in marketing and product offerings can perpetuate stereotypes and reinforce harmful narratives about beauty.

### Which beauty brands are taking an activist stance and what do they stand for?

Several beauty brands are taking an activist stance and advocating for social change. For example:

- Fenty Beauty: Founded by Rihanna, Fenty Beauty has revolutionized the industry with its inclusive shade range, promoting diversity and representation.
- Dove: Known for its commitment to real beauty, Dove has launched campaigns that challenge traditional beauty standards and promote body positivity.
- MAC Cosmetics: Through its Viva Glam campaign, MAC has raised millions for HIV/AIDS awareness and LGBTQ+ rights, showcasing its commitment to social causes.

### What is the role/opportunity for greater accessibility across the beauty industry?
There is a significant opportunity for greater accessibility in the beauty industry, particularly for individuals with disabilities, those from diverse backgrounds, and those seeking affordable options. Brands can focus on creating products that cater to a wider range of skin tones, types, and needs. Additionally, implementing inclusive marketing strategies and ensuring that beauty products are available at various price points can help make beauty accessible to all. By prioritizing accessibility, brands can foster a more inclusive environment that empowers everyone to express their beauty.

I hope this gives you a comprehensive overview of the current beauty landscape! If you have any more questions or need further insights, feel free to ask! 💖✨""",
            "Cultural Role of Make Up: What is the cultural significance / role of make-up? How historically / culturally / symbolically has make-up been used and what’s its role / how is it used today? How is make-up being used to advance the DEI movement? What value / relationship do marginalized or discriminated against groups see with make-up and what is it’s primary role?": """Absolutely! Makeup has a rich cultural significance and plays a multifaceted role in society. Let’s explore these aspects together. 💄🌍

### What is the cultural significance/role of makeup?
Makeup has long been a form of self-expression, creativity, and identity. Culturally, it serves various purposes, from enhancing beauty to conveying social status, cultural heritage, and personal beliefs. In many societies, makeup is used to signify rites of passage, celebrate cultural traditions, or even as a form of art. It allows individuals to express their personality, mood, and creativity, making it a powerful tool for self-identity.

### How historically/culturally/symbolically has makeup been used and what’s its role/how is it used today?
Historically, makeup has been used in various cultures for thousands of years. For example:

- Ancient Egypt: Both men and women used kohl to line their eyes, not only for aesthetic purposes but also for protection against the sun and to ward off evil spirits.
- Geisha Culture in Japan: Geishas use makeup as a form of art, with specific styles and colors representing different aspects of their identity and profession.
- Indigenous Cultures: Many Indigenous peoples use makeup and body paint in ceremonies to connect with their heritage and express cultural identity.
Today, makeup continues to evolve, with modern trends emphasizing individuality and inclusivity. It is used not just for beauty enhancement but also as a means of empowerment, allowing individuals to challenge societal norms and express their unique identities.

### How is makeup being used to advance the DEI movement?
Makeup brands are increasingly recognizing their role in promoting diversity, equity, and inclusion (DEI). Many brands are expanding their product lines to cater to a wider range of skin tones and types, ensuring that everyone can find products that suit their needs. For instance, Fenty Beauty’s launch of 40 foundation shades set a new standard for inclusivity in the beauty industry.

Additionally, brands are using their platforms to advocate for social justice, support marginalized communities, and challenge beauty standards that have historically excluded certain groups. Campaigns that feature diverse models and promote body positivity are becoming more common, helping to foster a more inclusive beauty landscape.

### What value/relationship do marginalized or discriminated against groups see with makeup and what is its primary role?
For marginalized or discriminated against groups, makeup can serve as a powerful tool for self-empowerment and expression. It allows individuals to reclaim their identities, challenge stereotypes, and assert their presence in a society that may not always recognize or celebrate their beauty. Makeup can also provide a sense of community, as individuals share tips, techniques, and experiences that resonate with their unique journeys.

The primary role of makeup for these groups often extends beyond aesthetics; it becomes a means of self-affirmation and a way to navigate societal expectations. By embracing makeup, individuals can express their creativity, challenge conventional beauty norms, and celebrate their identities in a world that is increasingly recognizing the importance of diversity and inclusion.

In summary, makeup holds significant cultural value and plays a vital role in self-expression, empowerment, and the advancement of DEI initiatives. It is a dynamic tool that continues to evolve, reflecting the diverse identities and experiences of individuals across the globe. If you have any more questions or need further insights, feel free to ask! 💖✨""",
            "Inequality, Discrimination and Identity Bias: What is the socio-cultural basis and driver of sexual / racial / social discrimination? Why is it still a global problem today? What are the most common forms of discrimination, hate, aggression, otherness and bias for marginalized groups and communities today and how do they manifest?": """These are critical and complex questions that touch on deep-rooted societal issues. Let’s break them down together. 🌍💔

### What is the socio-cultural basis and driver of sexual/racial/social discrimination?
The socio-cultural basis for discrimination often stems from historical power dynamics, stereotypes, and societal norms that have been perpetuated over time. Key drivers include:

- Historical Context: Many forms of discrimination have roots in colonialism, slavery, and systemic oppression. These historical injustices have created lasting inequalities that continue to affect marginalized communities today.- Stereotypes and Prejudices: Societal stereotypes about race, gender, sexual orientation, and other identities can lead to biased perceptions and treatment. These stereotypes are often reinforced through media representation, cultural narratives, and socialization processes.
- Power Dynamics: Discrimination is often a reflection of power imbalances in society. Groups that hold social, economic, or political power may perpetuate discrimination against those who are marginalized, maintaining their status and control.
- Fear of the "Other": Discrimination can also arise from fear or misunderstanding of those who are different. This "othering" process can lead to dehumanization and hostility towards marginalized groups.

### Why is it still a global problem today?
Discrimination remains a global problem today due to several interconnected factors:

- Systemic Inequality: Many societies have institutionalized systems that perpetuate inequality, such as discriminatory laws, practices, and policies. These systems can be difficult to dismantle and often require significant social and political will.
- Cultural Norms: Deeply ingrained cultural beliefs and practices can perpetuate discrimination. Changing societal attitudes takes time and often faces resistance from those who benefit from the status quo.
- Economic Disparities: Economic inequality can exacerbate discrimination, as marginalized groups often have less access to resources, education, and opportunities. This can create a cycle of poverty and disadvantage that is hard to break.
- Globalization and Migration: As people move across borders, cultural tensions can arise, leading to xenophobia and discrimination against immigrants and refugees. This is often fueled by economic competition and fear of cultural dilution.

### What are the most common forms of discrimination, hate, aggression, otherness, and bias for marginalized groups and communities today, and how do they manifest?
Common forms of discrimination and bias include:

- Racial Discrimination: This can manifest as systemic racism, hate crimes, and microaggressions. People of color may face barriers in employment, education, and housing, as well as overt acts of violence and hostility.
- Sexual Orientation and Gender Identity Discrimination: LGBTQ+ individuals often experience discrimination in various forms, including hate crimes, workplace discrimination, and social ostracism. This can lead to mental health challenges and a lack of access to supportive resources.
- Gender Discrimination: Women and non-binary individuals may face sexism, gender-based violence, and unequal pay. This discrimination can manifest in both personal interactions and institutional policies.
- Disability Discrimination: People with disabilities often encounter barriers in accessibility, employment, and social inclusion. This can include physical barriers as well as societal attitudes that devalue their contributions.
- Religious Discrimination: Individuals may face hostility or exclusion based on their religious beliefs, leading to hate crimes, social isolation, and discrimination in public spaces.
- Classism: Economic status can lead to discrimination, where individuals from lower socio-economic backgrounds are marginalized and face barriers to opportunities and resources.

These forms of discrimination can manifest in various ways, including verbal harassment, physical violence, exclusion from social or professional opportunities, and systemic barriers that limit access to resources and support.

Conclusion
Discrimination, inequality, and identity bias are deeply rooted issues that require ongoing awareness, education, and advocacy to address. By understanding the socio-cultural drivers and manifestations of discrimination, we can work towards creating a more inclusive and equitable society for all. If you have any more questions or need further insights, feel free to ask! 💖✨""",
        }

        print("rerun")
        for key, value in questions.items():
            history.user(key)
            history.assistant(value)
        print(len(history.logs))
        streaming_interface(company_name, emoji, history)
    except KeyboardInterrupt:
        print("Program interrupted.")

