import React, { useEffect } from "react";
import "./Header.css";
import HomeSharpIcon from "@mui/icons-material/HomeSharp";
import SearchIcon from "@mui/icons-material/Search";
import InputIcon from "@mui/icons-material/Input";
// import React, { useState, useEffect } from "react";

function Header() {
  // useEffect(() => {
  //   fetch("http://127.0.0.1:8000/home");
  // }, []);
  return (
    <div className="header">
      <a href="/">
        <HomeSharpIcon className="home-icon" />
      </a>
      <div className="header-search">
        <a href="/fashion">
          <div className="header-category">Fashion</div>
        </a>
        <a href="/phones">
          <div className="header-category">Phones</div>
        </a>
        <a href="/electronics">
          <div className="header-category">Electronics</div>
        </a>
        <form>
          <div className="header-category">
            <button>Update</button>
          </div>
        </form>
      </div>

      <a href="/about">
        <div className="header-login">
          <p>About Us</p>
        </div>
      </a>
    </div>
  );
}

export default Header;
