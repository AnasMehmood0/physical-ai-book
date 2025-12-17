import React, { useState, useRef, useEffect } from 'react';
import './ChatInterface.css';

const ChatInterface = ({ selectedText = null }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      text: inputValue,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    setError(null);

    try {
      // Prepare the request based on whether there's selected text
      let requestData;
      if (selectedText) {
        // Use the context chat endpoint when selected text is available
        requestData = {
          message: inputValue,
          selected_context: selectedText
        };

        const response = await fetch('/api/chat/context', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestData)
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        const botMessage = {
          id: Date.now() + 1,
          text: data.response,
          sender: 'bot',
          sources: data.sources || [],
          timestamp: new Date()
        };

        setMessages(prev => [...prev, botMessage]);
      } else {
        // Use the regular chat endpoint when no selected text
        requestData = {
          message: inputValue,
          selected_text: selectedText || undefined
        };

        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestData)
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        const botMessage = {
          id: Date.now() + 1,
          text: data.response,
          sender: 'bot',
          sources: data.sources || [],
          timestamp: new Date()
        };

        setMessages(prev => [...prev, botMessage]);
      }
    } catch (err) {
      setError('Failed to send message. Please try again.');
      console.error('Chat error:', err);

      const errorMessage = {
        id: Date.now() + 1,
        text: 'Sorry, I encountered an error processing your request. Please try again.',
        sender: 'bot',
        error: true,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const clearChat = () => {
    setMessages([]);
    setError(null);
  };

  return (
    <>
      {/* Chat Widget Button */}
      <button
        className="chat-widget-button"
        onClick={toggleChat}
        aria-label={isOpen ? 'Close chat' : 'Open chat'}
      >
        <div className="chat-icon">💬</div>
        {error && <div className="error-indicator" title="Error occurred"></div>}
      </button>

      {/* Chat Widget Panel */}
      {isOpen && (
        <div className="chat-widget-panel">
          <div className="chat-header">
            <div className="chat-title">Physical AI Book Assistant</div>
            <div className="chat-controls">
              <button
                className="clear-chat-button"
                onClick={clearChat}
                title="Clear chat"
              >
                🗑️
              </button>
              <button
                className="close-chat-button"
                onClick={toggleChat}
                title="Close chat"
              >
                ✕
              </button>
            </div>
          </div>

          <div className="chat-messages">
            {messages.length === 0 ? (
              <div className="chat-welcome">
                <p>Hello! I'm your Physical AI Book assistant.</p>
                <p>Ask me anything about the book content:</p>
                <ul>
                  <li>What is Physical AI?</li>
                  <li>Explain computer vision in robotics</li>
                  <li>How do sensors work in embodied intelligence?</li>
                </ul>
                {selectedText && (
                  <div className="selected-context-notice">
                    <strong>Context:</strong> I'm focusing on the text you selected.
                  </div>
                )}
              </div>
            ) : (
              messages.map((message) => (
                <div
                  key={message.id}
                  className={`chat-message ${message.sender}-message`}
                >
                  <div className="message-content">
                    {message.text}
                  </div>
                  {message.sources && message.sources.length > 0 && (
                    <div className="message-sources">
                      <details>
                        <summary>Sources ({message.sources.length})</summary>
                        <ul>
                          {message.sources.map((source, index) => (
                            <li key={index}>{source}</li>
                          ))}
                        </ul>
                      </details>
                    </div>
                  )}
                  {message.error && (
                    <div className="error-message">
                      Error: {message.text}
                    </div>
                  )}
                </div>
              ))
            )}
            {isLoading && (
              <div className="chat-message bot-message">
                <div className="message-content">
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="chat-input-area">
            {selectedText && (
              <div className="selected-text-preview">
                <small>Context: "{selectedText.substring(0, 60)}..."</small>
              </div>
            )}
            <textarea
              ref={textareaRef}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask a question about the book..."
              disabled={isLoading}
              rows="1"
            />
            <button
              onClick={sendMessage}
              disabled={isLoading || !inputValue.trim()}
              className="send-button"
            >
              {isLoading ? 'Sending...' : 'Send'}
            </button>
          </div>

          {error && (
            <div className="error-notification">
              {error}
            </div>
          )}
        </div>
      )}
    </>
  );
};

export default ChatInterface;