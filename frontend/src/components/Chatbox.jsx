import { useState, useRef, useEffect } from "react";

const ChatBox = () => {
  const [question, setQuestion] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const askQuestion = async () => {
    if (!question.trim()) return;
    const userMessage = { role: "user", message: question };
    setChat((prev) => [...prev, userMessage]);
    setQuestion("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      const assistantMessage = { role: "assistant", message: data.answer };
      setChat((prev) => [...prev, assistantMessage]);
    } catch {
      setChat((prev) => [
        ...prev,
        {
          role: "assistant",
          message: "⚠️ An error occurred. Please try again later.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat, loading]);

  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-br from-white to-yellow-50 font-sans">
      {/* Header */}
      <div className="bg-amber-100 py-4 shadow-md border-b text-center">
        <h1 className="text-2xl font-bold text-amber-800 tracking-wide">
          📿 Vachanamrut AI — Spiritual Chat Assistant
        </h1>
        <p className="text-sm text-amber-700">Seek. Ask. Understand. Grow.</p>
      </div>

      {/* Messages */}
      <div className="flex-1 max-w-3xl mx-auto w-full px-4 py-6 space-y-4 overflow-y-auto">
        {chat.map((entry, i) => (
          <div
            key={i}
            className={`p-4 rounded-xl shadow-md whitespace-pre-wrap ${
              entry.role === "user"
                ? "bg-white border border-gray-200 text-gray-900"
                : "bg-emerald-50 border border-emerald-200 text-emerald-900 font-serif"
            }`}
          >
            <p className="text-xs font-semibold mb-1">
              {entry.role === "user" ? "🧑 You" : "📖 Vachanamrut AI"}
            </p>
            <p>{entry.message}</p>
          </div>
        ))}

        {loading && (
          <div className="bg-yellow-100 text-yellow-900 p-4 rounded-xl shadow-sm">
            🙏 Preparing spiritual guidance...
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="bg-white border-t px-4 py-4 sticky bottom-0 shadow-sm">
        <div className="flex gap-2 max-w-3xl mx-auto">
          <textarea
            rows="2"
            className="flex-1 p-3 border border-gray-300 rounded-md resize-none focus:outline-none focus:ring-2 focus:ring-amber-400"
            placeholder="Ask your spiritual question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button
            onClick={askQuestion}
            disabled={loading}
            className="bg-amber-600 hover:bg-amber-700 text-white px-4 py-2 rounded-md transition disabled:opacity-50"
          >
            Ask
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatBox;
