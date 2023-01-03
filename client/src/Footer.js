import React from 'react'
import './Footer.css'
function Footer() {
  return (
    <div className='footer'>
      <a href='#top'>
      <div  className='back-to-top'>
        <p>Back to top</p>
      </div>
      </a>
      <div className='footer-info'>
        <div className='footer-info-div1'>
          <span>
            <p className='footer-info-div1-line1'>Connect with Us</p>
            <a href='https://www.facebook.com' target='blank'><p className='footer-info-div1-lines'>Facebook</p></a>
            <a href='https://www.instagram.com' target='blank'><p className='footer-info-div1-lines'>Instagram</p></a>
            <a href='https://www.twitter.com' target='blank'><p className='footer-info-div1-lines'>Twitter</p></a>
          </span>
          <span>
            <p className='footer-info-div1-line1'>Contact Us</p>
            <a><p className='footer-info-div1-lines'>Email:query@iconic.com</p></a>
            <a><p className='footer-info-div1-lines'>Phone:9988776655</p></a>
          </span>
        </div>
        <div className='footer-info-div2'>
            <a>
              <p className='more-info'>Conditions of Use & Sale</p>
            </a>
            <a>
              <p className='more-info'>Privacy Notice</p>
            </a>
            <a>
              <p className='more-info'>© 2022, Iconic.com</p>
            </a>
        </div>
      </div>
    </div>
  )
}

export default Footer
