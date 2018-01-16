import React, { Component } from 'react'

const headerStyle = {
  textAlign: 'center',
  backgroundColor: 'hotpink'
}

const quotes = [
  "This is an item",
  "This is another item",
  "As expected"
]
const ATARAXIA = '&#x3AC;&#x3C4;&#x3B1;&#x3C1;&#x3B1;&#x3BE;&#x3AF;&#x3B1;'
class App extends Component {
  
  state = {
    items: quotes,
    quote: null
  }

  toggler = _id => {
    this.setState({
      quote: _id
    })
  }

  render() {
    return (
      <div>
        <Header
          styling={ headerStyle }
          text={ ATARAXIA } />
        <Main items={ this.state.items } 
          toggler={ index => this.toggler(index) } 
          which={ this.state.quote } />
      </div>
    )
  }
}

const Main = ({ items, toggler, which }) => 
  <ul>
    {
      items.map((quote, index) =>
        <li onClick={ e => toggler(index) }
         key={ index }>
          <button style={ which == index ? { fontWeight: 'bold' } : null }>
            { quote }
          </button>
        </li>)
    }
  </ul>

const Header = ({ styling, text }) =>
  <header>
    <h1 style={ styling }>
    { text }
  </h1>
</header>

export default App
