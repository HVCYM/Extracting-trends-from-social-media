import React from 'react'
import './Product.css'
import { useNavigate } from "react-router-dom";
function Product({desc,rank,image,sub_category,brand,score,flipkart_link}) {
  
  return (
    <div className='product'>
        <p className='product-category'>{sub_category}</p>
        <div className='product-div1'>
          <div    className='product-image-div'>
            <img className='product-image'  src={image}/>
          </div>
          <div className='product-details'>
            <p className='product-desc'>{desc.slice(0,50)}...</p>
            
            <p><b>Brand: </b>{brand}</p>
            <p className='product-rank'><h1>#{rank}</h1>(Score:{parseInt(score)})</p>
          </div>
          </div>
        <div className='product-div2'>
          <button className='flipkart-button' onClick={()=>window.open(flipkart_link, '_blank')}>Go to flipkart</button>
        </div>
        
    </div>
  )
}

export default Product
