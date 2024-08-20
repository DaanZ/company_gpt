from cto_toolshed.ai.llm.history import History
from cto_toolshed.util.files import json_read_file

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

openai_embeddings = OpenAIEmbeddings()


def load_knowledge_documents(path: str = "project.json"):
    texts = load_knowledge(path)
    pages = []
    for text in texts:
        pages.append(Document(page_content=text))

    return pages


def load_knowledge_logs(path: str = "project.json"):
    texts = load_knowledge(path)
    history = History()
    for text in texts:
        history.system(Document(page_content=text))

    return history



def load_knowledge(path: str = "project.json"):
    data = json_read_file(path)

    texts = []
    keys = ["content", "segment", "product", "industry", "audience", "business"]
    meta_info = "Centerline is: "
    for key in keys:
        if key in data:
            meta_info += "\n- " + key + ": " + data[key]
    texts.append(meta_info)

    competitor_info = "Competitors are: "
    for competitor in data["competitors"]:
        competitor_info += "\n- " + competitor["name"]
    texts.append(competitor_info)

    for chapter in data["chapters"]:
        title = chapter["title"]
        for research in chapter["research"]:
            texts.append(title + " - " + research["section"] + ": " + research["report"])
        texts.append(title + ": " + chapter["introduction"])
        # TODO remove double named sections
        for section in chapter["sections"]:
            for s in section["sections"]:
                texts.append(title + " - " + section["title"] + " - " + s["section"] + ": " + s["paragraph"])
        texts.append(title + ": " + chapter["recommendation"])

    return texts




if __name__ == "__main__":
    load_knowledge_base()