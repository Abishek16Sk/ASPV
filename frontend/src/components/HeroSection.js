import React, { useState, useEffect } from "react";
import axios from "axios";

const HeroSection = () => {
  const [products, setProducts] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
   
    axios
      .get("http://127.0.0.1:5000/api/products")
      .then((response) => setProducts(response.data))
      .catch((error) => console.error("Error fetching products:", error));

    // Set up the automatic sliding
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % products.length);
    }, 3000);
    
    return () => clearInterval(interval);
  }, [products.length]);

  return (
    <div style={{ position: "relative", width: "100%", height: "auto", overflow: "hidden" }}>
      <div
        style={{
          display: "flex",
          transition: "transform 0.5s ease", 
          transform: `translateX(-${currentIndex * 100}vw)`, 
        }}
      >
        {products.length > 0 &&
          products.map((product, index) => (
            <div
              key={index}
              style={{
                minWidth: "100vw", 
                height: "25vw", 
                backgroundColor: "#f9f9f9",
                overflow: "hidden",
                boxSizing: "border-box",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <img
                src={product.image_url}
                alt={product.name}
                style={{
                  width: "100%",
                  height: "100%", 
                  objectFit: "cover", 
                }}
              />
              <div
                style={{
                  position: "absolute",
                  bottom: "10px",
                  left: "10px",
                  color: "#fff",
                  fontWeight: "bold",
                  fontSize: "1.5rem",
                  backgroundColor: "rgba(0, 0, 0, 0.5)",
                  padding: "10px",
                  borderRadius: "5px",
                }}
              >
                {product.name} - ₹{product.price}
              </div>
            </div>
          ))}
      </div>
    </div>
  );
};

export default HeroSection;
