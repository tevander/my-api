from fastapi import FastAPI
from app.db_redshift import get_deployment_data
from app.git_reader import extract_repo_info
from app.prompt_builder import build_prompt
from app.llm_client import call_llm
from app.db_postgres import store_llm_response

app = FastAPI()
@app.get("/summarize/{deployment_id}")
def summarize(deployment_id: str):
    deployment_data = get_deployment_data(deployment_id)
    #print("\nrepo path: ", deployment_data["repo_path"])
    repo_data = extract_repo_info(deployment_data["repo_path"])
    prompt = build_prompt(deployment_data, repo_data)
    llm_response = call_llm(prompt)
    store_llm_response(deployment_id, llm_response)
    return {"llm_response": llm_response}