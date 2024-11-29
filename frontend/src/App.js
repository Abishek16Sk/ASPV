import React from "react";
import Header from "./components/Header";
import HeroSection from "./components/HeroSection";
import ProductCategories from "./components/ProductCategories";
import Footer from "./components/Footer";
import './styles.css'
const App = () => {
  return (
    <>
      <Header />
      <HeroSection />
      <ProductCategories />
      <Footer />
    </>
  );
};

export default App;
