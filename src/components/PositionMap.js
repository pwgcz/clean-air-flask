import React, { Component } from 'react';
import '../App.css';
import { Map, Marker, Popup, TileLayer, Tooltip } from 'react-leaflet';
import { Icon, latLngBounds } from 'leaflet';



class PositionMap extends Component {
  constructor(props){
    super(props);
    this.leafPoint = new Icon({
      iconUrl: 'icons8-fallen-leaf-48.png',
      iconSize: [30, 30]
    });

  }

  handleClick = (e) => {
    this.props.onClickStation(e);
 }

  render(){
     return(
      <div className='map-wraper'>
     <Map  bounds={ this.props.stations.length === 0 ? latLngBounds([[54.754139, 23.642153], [49.293564, 14.382222]]) : latLngBounds(this.props.stations.map(sta => [sta.gegrLat, sta.gegrLon])) } >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
        />
        {this.props.stations.map(sta => {
        return (
          <Marker key={sta.id} position={[sta.gegrLat, sta.gegrLon]} icon={this.leafPoint} onClick={this.handleClick.bind(this, sta)}>
            <Popup>{sta.name}</Popup>
            <Tooltip>
              {sta.name}
            </Tooltip>
          </Marker>
        )
      })}
      </Map>
      </div>
  )}
}
export default PositionMap;
