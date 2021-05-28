import "./App.css";
import React from 'react'
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Redirect,
} from "react-router-dom";
import Navbar from "./Components/Navbar";
import HomePage from "./Pages/HomePage";
import SignUp from "./Pages/SignUp";
import Login from "./Pages/Login";

function App() {
	return (
		<div className='App'>
			<Router>
				<Navbar />
				<Switch>
					<Route exact path='/'>
						<HomePage />
					</Route>
					<Route exact path='/login'>
						<Login />
					</Route>
					<Route exact path='/signup'>
						<SignUp />
					</Route>
					{/* Redirecting non-matches to home */}
					<Route render={() => <Redirect to='/' />} />
				</Switch>
			</Router>
		</div>
	);
}

export default App;
