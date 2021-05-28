import React, { useState } from "react";
import Logo from "../logo.svg";
import { Link, useHistory } from "react-router-dom";
import "../CSS/Navbar.css";

export default function Navbar() {
	const [isLoggedIn] = useState(false); // to be replaced with useContext
	const history = useHistory();

	function logout() {}

	return (
		<div className='custom-navbar'>
			<div className='nav-left'>
				<div className='nav-logo'>
					<Link to='/' className='logo-link'>
						<img src={Logo} alt='logo' className='logo' />
					</Link>
				</div>
				<div className='nav-logoCaption'>nametobedecided</div>
			</div>
			<div className='nav-right'>
				<div className='tab-container'>
					<Link to='/' className='tab'>
						ABCD
					</Link>
					<Link to='/' className='tab'>
						ABCD
					</Link>
					<Link to='/' className='tab'>
						ABCD
					</Link>
					{isLoggedIn ? (
						<Link className='tab' onClick={logout}>
							LogOut
						</Link>
					) : (
						<Link to='/login' className='tab'>
							Login
						</Link>
					)}
				</div>
			</div>
		</div>
	);
}
