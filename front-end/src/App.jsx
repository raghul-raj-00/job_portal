import { useState } from 'react'
import './App.css'
import Registerpage from './Registerpage'
import Loginpage from './Loginpage'
import Joblist from './Joblist'
import Applyjob from './Applyjob'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
function App() {
  

  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Loginpage />} />
      <Route path='/login' element={<Loginpage/>}/>
      <Route path='/register' element={<Registerpage/>}/>
      <Route path='/joblist' element={<Joblist/>}/>
      <Route path='/applyjob/:jobId' element={<Applyjob/>}/>
    </Routes>
    </BrowserRouter>
  )
}

export default App
