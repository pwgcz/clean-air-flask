import React, { Component } from 'react';
import { Stands } from './Stands';



class Stations extends Component{


  get graphs(){
    if(this.props.station.length === 0){
      return(
    <div className="additional-info">
      <h1>
      <h1>Tips:</h1>
      <q>Enter a name of citty or district in search field to focous map on this area</q>
      <q>Click on leaf marker on map to see graphs</q>
      </h1>
    </div>
    )
    }else {
      return(
    <div className='station-wraper'>
      {this.props.station.map(sta => {
        return (
          <div key={sta.id} className='station-card'>
          <h1>{sta.name}</h1>
          <Stands station={sta}/>
          </div>
        )
      })}
    </div>
    )
    }
  }

  render(){

  return this.graphs
}
}
export default Stations;
