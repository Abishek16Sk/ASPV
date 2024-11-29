import React, { useState, useEffect } from "react";
import axios from "axios";

const ProductCategories = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true); 
  useEffect(() => {
    
    axios.get("http://127.0.0.1:5000/api/products")
      .then(response => {
        setProducts(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error("Error fetching products:", error);
        setLoading(false);
        alert("Error loading products.");
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;  
  }

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: "20px",
        padding: "20px",
        backgroundColor: "#f9f9f9",
      }}
    >
      {products.map((product, index) => (
        <div
          key={index}
          style={{
            border: "1px solid #ddd",
            padding: "15px",
            borderRadius: "8px",
            textAlign: "center",
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
            backgroundColor: "#fff",
          }}
        >
          <img
            src={product.image_url || "/path/to/default-image.jpg"}  
            alt={product.name}
            style={{
              width: "200px",
              height: "300px",
              objectFit: "cover",
              borderRadius: "5px",
              marginBottom: "8px",
            }}
          />
          <h3 style={{ marginBottom: "5px", fontSize: "1.2rem" }}>{product.name}</h3>
          <p style={{ fontStyle: "italic", color: "#888", marginBottom: "5px" }}>
            {product.category}
          </p>
          <p style={{ marginBottom: "10px", color: "#555" }}>{product.description}</p>
          <p style={{ fontWeight: "bold", color: "#333", fontSize: "1.1rem" }}>
            ₹{product.price}
          </p>
          <button
            style={{
              marginTop: "10px",
              padding: "10px 20px",
              backgroundColor: "#28a745",
              color: "#fff",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer",
              fontSize: "1rem",
              fontWeight: "bold",
              transition: "background-color 0.3s ease",
            }}
            onMouseOver={(e) => (e.target.style.backgroundColor = "#218838")}
            onMouseOut={(e) => (e.target.style.backgroundColor = "#28a745")}
            onClick={() => alert(`You clicked Buy on ${product.name}`)}
          >
            Buy
          </button>
        </div>
      ))}
    </div>
  );
};

export default ProductCategories;
