/* eslint-disable prefer-template */
import axios from "axios";

// const HTTPCLIENT_BASE_URL = "http://localhost:8000";
// const HTTPCLIENT_BASE_URL = process.env.HTTPCLIENT_BASE_URL || "http://localhost:8000";
// NA.
// - MP. This is Vite specific.
const HTTPCLIENT_BASE_URL = import.meta.env.VITE_HTTPCLIENT_BASE_URL;
console.log("HTTPCLIENT_BASE_URL: " + HTTPCLIENT_BASE_URL);

// NA.
// - https://stackoverflow.com/questions/45578844/how-to-set-header-and-options-in-axios
// axios.defaults.headers.get['Content-Type'] = 'application/json';
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

const httpClient = axios.create({
  baseURL: HTTPCLIENT_BASE_URL,
});

httpClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    return Promise.resolve({ error });
  },
);

export default httpClient;
