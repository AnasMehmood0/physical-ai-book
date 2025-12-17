import React, { useState, useEffect } from 'react';
import Layout from '@theme-original/Layout';
import ChatInterface from '@site/src/components/ChatBot/ChatInterface';
import ContextSelector from '@site/src/components/ChatBot/ContextSelector';

export default function LayoutWrapper(props) {
  const [selectedText, setSelectedText] = useState(null);

  const handleTextSelection = (text) => {
    setSelectedText(text);
  };

  return (
    <>
      <Layout {...props} />
      <ContextSelector onTextSelection={handleTextSelection} />
      <ChatInterface selectedText={selectedText} />
    </>
  );
}