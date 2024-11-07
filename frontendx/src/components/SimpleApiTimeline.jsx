import React, { useState, useEffect } from "react";
import Plot from 'react-plotly.js';
import httpClient from '../infra/httpClient';

// NA.
// - MP study this carefully.  Ask more questions regarding HTTP headers and why.
const SimpleTimeline = () => {
    const [data, setData] = useState();

    useEffect(() => {
        // NA.
        // NOTE: MP.  Ask more about this in a one on one meeting.
        // - https://jasonwatmore.com/post/2021/07/01/axios-http-get-request-examples
        const headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Access-Control-Allow-Origin': '*'
        };
        httpClient
            .get("/simples", { headers })       
            .then((response) => {
                const simples = response.data;
                console.log('simples: ', simples);

                let xs = simples.map(x => x["id"]);
                console.log('xs: ', xs);
                let ys = simples.map(y => y["id"] * 2);
                console.log('ys: ', ys);

                let dataTemplate1 = {
                    x: xs,
                    y: ys,
                    type: 'scatter',
                    mode: 'lines+markers',
                    marker: { color: 'red' },
                };

                let dataTemplate2 = { type: 'bar', x: [1, 2, 3], y: [2, 5, 3] };

                let dataTemplates = [];
                dataTemplates.push(dataTemplate1);
                dataTemplates.push(dataTemplate2);

                setData(dataTemplates);
            })
            .catch((error) => {
                const msg = "Error getting data" + error;
                console.error(msg);
            });
    }, []);

    return (
        <div>
            <Plot
                data={data}
                layout={{ width: 320, height: 240, title: 'A Fancy Plot 2' }}
            />
        </div>
    );
}

export default SimpleTimeline;
