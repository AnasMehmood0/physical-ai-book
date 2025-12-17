import React, { useEffect, useState } from 'react';

const ContextSelector = ({ onTextSelection }) => {
  const [selectedText, setSelectedText] = useState('');

  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      const text = selection.toString().trim();

      if (text && selection.anchorOffset !== selection.extentOffset) { // Ensure actual text is selected
        setSelectedText(text);
        onTextSelection(text);
      } else if (!text) {
        setSelectedText('');
        onTextSelection(null);
      }
    };

    document.addEventListener('mouseup', handleSelection); // Use mouseup to ensure selection is complete
    document.addEventListener('keyup', handleSelection); // For keyboard selections

    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('keyup', handleSelection);
    };
  }, [onTextSelection]);

  const clearSelection = () => {
    window.getSelection().removeAllRanges();
    setSelectedText('');
    onTextSelection(null);
  };

  // This component can be extended with visual indicators if needed
  // For now, it just manages the text selection state and passes it to the chat interface

  return (
    <div style={{ display: 'none' }}>
      {/* Hidden component that manages text selection state */}
    </div>
  );
};

export default ContextSelector;