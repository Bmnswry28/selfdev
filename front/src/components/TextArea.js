import React from 'react';
import './TextArea.css';

const TextArea = ({ placeholder, rows = 3, value, onChange }) => {
  return (
    <textarea
      placeholder={placeholder}
      rows={rows}
      value={value}
      onChange={onChange}
    />
  );
};

export default TextArea;
