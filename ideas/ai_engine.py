from sentence_transformers import SentenceTransformer
from django.db import connection

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def generate_embedding(text):
    model = get_model()
    embedding = model.encode(text)
    return embedding.tolist()


def check_similarity(new_embedding):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT MAX(1 - (embedding <=> %s::vector))
            FROM ideas_idea
            WHERE embedding IS NOT NULL
        """, [new_embedding])

        result = cursor.fetchone()

    if result and result[0] is not None:
        return float(result[0])

    return 0.0