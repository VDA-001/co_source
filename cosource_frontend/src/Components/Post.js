import React, { Component } from 'react'
import { CountryDropdown, RegionDropdown, CountryRegionData } from 'react-country-region-selector';
import "../CSS/Post.css"

class Post extends Component {
        constructor (props) {
            super(props);
            this.state = { country: '', region: '' };
        }
        
        selectCountry (val) {
            this.setState({ country: val });
        }
        
        selectRegion (val) {
            this.setState({ region: val });
        }
        
        render () {
            const { country, region } = this.state;
            return (
            <div>
            <div className="container">
            <div className="row">
            <div className="col-xl-6">
            <img src="undraw_add_post_64nu.svg" alt="" class="image" />
            </div>
            <div className="col-xl-6">
                <h2 className="text-center  text-uppercase mt-5">Post An Ad</h2>
                <div className="mb-3 mt-5">
                <label for="exampleFormControlTextarea1" className="form-label">Description</label>
                <textarea className="form-control text" id="exampleFormControlTextarea1" rows="3"></textarea>
                </div>
                <p className="form-label pb-2">Upload image</p>
                <input type="File" accept="image/*" class="mb-3"/>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Your Link</label>
                    <input type="link" class="form-control text" id="exampleFormControlInput1" placeholder="Add your link"/>
                </div>
        <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Phone no.</label>
                    <input type="phone" class="form-control text" id="exampleFormControlInput1" placeholder="Add your Phone no."/>
                </div>
        <div>
                <p className="form-label pb-2">Country</p>
                <CountryDropdown
                value={country}
                onChange={(val) => this.selectCountry(val)} class="form-select text" aria-label="Default select example"/>
            <p className="form-label pb-2">Region</p>
            <RegionDropdown
                country={country}
                value={region}
        onChange={(val) => this.selectRegion(val)} class="form-select text" aria-label="Default select example"/>
        </div>
        <button class="mt-4 btn">Submit an Ad</button>
        </div>
        </div>
        </div>
        </div>
        );
    }
}

export default Post
