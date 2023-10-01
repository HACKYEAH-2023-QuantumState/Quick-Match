import React from 'react';

interface ColorButtonProps {
  onClick: () => void;
}

const ColorButton: React.FC<ColorButtonProps> = ({ onClick }) => {
  return (
    <button
      onClick={onClick}
      style={{
        backgroundColor: '#ff4694',
        color: '#776fff',
        padding: '10px 20px',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
      }}
    >
      Click Me
    </button>
  );
};

export default ColorButton;
