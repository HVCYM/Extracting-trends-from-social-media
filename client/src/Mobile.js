import React, { useState, useEffect } from "react";
import "./Mobile.css";
import Product from "./Product";
function Mobile({ title }) {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/phones_list")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        setIsLoading(false);
        console.log(data);
      });
  }, []);
  var counter = 0,
    pre_score = -1,
    flag = 0;
  return (
    <div className="mobile">
      <div className="mobile-title">{title}</div>
      <div className="mobile-content">
        {isLoading ? (
          <div>Loading</div>
        ) : (
          data.map((dat) => {
            // console.log(dat)
            if (dat.Trend_score > pre_score) {
              pre_score = dat.Trend_score;
              flag = 1;
              console.log(counter);
            }
            var url = dat.IMAGE_URL;
            // console.log(url)
            if (dat.IMAGE_URL == "null") {
              url = dat.product_image_link;
            }
            return (
              <Product
                key={dat.id}
                desc={dat.product_title}
                rank={(counter = counter + 1)}
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

export default Mobile;
