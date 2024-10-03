import React from "react";
import Link from "next/link";
import { RainbowButton } from "@/components/magicui/rainbow-button"; // Assuming you want to use this somewhere

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white p-8 md:p-12">
      <div className="relative z-[20]  w-full h-[0.2rem] bg-gray-800 opacity-[50%] rounded-full mb-[2%] "></div>

      <div className="container mx-auto flex flex-col md:flex-row justify-between items-center">
        {/* Logo or Branding */}
        <div className="mb-6 md:mb-0">
          <h2 className="text-2xl font-bold">Cipher App</h2>
        </div>

        {/* Navigation Links */}
        <div className="flex space-x-8 mb-6 md:mb-0">
          <Link
            href="/"
            className="hover:text-blue-400 transition-colors text-lg"
          >
            Homepage
          </Link>
          <Link
            href="/about"
            className="hover:text-blue-400 transition-colors text-lg"
          >
            About
          </Link>
          <Link
            href="/contact"
            className="hover:text-blue-400 transition-colors text-lg"
          >
            Contact
          </Link>
        </div>

        {/* Social Media Icons */}
        <div className="flex space-x-6">
          <Link href="https://twitter.com">
            <img
              src="/icons/twitter.svg"
              alt="Twitter"
              className="h-6 w-6 hover:opacity-75 transition-opacity"
            />
          </Link>
          <Link href="https://facebook.com">
            <img
              src="/icons/facebook.svg"
              alt="Facebook"
              className="h-6 w-6 hover:opacity-75 transition-opacity"
            />
          </Link>
          <Link href="https://instagram.com">
            <img
              src="/icons/instagram.svg"
              alt="Instagram"
              className="h-6 w-6 hover:opacity-75 transition-opacity"
            />
          </Link>
        </div>
      </div>

      {/* Copyright Section */}
      <div className="mt-8 text-center text-gray-400 text-sm">
        &copy; 2023 Cipher App. All rights reserved.
      </div>
    </footer>
  );
};

export default Footer;
