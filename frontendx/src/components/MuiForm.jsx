import { useState } from 'react';
import { TextField } from '@mui/material';
import { useForm } from 'react-hook-form';
import httpClient from '../infra/httpClient';

const MuiForm = () => {
    const [name , setName] = useState();
    const [x , setX] = useState();
    const [resultData , setResultData] = useState();    
  const { register, handleSubmit, reset, watch } = useForm();

  const currentX = watch('x');

  const onSubmit = async (data) => {
    /*
    const headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*'
    };
    const url = `/api3/predict?x=${data.x}`
    httpClient
        .get(url, { headers })
        .then((response) => {
            const y_pred = response.data
            console.log('y_pred: ', y_pred)
            setResultData(y_pred)
        })
        .catch((error) => {
            const msg = "Error getting data" + error
            console.error(msg)
        });
    */
    console.log("data.x: " + data.x);      
    reset();
  };

  /*
      <div>
        {currentX && <div>param1: {currentX}</div>}          
        {resultData && <div>result: {resultData}</div>}
      </div>
  */
  return (
      <form onSubmit={handleSubmit(onSubmit)}>
        <TextField inputRef={register} id="x" name="x" helperText="Enter x value" />
      </form>
  );
};

export default MuiForm;