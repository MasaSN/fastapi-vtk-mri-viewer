from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import vtk
import vtk.util.numpy_support as vtk_np
import numpy as np

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>VTK with FastAPI</title>
        </head>
        <body>
            <h1>VTK Example</h1>
            <div id="container" style="width: 100vw; height: 100vh;"></div>
            <script src="https://unpkg.com/vtk.js"></script>
            <script>
                // Your VTK.js code here
            </script>
        </body>
    </html>
    """

# Add more routes for handling VTK operations if needed

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
