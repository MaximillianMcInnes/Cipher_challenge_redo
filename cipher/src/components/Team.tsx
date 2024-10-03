"use client";
import React from "react";
import { AnimatedTooltip } from "@/components/ui/animated-tooltip";

const Team = () => {
    return (
      <div className="relative text-center"> {/* Center the content */}
        <p className="text-4xl sm:text-7xl font-bold relative z-20 bg-clip-text text-transparent bg-gradient-to-b from-neutral-200 to-neutral-500 py-8">
          Our Team
        </p>
        <div className="relative mt-[5%] p-4">
          <AnimatedTooltipPreview />
        </div>
      </div>
    );
  };
  

export default Team;

const people = [
    {
      id: 1,
      name: "Maximillian McInnes",
      designation: "Senior Full Stack Engineer and Artificial Intelligence Specialist",
      image: "/Max_Mcinnes.jpeg", // Image from public folder
    },
    {
      id: 2,
      name: "Saud Ali",
      designation: "Advanced Cryptographic Systems Developer",
      image: "/Max_Mcinnes.jpeg", // Image from public folder
    },
  ];
  

export function AnimatedTooltipPreview() {
  return (
    <div className="flex flex-row items-center justify-center mb-10 w-full">
      <AnimatedTooltip items={people} />
    </div>
  );
}
