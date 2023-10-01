import React from 'react';
import Header from './components/header';
import Navbar from './components/navbar';
import Hero from './components/hero';
import Login from './components/login';

const MainPage: React.FC = () => {
  return (
    <div>
      <Navbar />
      <Hero />
      <Header />
      
     
     
      {/* Your main content goes here */}
    </div>
  );
};

export default MainPage;
