import React, {useState, useEffect} from 'react';
import './App.css';
import Nav from './components/Nav';
import PositionMap from './components/PositionMap';
import SearchForm from './components/SearchForm';
import Stations  from './components/Stations';
import axios from 'axios';

function App() {
  const [stationGraph, setStationGraph] = useState([]);
  const [stations, setStations] = useState([]);
  const [isInDatabase, setIsInDatabase] =useState(true);


  useEffect(() => {
    axios.get(`/stations`)
    .then((res) => {
      setStations(res.data)
    })
  },[])

  const onClickStation = (data)=>{
      setStationGraph([data])
  }

    const getSerchResult = (e) => {
      e.preventDefault();
      const result = e.target.elements.search.value;
        axios.get(`/cities-stations/${result}`)
        .then((res) => {
          setStations(res.data);
          setIsInDatabase(true);
        }).catch(handleErrors);
    }

    const handleErrors = (err) =>{
      if (err.response){
        setIsInDatabase(false);
        console.log('response error')
      }else if(err.request){
        console.log('request error')
      } else {
        console.log('error')
      }
    };

  return (
    <div>
        <Nav />
      <div className='app'>
        <PositionMap stations = {stations}  onClickStation={onClickStation} />
        <div className='data-wraper'>
          <SearchForm getSerchResult = {getSerchResult} valid={isInDatabase} />
          <Stations station = {stationGraph} / >
        </div>
      </div>
    </div>

  );
}
export default App;
