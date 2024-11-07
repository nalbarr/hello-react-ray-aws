import React, { useState } from "react";
import httpClient from '../infra/httpClient';

const SimpleForm = () => {
    const [formData , setFormData] = useState({
        param1: '',
        param2: ''
    });
    const [resultData , setResultData] = useState('');

    /*
    NOTE:
    - MP.  Why do we not need this?
    useEffect(() => {
    }, []);
    */
        
    /*
    NOTE:
    - MP. Consider below later.  Ignore uncontrolled input browser warnings for now.
    - https://dev.to/stanleyjovel/simplify-controlled-components-with-react-hooks-23nn
    */
    const handleFormInput = (e) => {
        setFormData({[e.target.name]: e.target.value})
    }

    const handleResponse = (e) => {
        // NA.
        // - No op. Just so the browser does not complain    
    }    
    
    const handleDebugSubmit = () => {
        alert(formData.param1)
    }

    const handleSubmit = () => {
        // NA.
        // NOTE:
        // - MP. Connect bridge here.
        // - MP. Debug and extend this on your own.
        const headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Access-Control-Allow-Origin': '*'
        };
        // NA.
        // NOTE:
        // - MP. api3 will take param1 and return JSON.
        // - MP. below back ticks are for literal template strings.
        const url = `/api3/predict?x=${formData.param1}`
        httpClient
            .get(url, { headers })       
            .then((response) => {
                const y_pred = response.data
                console.log('y_pred: ', y_pred)
                setResultData(y_pred)
                /*
                NOTE:
                - MP. if you were to map against list.
                let ys = ys.map(x => x["id"])
                if (ys != null) {
                    console.log('ys: ', ys)
                }
                setResultData(ys)
                */
            })
            .catch((error) => {
                const msg = "Error getting data" + error
                console.error(msg)
            }); 
    }

	// NA. Remove uncontrolled form warnings.
	// https://thewebdev.info/2021/09/18/how-to-fix-the-a-component-is-changing-an-uncontrolled-input-of-type-text-to-be-controlled-error-in-react/
    return (
       <div>
	       <p>
		       Simple Form
		</p>
            <input 
            type="text" 
            name="param1" 
            onChange={handleFormInput} 
            placeholder="Parameter1" 
            value={formData.param1 ?? ""}/>
            <br/>

            <input 
            type="text" 
            name="param2" 
            onChange={handleFormInput} 
            placeholder="Parameter2" 
            value={formData.param2 ?? ""}/>
            <br/>

            <input 
            type="text" 
            name="result" 
            onChange={handleResponse}             
            placeholder="Result" 
            value={resultData.y ?? ""}/>
            <br/>            

            <button onClick={handleSubmit}>Submit</button> 
            {/* <button onClick={handleDebugSubmit}>Submit</button> */}
        </div>
    );
}

export default SimpleForm;
