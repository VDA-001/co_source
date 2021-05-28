import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
//import { firebase } from "../config/firebase";
import "../CSS/SignUp.css";

export default function SignUp() {
	const [form, setForm] = useState({
		email: "",
		password: "",
		name: "",
		phone: "",
		address: "",
		city: "",
		state: "",
		country: "",
	});
	const [isLoading, setIsLoading] = useState(false);
	const [err, setError] = useState("");
	const history = useHistory();
	function handleForm(e) {}
	function handleInput(e) {
		setForm({ ...form, [e.target.name]: e.target.value });
	}

	return (
		<div className='signup'>
			<div className='signup-left'>
				<p className='left-message'>
					Do your bit! <br />
					Contribute Valuable and Genuine leads!!!
				</p>
			</div>
			<div className='signup-right'>
				<div className='signup-container'>
					<div className='signup-form'>
						<div
							className={
								err ? "signup-header remove-padding" : "signup-header"
							}>
							SignUp
						</div>
						<div className='signup-fields'>
							<form onSubmit={handleForm} className='form-fields'>
								{err !== "" && <p className='err-message'>{err}</p>}
								<div className='input-container'>
									<input
										type='email'
										className='input-field-su'
										name='email'
										placeholder='Email'
										value={form.email}
										onChange={handleInput}
									/>
									<input
										type='password'
										className='input-field-su'
										name='password'
										placeholder='Password'
										value={form.password}
										onChange={handleInput}
									/>
								</div>
								<div className='input-container'>
									<input
										type='name'
										className='input-field-su'
										name='name'
										placeholder='Name'
										value={form.name}
										onChange={handleInput}
									/>
									<input
										type='phone'
										className='input-field-su'
										name='phone'
										placeholder='Phone'
										value={form.phone}
										onChange={handleInput}
									/>
								</div>
								<div className='input-container'>
									<input
										type='address'
										className='input-field-su'
										name='address'
										placeholder='Address'
										value={form.address}
										onChange={handleInput}
									/>
									<input
										type='city'
										className='input-field-su'
										name='city'
										placeholder='City'
										value={form.city}
										onChange={handleInput}
									/>
								</div>
								<div className='input-container'>
									<input
										type='state'
										className='input-field-su'
										name='state'
										placeholder='State'
										value={form.state}
										onChange={handleInput}
									/>
									<input
										type='country'
										className='input-field-su'
										name='country'
										placeholder='Country'
										value={form.country}
										onChange={handleInput}
									/>
								</div>
								<div className='button-container'>
									<button type='submit' className='signup-button'>
										{isLoading ? "Signing Up" : "SignUp"}
									</button>
								</div>
							</form>
						</div>
						<div className='sign-up-new'>
							<span>Already a User?</span>
							<Link className='signup-link' to='/login'>
								Log In!
							</Link>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}
