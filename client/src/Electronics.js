import React, { useState, useEffect } from "react";
import "./Electronics.css";
import Product from "./Product";
// import Electronics from './Electronics'
function Electronics({ title }) {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/electronics_list")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        setIsLoading(false);
        console.log(data);
      });
  }, []);

  useEffect(() => {
    console.log("after clearing");

    return () => {
      console.log("clearing...");
    };
  }, []);

  var counter = 0,
    pre_score = -1,
    flag = 0;
  return (
    <div className="electronics">
      <div className="electronics-title">{title}</div>
      <div className="electronics-content">
        {isLoading ? (
          <div>Loading</div>
        ) : (
          data.map((dat) => {
            // console.log(dat)
            var url = dat.IMAGE_URL;
            if (dat.Trend_score > pre_score) {
              pre_score = dat.Trend_score;
              flag = 1;
              console.log(counter);
            }
            if (dat.IMAGE_URL === "null") {
              url = dat.product_image_link;
            }
            return (
              <Product
                key={dat.id}
                desc={dat.product_title}
                rank={(counter = counter + flag)}
                image={url}
                flipkart_link={dat.Flipkart_url}
                brand={dat.Brand}
                sub_category={dat.Sub_Category}
                score={dat.Trend_score}
              />
            );
          })
        )}
      </div>
    </div>
  );
}

export default Electronics;
