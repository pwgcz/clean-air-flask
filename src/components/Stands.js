import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { MeasuringData } from './MeasuringData';



export const Stands = ({station}) =>{

const [stands, setStands] = useState([])
let standsList = []

useEffect(() => {
  axios.get(`/measuring-stands/${station.id}`)
  .then((res) => {
    setStands(res.data);
  }).catch(handleErrors)
},[station.id]);

const handleErrors = (err) =>{
  if (err.response){
    console.log('response error')
  }else if(err.request){
    console.log('request error')
  } else {
    console.log('unexpectec error')
  }
};

   standsList = stands.map(sta => {
    return (
      <div key={sta.id} >
      <h4>{sta.name} ({sta.code})</h4>

      <div className='stand-card'>
        <MeasuringData stand={sta}/>
        </div>
      </div>
    )
  })



  return(
    <div>
  {standsList}
  </div>
  )
}
