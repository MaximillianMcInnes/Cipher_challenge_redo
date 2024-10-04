from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import runpy
import os
import runpy

cipher_text = r"C:\Users\Maximillian Mcinnes\Desktop\Cipher app\backend\back\cipher.txt"
plain_text = r"C:\Users\Maximillian Mcinnes\Desktop\Cipher app\backend\back\plaintext.txt"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Textsolver(BaseModel):
    text: str


################################################################################################################################################################
#affine 


# Define the request body schema
class TextRequest(BaseModel):
    text: str

# Create the /api/affine endpoint that reverses the text

@app.post("/api/keyword_sub")
async def reverse_text(request: Textsolver):
    print(f"Received request with text: {request.text}")  # Add this log
    try:
        # Extract the text from the request
        text = request.text

        # Define paths for the input (cipher_text) and output (plain_text) files

        # Path to the script you want to run
        sub_path = "substiution.py"

        # Write the text to the cipher_text file
        with open(cipher_text, "w", encoding='utf-8') as file:
            file.write(text)

        # Run the external Python script that processes the cipher_text file
        print("befpre run")
        runpy.run_module(sub_path, run_name="__main__")
        print("after running")
        # Read the deciphered text from the plain_text file
        with open(plain_text, "r", encoding='utf-8') as file:
            deciphered_text = file.read()

        # Return the deciphered text in the response
        print(deciphered_text)
        print("aaaaaa")
        
        return {"Deciphered Text": deciphered_text}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




################################################################################################################################################################
@app.post("/api/affine")
async def reverse_text(request: TextRequest):
    try:
        text = request.text

        # Define paths for the input (cipher_text) and output (plain_text) files
        # Path to the script you want to run
        affine_path = r"C:\Users\Maximillian Mcinnes\Desktop\Cipher app\backend\back\Affine.py"

        # Write the text to the cipher_text file
        with open(cipher_text, "w", encoding='utf-8') as file:
            file.write(text)

        # Run the external Python script that processes the cipher_text file
        os.system(affine_path)

        # Read the deciphered text from the plain_text file
        with open(plain_text, "r", encoding='utf-8') as file:
            deciphered_text = file.read()

        # Return the deciphered text in the response
        print(deciphered_text)
        return {"Deciphered Text": deciphered_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




########################################################################################################
#Caesar cipher 


@app.post("/api/caesar")
async def caesar_solver(request: Textsolver):
    input_text = request.text
    print(input_text)
    if not input_text:
        raise HTTPException(status_code=400, detail="No text provided")

    # Define the path for the cipher text file

    # Write the input text to the cipher text file
    with open(cipher_text, "w", encoding='utf-8') as file:
        file.write(input_text)

    # Path to the Caesar solver script
    caesar_path = r"C:\Users\Maximillian Mcinnes\Desktop\Cipher app\backend\back\Caeser.py"

    # Run the Caesar cipher solver script
    try:
        runpy.run_path(caesar_path, run_name="__main__")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running Caesar solver: {str(e)}")

    # Path to the output plain text file
    plain_text_path = r"C:\Users\Maximillian Mcinnes\Desktop\Cipher app\backend\back\plaintext.txt"

    # Read the deciphered text from the plain text file
    try:
        with open(plain_text_path, "r", encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Plaintext file not found after Caesar solver execution.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading plaintext file: {str(e)}")

    # Log or return the deciphered text
    print(text)
    return {"Deciphered Text": text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
