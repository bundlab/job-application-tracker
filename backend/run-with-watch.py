import subprocess
from watchfiles import watch

print("Watching for changes... Press Ctrl+C to stop")

for changes in watch("."):
    print("File changed → restarting server")
    try:
        subprocess.run(["uvicorn", "app.main:app", "--port", "8000"], check=True)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Server crashed: {e}")
