import React, { Component } from 'react';
import {Route, Switch} from "react-router-dom";

// import PageNotFound from "./PageNotFound";
import Header from "./components/common/Header";
import ProfilePage from "./components/core/ProfilePage";
import PrivateRoute from "./components/authentication/PrivateRoute";
import LoginPage from "./components/authentication/LoginPage";
import SignUpPage from "./components/authentication/SignUpPage";

import './App.css';

class App extends Component {
  render () {
    return (
      <div className="App">
        <Header/>
        <Switch>
          <PrivateRoute exact path="/" component={ProfilePage}/>
          <Route path="/login" component={LoginPage}/>
          <Route path="/sign-up" component={SignUpPage}/>
          {/* <Route component={PageNotFound}/> */}
        </Switch>
      </div>
    );
  }
}

export default App;
