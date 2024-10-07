from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import runpy
import os
import runpy
from pathlib import Path
import subprocess


base_dir = Path(__file__).resolve().parent / 'maxs'


cipher_text = base_dir / 'cipher.txt'
plain_text = base_dir / 'plaintext.txt'

def main():
        input_text = input("enter cipher text \n : ")
        with open(cipher_text, "w", encoding='utf-8') as file:
            file.write(input_text)

        caesar_path = base_dir / 'Caeser.py'

        # Run the Caesar cipher solver script
        try:
            subprocess.run(['python', str(caesar_path)])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error running Caesar solver: {str(e)}")

        try:
            with open(plain_text, "r", encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            raise HTTPException(status_code=500, detail="Plaintext file not found after Caesar solver execution.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading plaintext file: {str(e)}")

        # Log or return the deciphered text
        print(text)
        return {"Deciphered Text": text}


if __name__ == "__main__":
    main()