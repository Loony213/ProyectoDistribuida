import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import DeleteUser from './DeleteUser';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/delete" component={DeleteUser} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
