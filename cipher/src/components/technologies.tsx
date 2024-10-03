"use client";
import { animate, motion } from "framer-motion";
import React, { useEffect, useState } from "react";
import { cn } from "@/lib/utils";
import { GoCopilot } from "react-icons/go";

const Technologies = () => {
  return (
    <div className="relative w-full">
      <div className="mt-[7%] flex flex-col justify-center items-center">
        <p className="text-4xl sm:text-7xl font-bold relative z-20 bg-clip-text text-transparent bg-gradient-to-b from-neutral-200 to-neutral-500 py-8">
          How We Do It
        </p>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-8 w-full max-w-6xl">
          <CardPython />
          <MachineLearning />
          <CardRust />
        </div>
      </div>
      <div className="mt-[5%] relative z-[20] w-[97%] h-[0.2rem] bg-gray-800 opacity-[50%] rounded-full mb-8"></div>
    </div>
  );
};

export default Technologies;

export function CardPython() {
  return (
    <Card>
      <CardSkeletonContainer>
        <Skeleton />
      </CardSkeletonContainer>
      <CardTitle>Python</CardTitle>
      <CardDescription>
        We use Python for some decryption algorithms and as part of our backend,
        including FastAPI, Django, and Python 3.12.
      </CardDescription>
    </Card>
  );
}

export function CardRust() {
  return (
    <Card>
      <CardSkeletonContainer>
        <Skeleton3 />
      </CardSkeletonContainer>
      <CardTitle>Rust</CardTitle>
      <CardDescription>
        Some parts of our backend are developed using Rust with a focus on
        speed. For more complex algorithms, we implement Rust to reduce waiting
        times. However, due to the lack of support for certain packages, such as
        those for machine learning, we face limitations in its full adoption.
      </CardDescription>
    </Card>
  );
}

export function MachineLearning() {
  return (
    <Card>
      <CardSkeletonContainer>
        <Skeleton2 />
      </CardSkeletonContainer>
      <CardTitle>Artificial Intelligence</CardTitle>
      <CardDescription>
        We use Python libraries including scikit-learn, NumPy, and TensorFlow
        for our custom-built cipher detection. Our datasets are free to use upon
        request.
      </CardDescription>
    </Card>
  );
}

const Skeleton3 = () => {
  const scale = [1, 1.1, 1];
  const transform = ["translateY(0px)", "translateY(-4px)", "translateY(0px)"];
  const sequence = [
    [
      ".circle-1",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-2",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-3",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-4",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-5",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
  ];

  useEffect(() => {
    // @ts-ignore
    animate(sequence, {
      repeat: Infinity,
      repeatDelay: 1,
    });
  }, []);
  return (
    <div className="p-8 overflow-hidden h-full relative flex items-center justify-center">
      <div className="flex flex-row flex-shrink-0 justify-center items-center gap-2">
        <Container className="h-8 w-8 circle-5">
          <RustTool className="h-4 w-4 " />
        </Container>
        <Container className="circle-3">
          <Rust className="h-8 w-8 dark:text-white" />
        </Container>
        <Container className="h-8 w-8 circle-5">
          <RustAPI className="h-4 w-4 " />
        </Container>
      </div>

      <div className="h-40 w-px absolute top-20 m-auto z-40 bg-gradient-to-b from-transparent via-cyan-500 to-transparent animate-move">
        <div className="w-10 h-32 top-1/2 -translate-y-1/2 absolute -left-10">
          <Sparkles />
        </div>
      </div>
    </div>
  );
};

const Skeleton2 = () => {
  const scale = [1, 1.1, 1];
  const transform = ["translateY(0px)", "translateY(-4px)", "translateY(0px)"];
  const sequence = [
    [
      ".circle-1",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-2",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-3",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-4",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-5",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
  ];

  useEffect(() => {
    // @ts-ignore
    animate(sequence, {
      repeat: Infinity,
      repeatDelay: 1,
    });
  }, []);
  return (
    <div className="p-8 overflow-hidden h-full relative flex items-center justify-center">
      <div className="flex flex-row flex-shrink-0 justify-center items-center gap-2">
        <Container className="h-8 w-8 circle-5">
          <SkilitLearn className="h-4 w-4 " />
        </Container>
        <Container className="circle-3">
          <TensorFlow className="h-8 w-8 dark:text-white" />
        </Container>
        <Container className="h-8 w-8 circle-5">
          <Numpy className="h-4 w-4 " />
        </Container>
      </div>

      <div className="h-40 w-px absolute top-20 m-auto z-40 bg-gradient-to-b from-transparent via-cyan-500 to-transparent animate-move">
        <div className="w-10 h-32 top-1/2 -translate-y-1/2 absolute -left-10">
          <Sparkles />
        </div>
      </div>
    </div>
  );
};

const Skeleton = () => {
  const scale = [1, 1.1, 1];
  const transform = ["translateY(0px)", "translateY(-4px)", "translateY(0px)"];
  const sequence = [
    [
      ".circle-1",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-2",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-3",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-4",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
    [
      ".circle-5",
      {
        scale,
        transform,
      },
      { duration: 0.8 },
    ],
  ];

  useEffect(() => {
    // @ts-ignore
    animate(sequence, {
      repeat: Infinity,
      repeatDelay: 1,
    });
  }, []);
  return (
    <div className="p-8 overflow-hidden h-full relative flex items-center justify-center">
      <div className="flex flex-row flex-shrink-0 justify-center items-center gap-2">
        <Container className="h-8 w-8 circle-5">
          <FastAPILogo className="h-4 w-4 " />
        </Container>
        <Container className="circle-3">
          <PythonLogo className="h-8 w-8 dark:text-white" />
        </Container>
        <Container className="h-8 w-8 circle-5">
          <Numpy className="h-4 w-4 " />
        </Container>
      </div>

      <div className="h-40 w-px absolute top-20 m-auto z-40 bg-gradient-to-b from-transparent via-cyan-500 to-transparent animate-move">
        <div className="w-10 h-32 top-1/2 -translate-y-1/2 absolute -left-10">
          <Sparkles />
        </div>
      </div>
    </div>
  );
};

const Sparkles = () => {
  const randomMove = () => Math.random() * 2 - 1;
  const randomOpacity = () => Math.random();
  const random = () => Math.random();
  return (
    <div className="absolute inset-0">
      {[...Array(12)].map((_, i) => (
        <motion.span
          key={`star-${i}`}
          animate={{
            top: `calc(${random() * 100}% + ${randomMove()}px)`,
            left: `calc(${random() * 100}% + ${randomMove()}px)`,
            opacity: randomOpacity(),
            scale: [1, 1.2, 0],
          }}
          transition={{
            duration: random() * 2 + 4,
            repeat: Infinity,
            ease: "linear",
          }}
          style={{
            position: "absolute",
            top: `${random() * 100}%`,
            left: `${random() * 100}%`,
            width: `2px`,
            height: `2px`,
            borderRadius: "50%",
            zIndex: 1,
          }}
          className="inline-block bg-black dark:bg-white"
        ></motion.span>
      ))}
    </div>
  );
};

export const Card = ({
  className,
  children,
}: {
  className?: string;
  children: React.ReactNode;
}) => {
  return (
    <div
      className={cn(
        "max-w-sm w-full mx-auto p-8 rounded-xl border border-[rgba(255,255,255,0.10)] dark:bg-[rgba(40,40,40,0.70)] bg-gray-100 shadow-[2px_4px_16px_0px_rgba(248,248,248,0.06)_inset] group",
        className
      )}
    >
      {children}
    </div>
  );
};

export const CardTitle = ({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) => {
  return (
    <h3
      className={cn(
        "text-lg font-semibold text-gray-800 dark:text-white py-2",
        className
      )}
    >
      {children}
    </h3>
  );
};

export const CardDescription = ({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) => {
  return (
    <p
      className={cn(
        "text-sm font-normal text-neutral-600 dark:text-neutral-400 max-w-sm",
        className
      )}
    >
      {children}
    </p>
  );
};

export const CardSkeletonContainer = ({
  className,
  children,
  showGradient = true,
}: {
  className?: string;
  children: React.ReactNode;
  showGradient?: boolean;
}) => {
  return (
    <div
      className={cn(
        "h-[15rem] md:h-[20rem] rounded-xl z-40",
        className,
        showGradient &&
          "bg-neutral-300 dark:bg-[rgba(40,40,40,0.70)] [mask-image:radial-gradient(50%_50%_at_50%_50%,white_0%,transparent_100%)]"
      )}
    >
      {children}
    </div>
  );
};

const Container = ({
  className,
  children,
}: {
  className?: string;
  children: React.ReactNode;
}) => {
  return (
    <div
      className={cn(
        `h-16 w-16 rounded-full flex items-center justify-center bg-[rgba(248,248,248,0.01)]
    shadow-[0px_0px_8px_0px_rgba(248,248,248,0.25)_inset,0px_32px_24px_-16px_rgba(0,0,0,0.40)]
    `,
        className
      )}
    >
      {children}
    </div>
  );
};

export const ClaudeLogo = ({ className }: { className?: string }) => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      shapeRendering="geometricPrecision"
      textRendering="geometricPrecision"
      imageRendering="optimizeQuality"
      fillRule="evenodd"
      clipRule="evenodd"
      viewBox="0 0 512 512"
      className={className}
    >
      <rect fill="#CC9B7A" width="512" height="512" rx="104.187" ry="105.042" />
      <path
        fill="#1F1F1E"
        fillRule="nonzero"
        d="M318.663 149.787h-43.368l78.952 212.423 43.368.004-78.952-212.427zm-125.326 0l-78.952 212.427h44.255l15.932-44.608 82.846-.004 16.107 44.612h44.255l-79.126-212.427h-45.317zm-4.251 128.341l26.91-74.701 27.083 74.701h-53.993z"
      />
    </svg>
  );
};

export const PythonLogo = ({ className }: { className?: string }) => {
  return (
    <img
      className={className}
      src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
      alt="Python Logo"
      width="28"
    />
  );
};

export const FastAPILogo = ({ className }: { className?: string }) => {
  return (
    <svg
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 16 16"
      className={className}
    >
      <image
        href="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg"
        height="16"
        width="16"
      />
    </svg>
  );
};

export const TensorFlow = ({ className }: { className?: string }) => {
  return (
    <svg
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 16 16"
      className={className}
    >
      <image
        href="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg"
        height="16"
        width="16"
      />
    </svg>
  );
};

export const Rust = ({ className }: { className?: string }) => {
  return (
    <svg
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 16 16"
      className={className}
    >
      <image
        href="https://www.svgrepo.com/show/374056/rust.svg"
        height="16"
        width="16"
      />
    </svg>
  );
};


export const RustAPI = ({ className }: { className?: string }) => {
    return (
      <svg
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 16 16"
        className={className}
      >
        <image
          href="https://uxwing.com/wp-content/themes/uxwing/download/web-app-development/rest-api-icon.png"
          height="16"
          width="16"
        />
      </svg>
    );
  };

export const RustTool = ({ className }: { className?: string }) => {
    return (
      <svg
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 16 16"
        className={className}
      >
        <image
          href="https://www.svgrepo.com/show/373787/light-rust-toolchain.svg"
          height="16"
          width="16"
        />
      </svg>
    );
  };

export const SkilitLearn = ({ className }: { className?: string }) => {
  return (
    <svg
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 16 16"
      className={className}
    >
      <image
        href="https://icon.icepanel.io/Technology/svg/scikit-learn.svg"
        height="16"
        width="16"
      />
    </svg>
  );
};

export const Numpy = ({ className }: { className?: string }) => {
  return (
    <svg
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 16 16"
      className={className}
    >
      <image
        href="https://cdn.worldvectorlogo.com/logos/numpy-1.svg"
        height="16"
        width="16"
      />
    </svg>
  );
};
