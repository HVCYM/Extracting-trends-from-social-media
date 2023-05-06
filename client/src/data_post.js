import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./data_post.css";

function Data() {
  const [category, setCategory] = useState("");
  const [url, setUrl] = useState("");
  const [tweet, setTweet] = useState("");
  const [score, setScore] = useState(0);
  const [image, setImage] = useState(null);
  const [video, setVideo] = useState(null);
  const [id, setId] = useState(0);
  const [brand, setBrand] = useState("");
  const [sub, setSub] = useState("");
  const [furl, setFurl] = useState(null);
  const [pimage, setPimage] = useState(null);
  const [product, setProduct] = useState("");

  //   const history = useHistory();
  const navigate = useNavigate();

  const Add_data = async (e) => {
    e.preventDefault();
    let formField = new FormData();
    formField.append("category", category);
    formField.append("url", url);
    formField.append("tweet", tweet);
    formField.append("score", score);
    formField.append("image", image);
    formField.append("video", video);
    formField.append("item_id", id);
    formField.append("brand", brand);
    formField.append("sub", sub);
    formField.append("flipkart_url", furl);
    formField.append("product_image", pimage);
    formField.append("product_title", product);
    await axios({
      method: "post",
      url: "http://127.0.0.1:8000/tasklist",
      data: formField,
    })
      .then((response) => {
        console.log(response.data);
        navigate("/");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const [hashid, setHashid] = useState();
  const [hash, setHash] = useState("");
  const Add_hashtag = async (e) => {
    e.preventDefault();
    let formField = new FormData();
    formField.append("item_id", hashid);
    formField.append("hashtag", hash);
    await axios({
      method: "post",
      url: "http://127.0.0.1:8000/tasklist",
      data: formField,
    })
      .then((response) => {
        console.log(response.data);
        navigate("/");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const [file, setFile] = useState();
  const file_data = async (e) => {
    e.preventDefault();
    let formField = new FormData();
    formField.append("file", file);
    await axios({
      method: "post",
      url: "http://127.0.0.1:8000/tasklist",
      data: formField,
    })
      .then((response) => {
        console.log(response.data);
        navigate("/");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="data-post">
      <div className="upload-file">
        <h1 className="title-label">Upload file</h1>
        <form onSubmit={file_data}>
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
          ></input>
          <button className="flipkart-button" type="submit">
            Submit
          </button>
        </form>
      </div>
      <div className="main-section">
        <h1 className="title-label">Product Details</h1>
        <form onSubmit={Add_data}>
          <label>category: </label>
          <input
            type="text"
            placeholder="category"
            onChange={(e) => setCategory(e.target.value)}
          ></input>
          <label>url: </label>
          <input
            type="text"
            placeholder="url"
            onChange={(e) => setUrl(e.target.value)}
          ></input>
          <label>Tweet_Text: </label>
          <input
            type="text"
            placeholder="tweet text"
            onChange={(e) => setTweet(e.target.value)}
          ></input>
          <label>Trend_score: </label>
          <input
            type="number"
            step="0.01"
            placeholder="trending score"
            onChange={(e) => setScore(e.target.value)}
          ></input>
          <label>IMAGE_URL: </label>
          <input
            type="text"
            placeholder="image url"
            onChange={(e) => setImage(e.target.value)}
          ></input>
          <label>video_url: </label>
          <input
            type="text"
            placeholder="video url"
            onChange={(e) => setVideo(e.target.value)}
          ></input>
          <label>item_id: </label>
          <input
            type="number"
            placeholder="item id"
            onChange={(e) => setId(e.target.value)}
          ></input>
          <label>brand: </label>
          <input
            type="text"
            placeholder="brand"
            onChange={(e) => setBrand(e.target.value)}
          ></input>
          <label>sub category: </label>
          <input
            type="text"
            placeholder="sub category"
            onChange={(e) => setSub(e.target.value)}
          ></input>
          <label>Flipkart_url: </label>
          <input
            type="text"
            placeholder="flipkart url"
            onChange={(e) => setFurl(e.target.value)}
          ></input>
          <label>product_image_link: </label>
          <input
            type="text"
            placeholder="product image link"
            onChange={(e) => setPimage(e.target.value)}
          ></input>
          <label>product_title: </label>
          <input
            type="text"
            placeholder="protuct title"
            onChange={(e) => setProduct(e.target.value)}
          ></input>
          <button className="flipkart-button" type="submit">
            Submit
          </button>
        </form>
      </div>
      <div className="add-hashtag">
        <form onSubmit={Add_hashtag}>
          <label>item id: </label>
          <input
            type="number"
            placeholder="item id"
            onChange={(e) => setHashid(e.target.value)}
          ></input>
          <label>hash tag: </label>
          <input
            type="text"
            placeholder="hashtag"
            onChange={(e) => setHash(e.target.value)}
          ></input>
          <button className="flipkart-button" type="submit">
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}

export default Data;
