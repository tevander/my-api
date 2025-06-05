import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def store_llm_response(deployment_id, response):
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO deployments (id, summary)
            VALUES (%s, %s)
            ON CONFLICT (id) DO UPDATE SET summary = EXCLUDED.summary;
        """, (deployment_id, response))

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Stored the LLM response for deployment {deployment_id}")
    except Exception as e:
        print(f"error storing LLM response: {e}")
        

