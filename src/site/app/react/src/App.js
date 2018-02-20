import React, { Component } from 'react'
import Header from './components/Header.js'
import Masthead from './components/Masthead.js'
import Main from './components/Main.js'
import Nav from './components/Nav.js'
import Footer from './components/Footer.js'
import ContactNav from './components/ContactNav.js'

const ATARAXIA = '\u03AC\u03C4\u03B1\u03C1\u03B1\u03BE\u03AF\u03B1'

class App extends Component {
  
  render() {
    return (
      <div>
        <Header />
        <Main>
          <Masthead>
            { ATARAXIA }
          </Masthead>
          <Nav />
        </Main>
        <Footer>
          <ContactNav />
        </Footer>
      </div>
    )
  }
}

export default App