def build_prompt(deployment, repo_info):
    return f"""
I need you to summarize this development change in a human readable way. Here is all of the context/information:\n
Deployment: {deployment['name']}
Tags: {', '.join(deployment['tags'])}

README:
{repo_info['readme']}

Latest Commit:
{deployment['latest_commit']}
"""