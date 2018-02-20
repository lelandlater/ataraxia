import React, { Component } from 'react'
import Header from './components/Header.js'
import Masthead from './components/Masthead.js'
import Main from './components/Main.js'
import Footer from './components/Footer.js'

const ATARAXIA = '\u03AC\u03C4\u03B1\u03C1\u03B1\u03BE\u03AF\u03B1'

class App extends Component {
  
  //state = {
  //  items: contents,
  //  quote: null
  //}

  //toggler = _id => {
  //  this.setState({
  //    content: _id
  //  })
  //}

  render() {
    let content
    content = (
      <Masthead>
        { ATARAXIA }
      </Masthead>
    )
    return (
      <div>
        <Header />
        <Main>
          { content }
        </Main>
        <Footer />
      </div>
    )
  }
}
        //<Main items={ this.state.items } 
        //  toggler={ index => this.toggler(index) } 
        //  which={ this.state.content } />

//const Main = ({ items, toggler, which }) => 
//  <ul>
//    {
//      items.map((content, index) =>
//        <li onClick={ e => toggler(index) }
//         key={ index }>
//          <button style={ which === index ? { fontWeight: 'bold' } : null }>
//            { content }
//          </button>
//        </li>)
//    }
//  </ul>
//
//const Header = ({ styling, text }) =>
//  <header>
//    <h1 style={ styling }>
//    { text }
//  </h1>
//</header>

export default App
