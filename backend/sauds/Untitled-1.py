import runpy

sub_path = "substiution.py"
# Write the text to the cipher_text file


        # Run the external Python script that processes the cipher_text file
print("befpre run")
runpy.run_module(sub_path, run_name="__main__")