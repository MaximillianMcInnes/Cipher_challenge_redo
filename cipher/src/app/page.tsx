"use client";
import { useState, FormEvent } from "react";
import Team from "@/components/Team";
import { Separator } from "@/components/ui/separator";
import { Button } from "@/components/ui/button";
import { BackgroundBeamsWithCollisionDemo } from "@/components/front_text";
import { ShineBorder } from "@/components/ui/shine-border";
import { Textarea } from "@headlessui/react";
import clsx from "clsx";
import * as React from "react";
import { Check, ChevronsUpDown } from "lucide-react";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import CubeLoader from '@/components/cubeloader';
import Technologies from "@/components/technologies";

const cipherOptions = [
  { name: "Auto-Solve", label: "auto_solve" },
  { name: "Caesar", label: "caesar" },
  { name: "Affine", label: "affine" },
  { name: "Keyword Substitution", label: "keyword_sub" },
  {name: "Vigenère", label: "Vigenere"},
];

// Decoded_text component to display either the loader or the result
const Decoded_text = ({ text, loading, timeTaken }) => {
  // Format time to seconds and 2 decimal places
  const formattedTime = timeTaken ? (timeTaken / 1000).toFixed(2) : null;

  return (
    <div className="flex items-center justify-center flex-col p-4">
      <ShineBorder
        className="relative flex w-[80%] flex-col z-10 items-center justify-center overflow-visible rounded-lg border-2 border-gray-700 bg-transparent scale-90 md:shadow-xl h-max"
        color={["#A07CFE", "#FE8FB5", "#FFBE7B"]}
      >
        <div className="text-white mt-4">
          {loading ? (
            <CubeLoader />
          ) : (
            text && (
              <>
                <h1 className="text-4xl sm:text-6xl font-bold text-center bg-clip-text text-transparent bg-gradient-to-b from-neutral-200 to-neutral-500 py-4 mb-6">
                  Your Decrypted Text
                </h1>
                <p className="text-lg sm:text-l p-6 leading-relaxed rounded-lg shadow-md">
                  {text}
                </p>
              </>
            )
          )}
          {!loading && formattedTime && (
            <p className="text-sm text-gray-400 mt-4 p-2">
              Time taken: {formattedTime} seconds
            </p>
          )}
        </div>
      </ShineBorder>
    </div>
  );
};


export default function Home() {
  const [inputText, setInputText] = useState<string>("");
  const [outputText, setOutputText] = useState<string>("");
  const [selectedCipher, setSelectedCipher] = useState<string>("Select Cipher");
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [showBox, setShowBox] = useState(false); // New state for controlling box visibility
  const [timeTaken, setTimeTaken] = useState<number | null>(null); // State for time taken

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setShowBox(true); // Show the box on submit

    try {
      // Start measuring time
      const startTime = performance.now();

      // Find the selected cipher's label for the API call
      const selectedCipherLabel = cipherOptions.find(
        (option) => option.name === selectedCipher
      )?.label;

      if (!selectedCipherLabel) {
        throw new Error("Cipher not found");
      }

      const response = await fetch(
        `http://localhost:5000/api/${selectedCipherLabel}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text: inputText }),
        }
      );

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      setOutputText(data["Deciphered Text"]);

      // End measuring time
      const endTime = performance.now();
      setTimeTaken(endTime - startTime); // Calculate and set time taken
    } catch (error) {
      console.error("Error during fetch:", error);
      setOutputText("An error occurred while processing your request.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="relative">
      <BackgroundBeamsWithCollisionDemo />

      <div className="flex items-center justify-center mt-[%]">
        <ShineBorder
          className="relative flex w-[80%] flex-col z-10 items-center justify-center overflow-visible rounded-lg border-2 border-gray-700 bg-transparent scale-90 md:shadow-xl h-max%"
          color={["#A07CFE", "#FE8FB5", "#FFBE7B"]}
        >
          <div className="w-full z-200005 bg-transparent p-4">
            <form onSubmit={handleSubmit}>
              <Textarea
                className={clsx(
                  "custom-scroll block w-full h-[15rem] resize-none rounded-lg border-none bg-transparent py-1.5 px-3 text-sm text-white",
                  "focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-white/25"
                )}
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder="Enter your Cipher Text here ..."
              />

              <div className="p-1 relative border-1 border-white mt-4 p-4 rounded-lg">
                <div className="flex flex-col items-center justify-center space-y-4">
                  <Popover open={open} onOpenChange={setOpen}>
                    <PopoverTrigger asChild>
                      <Button
                        variant="outline"
                        className="relative inline-flex items-center justify-between text-white w-[200px] hover:bg-gray-800 transition-colors duration-300"
                      >
                        {selectedCipher ? selectedCipher : "Select Cipher Type"}
                        <ChevronsUpDown className="ml-2 h-4 w-4" />
                      </Button>
                    </PopoverTrigger>
                    <PopoverContent
                      className="w-[200px] p-0 mt-2 bg-gray-700 text-white shadow-lg rounded-md"
                      align="start"
                      side="bottom"
                    >
                      <Command>
                        <CommandInput placeholder="Search cipher type..." />
                        <CommandList>
                          <CommandEmpty>No cipher found.</CommandEmpty>
                          <CommandGroup>
                            {cipherOptions.map((cipher) => (
                              <CommandItem
                                key={cipher.label}
                                onSelect={() => {
                                  setSelectedCipher(cipher.name);
                                  setOpen(false);
                                }}
                                className={clsx(
                                  "transition-all duration-300 cursor-pointer p-2 hover:bg-gray-600 hover:text-white",
                                  "focus:bg-gray-700 active:scale-95"
                                )}
                              >
                                <Check
                                  className={clsx(
                                    "mr-2 h-4 w-4",
                                    selectedCipher === cipher.name
                                      ? "opacity-100"
                                      : "opacity-0"
                                  )}
                                />
                                {cipher.name}
                              </CommandItem>
                            ))}
                          </CommandGroup>
                        </CommandList>
                      </Command>
                    </PopoverContent>
                  </Popover>

                  <Button
                    variant="outline"
                    className="text-white w-[150px] hover:bg-gray-800 transition-colors duration-300"
                    type="submit"
                    disabled={loading}
                  >
                    {loading ? "Loading..." : "Submit"}
                  </Button>
                </div>
                <div className="text-right text-gray-100 font-bold text-sm absolute right-0 top-0 mt-2 mr-4 pt-4">
                  {inputText.length}/10,000 characters
                </div>
              </div>
            </form>
          </div>
        </ShineBorder>
      </div>
      <div className="relative z-[20] w-[97%] h-[0.2rem] bg-gray-800 opacity-[50%] rounded-full mb-8"></div>

      {/* Conditionally render Decoded_text based on showBox */}
      {showBox && <Decoded_text text={outputText} loading={loading} timeTaken={timeTaken} />}

      <Technologies />
      <Team />
    </div>
  );
}
