import React, { Component } from 'react';

import '../App.css';



class SearchForm extends Component{
  constructor(props) {
    super(props);
    this.state = {value: ''};
    this.handlerCityChange = this.handlerCityChange.bind(this);
  }

     handlerCityChange = (event) => {
      this.setState({value: event.target.value})
    }

    get notFaundError() {
  if (this.props.valid) return  <p className='validation'></p>;
  return <p className='validation'>Entered name not exist or you do not enter any name, try enter other name</p>;
}
    render(){

    return (
      <div className='form-wraper'>
      <form onSubmit={this.props.getSerchResult} className='search-form' >
        <input className={this.props.valid ? '' : 'search-field'} value={this.state.value} name='search' placeholder='Search' type='text' onChange={this.handlerCityChange} />
        <button type='submit'>Search</button>
      </form>

    {this.notFaundError}

      </div>
    )
  }
}

export default SearchForm;
