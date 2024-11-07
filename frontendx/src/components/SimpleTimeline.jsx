// SimpleTimeline.js

import React, { useState, useEffect } from "react";
import Plot from 'react-plotly.js';
//import httpClient from '../infra/httpClient';

const SimpleTimeline = () => {
    const [data, setData] = useState();

    useEffect(() => {
        /*
        httpClient
            .get("simples/")
            .then((response) => {
                const simples = response.data;
                console.log('useEffect1, simples: ', simples);

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
        */

        let data = { type: 'bar', x: [1, 2, 3], y: [2, 5, 3] }
        let dataTemplates = []
        dataTemplates.push(data)
        setData(dataTemplates)
    }, []);

    return (
        <div>
            <p>
                Simple Timeline
            </p>
            <Plot
                data={data}
                layout={{ width: 320, height: 240, title: 'A Fancy Plot 1' }}
            />
        </div>
    );
}

export default SimpleTimeline;

