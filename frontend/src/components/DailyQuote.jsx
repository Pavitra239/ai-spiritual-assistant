import { useEffect, useState } from "react";

const DailyQuote = () => {
  const [quote, setQuote] = useState(null);

  useEffect(() => {
    fetch("/vachanamrut.json")
      .then((res) => res.json())
      .then((data) => {
        const random = data[Math.floor(Math.random() * data.length)];
        setQuote(random);
      });
  }, []);

  if (!quote) return null;

  return (
    <div className="bg-yellow-100 border-b border-yellow-300 text-yellow-900 px-6 py-4 text-sm shadow">
      <p className="italic font-serif">“{quote.text.slice(0, 250)}...”</p>
      <p className="text-right text-xs font-semibold mt-1">
        📖 {quote.title} — {quote.location}
      </p>
    </div>
  );
};

export default DailyQuote;
