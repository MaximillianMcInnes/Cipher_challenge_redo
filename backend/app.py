from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import runpy
import os
from pathlib import Path
import subprocess


# Define base directory for scripts and text files
base_dir = Path(__file__).resolve().parent / 'maxs'

# Define paths for cipher and plaintext files
cipher_text = base_dir / 'cipher.txt'
plain_text = base_dir / 'plaintext.txt'

# Initialize FastAPI app
app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Define request body schema
class Textsolver(BaseModel):
    text: str


########################################################################################################
# Keyword Substitution Cipher

@app.post("/api/keyword_sub")
async def keyword_substitution(request: Textsolver):
    print(f"Received request with text: {request.text}")  # Logging request
    try:
        # Extract the text from the request
        text = request.text

        # Define path to the substitution script
        sub_path = base_dir / 'substiution.py'

        # Write the text to the cipher_text file
        with open(cipher_text, "w", encoding='utf-8') as file:
            file.write(text)

        # Run the external Python script that processes the cipher_text file
        print("Before running substitution cipher script")
        subprocess.run(['python', str(sub_path)])
        print("After running substitution cipher script")

        # Read the deciphered text from the plain_text file
        with open(plain_text, "r", encoding='utf-8') as file:
            deciphered_text = file.read()

        # Return the deciphered text in the response
        print(deciphered_text)
        return {"Deciphered Text": deciphered_text}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


########################################################################################################
# Affine Cipher
@app.post("/api/Railfence")
async def affine_solver(request: Textsolver):
    try:
        # Logging the text received
        text = request.text
        print(f"Received text for Railfence Cipher: {text}")
        
        # Ensure base_dir and file paths are correct
        print(f"Base directory: {base_dir}")
        print(f"Cipher text file path: {cipher_text}")
        print(f"Plain text file path: {plain_text}")

        # Write the input text to the cipher_text file
        with open(cipher_text, "w", encoding='utf-8') as file:
            file.write(text)
        print("Successfully wrote cipher text")

        # Define path to the affine cipher script
        affine_path = base_dir / 'railfence.py'
        print(f"railfence script path: {affine_path}")

        # Run the external Python script that processes the cipher_text file
        print("Running railfence cipher script")
        subprocess.run(['python', str(affine_path)])
        print("railfence cipher script executed successfully")

        # Read the deciphered text from the plain_text file
        if plain_text.exists():
            print(f"Plain text file exists: {plain_text}")
            with open(plain_text, "r", encoding='utf-8') as file:
                deciphered_text = file.read()
            print(f"Deciphered text: {deciphered_text}")
        else:
            print(f"Plain text file does not exist: {plain_text}")
            raise HTTPException(status_code=500, detail="Plaintext file not found after Affine solver execution.")

        # Return the deciphered text in the response
        return {"Deciphered Text": deciphered_text}

    except Exception as e:
        print(f"Error during Affine cipher processing: {str(e)}")
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")


@app.post("/api/affine")
async def affine_solver(request: Textsolver):
    try:
        # Logging the text received
        text = request.text
        print(f"Received text for Affine Cipher: {text}")
        
        # Ensure base_dir and file paths are correct
        print(f"Base directory: {base_dir}")
        print(f"Cipher text file path: {cipher_text}")
        print(f"Plain text file path: {plain_text}")

        # Write the input text to the cipher_text file
        with open(cipher_text, "w", encoding='utf-8') as file:
            file.write(text)
        print("Successfully wrote cipher text")

        # Define path to the affine cipher script
        affine_path = base_dir / 'Affine.py'
        print(f"Affine script path: {affine_path}")

        # Run the external Python script that processes the cipher_text file
        print("Running Affine cipher script")
        subprocess.run(['python', str(affine_path)])
        print("Affine cipher script executed successfully")

        # Read the deciphered text from the plain_text file
        if plain_text.exists():
            print(f"Plain text file exists: {plain_text}")
            with open(plain_text, "r", encoding='utf-8') as file:
                deciphered_text = file.read()
            print(f"Deciphered text: {deciphered_text}")
        else:
            print(f"Plain text file does not exist: {plain_text}")
            raise HTTPException(status_code=500, detail="Plaintext file not found after Affine solver execution.")

        # Return the deciphered text in the response
        return {"Deciphered Text": deciphered_text}

    except Exception as e:
        print(f"Error during Affine cipher processing: {str(e)}")
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

########################################################################################################
# Caesar Cipher

@app.post("/api/caesar")
async def caesar_solver(request: Textsolver):
        input_text = request.text
        with open(cipher_text, "w", encoding='utf-8') as file:
            file.write(input_text)
        print("1")

        caesar_path = base_dir / 'Caeser.py'
        print("1")
        # Run the Caesar cipher solver script
        try:
            subprocess.run(['python', str(caesar_path)])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error running Caesar solver: {str(e)}")
        print("1")
        try:
            with open(plain_text, "r", encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            raise HTTPException(status_code=500, detail="Plaintext file not found after Caesar solver execution.")
        print("1")

        # Log or return the deciphered text
        print(text)
        return {"Deciphered Text": text}
########################################################################################################
# Run the FastAPI app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
