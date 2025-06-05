import psycopg2

def store_llm_response(deployment_id, response):
    try:
        conn = psycopg2.connect(
            dbname="testdb",
            user="teddyvw",
            host="localhost",
            port="5432",
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
        

