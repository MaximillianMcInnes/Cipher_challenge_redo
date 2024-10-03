interface DecodedTextProps {
    text: string | null;  // or `text?: string` if you want it to be optional
  }
  
  const Decoded_text: React.FC<DecodedTextProps> = ({ text }) => {
    return (
      <div className="text-white mt-4">
        {text && <p>Output: {text}</p>}
      </div>
    );
  };
  
  export default Decoded_text;
  