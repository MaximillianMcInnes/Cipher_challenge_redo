import React from 'react';
import Link from 'next/link';
import { RainbowButton } from "@/components/magicui/rainbow-button";

const Navbar = () => {
  return (
    <div className="flex flex-col items-center justify-between h-24 w-full">
      <div className="flex w-full justify-between items-center">
        <div className="flex-1 text-center text-4xl font-bold sm:text-left sm:text-3xl md:text-3xl lg:text-3xl">
          {/* Add a logo or brand name if necessary */}
        </div>
        <div className="flex items-center gap-5 flex-1 text-xl lg:text-lg lg:gap-4 md:gap-4 md:text-lg text-white">
          <Link href="/" className="hover:text-blue-500 transition-colors">Homepage</Link>
          <Link href="/contact" className="hover:text-blue-500 transition-colors">Contact</Link>
          <Link href="/about" className="hover:text-blue-500 transition-colors">About</Link>
        </div>
        <div className="flex items-center p-5">
          <RainbowButton>
            Donate
          </RainbowButton>
        </div>
      </div>
      {/* Divider at the bottom */}
      <div className="relative z-[20]  w-[97%] h-[0.2rem] bg-gray-800 opacity-[50%] rounded-full"></div>
      </div>
  );
}

export default Navbar;
