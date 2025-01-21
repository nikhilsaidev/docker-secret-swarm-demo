from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def display_secrets():
    secret_files = ["/run/secrets/kafka.pem", "/run/secrets/sample.pem"]
    secrets = []
    
    for secret_file in secret_files:
        if os.path.exists(secret_file):
            with open(secret_file, "r") as file:
                secrets.append(f"{os.path.basename(secret_file)}: {file.read().strip()}")
        else:
            secrets.append(f"{os.path.basename(secret_file)}: Not Found")
    
    return "<br>".join(secrets)

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=5000)
