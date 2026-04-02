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
            SELECT MAX(similarity) FROM (

                -- Approved Ideas
                SELECT 1 - (embedding <=> %s::vector) AS similarity
                FROM ideas_idea
                WHERE embedding IS NOT NULL
                AND status = 'approved'

                UNION ALL

                -- Approved Projects
                SELECT 1 - (embedding <=> %s::vector) AS similarity
                FROM projects_project
                WHERE embedding IS NOT NULL
                AND status = 'approved'

            ) AS combined;
        """, [new_embedding, new_embedding])

        result = cursor.fetchone()

    if result and result[0] is not None:
        return float(result[0])

    return 0.0