import React, {Component} from 'react';
import '../App.css';
import Logo from '../Icons/icons8-sakura-96.png';

class Nav extends Component {

  render(){
  return (

    <nav>
    <img src={Logo}  alt="logo" />
    <a href="/">
    Clean Air
    </a>
    </nav>
  );
}
}
export default Nav;
