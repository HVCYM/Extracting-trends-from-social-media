import React from 'react'
import './App.css'
import Header from './Header'
import Footer from './Footer'
import Home from './Home'
import Fashion from './Fashion'
import Mobile from './Mobile'
import Electronics from './Electronics'
import About from './About'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
function App() {
  return (
    <Router>
      <Routes>
      <Route path='/' element={<> <Header/> <Home/> <Footer/> </>} />
      <Route path='/fashion' element={<><Header/><Fashion title='Fashion'/><Footer/></>}/>
      <Route path='/phones' element={<><Header/><Mobile title='SmartPhones'/><Footer/></>}/>
      <Route path='/electronics' element={<><Header/><Electronics title='Electronics'/><Footer/></>}/>
      <Route path='/about' element={<><Header/><About/><Footer/></>}/>
      </Routes>
    </Router>
  )
}

export default App
