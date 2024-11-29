import React from "react";

const Header = () => (
  <header style={{ padding: "20px", backgroundColor: "#007BFF", color: "#fff" }}>
     <h1 style={{ textAlign: "center", marginBottom: "20px" }}>ASPV International Production</h1>
    <nav>
      <a href="Products" style={{ margin: "0 10px", color: "#fff" }}>Products</a>
      <a href="contact" style={{ margin: "0 10px", color: "#fff" }}>Contact</a>
    </nav>
  </header>
);

export default Header;
