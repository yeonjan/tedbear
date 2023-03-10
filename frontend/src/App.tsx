import React from 'react';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomePage from 'pages/HomePage'
import LandingPage from 'pages/LandingPage'
import GamePage from 'pages/GamePage'
import CollectionPage from 'pages/CollectionPage'
import ProfilePage from 'pages/ProfilePage'
import LayoutPage from 'pages/LayoutPage'
import TestPage from 'pages/TestPage'
import GlobalStyle from 'GlobalStyle';



function App() {
  return (
    <div className="App">
      <GlobalStyle />
      <BrowserRouter>
        <Routes>
          <Route element={<LayoutPage/>}>
            <Route path="/home" element={<HomePage />} />
            <Route path="/" element={<LandingPage />} />
            <Route path="/game" element={<GamePage />} />
            <Route path="/collection" element={<CollectionPage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="/test" element={<TestPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
