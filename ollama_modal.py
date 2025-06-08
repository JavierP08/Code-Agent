import asyncio
import subprocess
import modal

MODEL_DIR = "/ollama_models"
OLLAMA_VERSION = "0.7.1"
OLLAMA_PORT = 11434
MODELS_TO_DOWNLOAD = ["qwen3:14b"]

ollama_image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("curl", "ca-certificates")
    .run_commands(
        f"OLLAMA_VERSION={OLLAMA_VERSION} curl -fsSL https://ollama.com/install.sh | sh",
        f"mkdir -p {MODEL_DIR}",
    )
    .env({
        "OLLAMA_HOST": f"0.0.0.0:{OLLAMA_PORT}",
        "OLLAMA_MODELS": MODEL_DIR,
    })
)

app = modal.App("Qwen-model", image=ollama_image)
model_volume = modal.Volume.from_name("Qwen3-models", create_if_missing=True)

@app.cls(
    gpu="A10G",
    volumes={MODEL_DIR: model_volume},
    timeout=300,
    min_containers=0, 
)
class OllamaServer:
    ollama_process: subprocess.Popen | None = None

    @modal.enter()
    async def start_ollama(self):
        self.ollama_process = subprocess.Popen(["ollama", "serve"])
        await asyncio.sleep(10)
        current_models = subprocess.run(["ollama", "list"], capture_output=True, text=True).stdout

        for model in MODELS_TO_DOWNLOAD:
            if model not in current_models:
                proc = await asyncio.create_subprocess_exec("ollama", "pull", model)
                await proc.wait()
                await asyncio.get_running_loop().run_in_executor(None, model_volume.commit)

    @modal.exit()
    def stop_ollama(self):
        if self.ollama_process and self.ollama_process.poll() is None:
            self.ollama_process.terminate()

    @modal.web_server(port=OLLAMA_PORT)
    def serve(self):
        pass
