import os

DUMMY_DB_PATH = os.path.expanduser("~/Desktop/dummyDB")

def parse_line(line):
    key, value = line.strip().split("=",1)
    return key.strip(), value.strip()

def get_deployment_data(deployment_id):
    file_path = os.path.join(DUMMY_DB_PATH, f"{deployment_id}.txt")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"no info found LOL. deployment ID: {deployment_id}")
    data = {}
    with open(file_path, "r") as f:
        for line in f:
            if "=" in line:
                key, value = parse_line(line)
                data[key] = value

    tags = data.get("tags", "").split(",")
    metadata = {
        "language": data.get("language", ""),
        "team": data.get("team", "")
    }
    #print(f"[DEBUG] Parsed deployment data: {data}")

    return {
        "id": data.get("id", deployment_id),
        "name": data.get("name", "unknown-service"),
        "tags": tags,
        "metadata": metadata,
        "repo_path": data.get("repo_path", ""),
        "latest_commit": data.get("latest_commit", "")
    }