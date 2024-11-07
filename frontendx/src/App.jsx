import './App.css'
// NA
// - https://reactrouter.com/docs/en/v6/getting-started/concepts
// - https://stackoverflow.com/questions/69843615/switch-is-not-exported-from-react-router-dom
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import {
  SimpleForm,
  SimpleTimeline
} from "./components";

function App() {
  return (
    <Router>
      <p>
        hello-react-ray-aws
      </p>
      <p>
        This is a model cell extending HYBRID-FALL2022-PPOD hello-react-ray example for use with AWS cloud deployment.
      </p>
      <ul>
        <li><Link to='/route1'>Simple Form</Link></li>
        <li><Link to='/route2'>Simple Timeline </Link></li>
      </ul>

      <div>
        <Routes>
          <Route path="/route1" element={<SimpleForm />} />
          <Route path="/route2" element={<SimpleTimeline />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
