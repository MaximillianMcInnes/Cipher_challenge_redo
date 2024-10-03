// components/ComboBox.js
import { useState, FormEvent } from "react";
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


const ComboBox = ({ cipherOptions, selectedCipher, setSelectedCipher }) => {
  const [open, setOpen] = useState(false);

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          className="relative inline-flex items-center justify-between text-white w-[200px] hover:bg-gray-800 transition-colors duration-300 transform hover:scale-105"
        >
          {selectedCipher ? selectedCipher : "Select Cipher Type"}
          <ChevronsUpDown className="ml-2 h-4 w-4" />
        </Button>
      </PopoverTrigger>
      <PopoverContent
        className="w-[200px] p-0 mt-2 bg-gray-700 text-white shadow-lg rounded-md animate-slide-down"
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
                  key={cipher}
                  onSelect={() => {
                    setSelectedCipher(cipher);
                    setOpen(false);
                  }}
                >
                  <Check
                    className={clsx(
                      "mr-2 h-4 w-4",
                      selectedCipher === cipher ? "opacity-100" : "opacity-0"
                    )}
                  />
                  {cipher}
                </CommandItem>
              ))}
            </CommandGroup>
          </CommandList>
        </Command>
      </PopoverContent>
    </Popover>
  );
};

export default ComboBox;
